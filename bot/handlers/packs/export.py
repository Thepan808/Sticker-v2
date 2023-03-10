import json
import logging
import tempfile
import time
import zipfile
from html import escape as html_escape

# noinspection PyPackageRequirements
from telegram import ChatAction, ParseMode, Update
# noinspection PyPackageRequirements
from telegram.error import BadRequest, TelegramError
# noinspection PyPackageRequirements
from telegram.ext import (
    CommandHandler,
    MessageHandler,
    ConversationHandler,
    CallbackContext,
    Filters
)

from bot import stickersbot
from bot.stickers import StickerFile
from bot.strings import Strings
from config import config
from ..conversation_statuses import Status
from ..fallback_commands import cancel_command
from ...utils import decorators
from ...utils import utils
from ...utils.pyrogram import get_set_emojis_dict

logger = logging.getLogger(__name__)


class DummyMessage:
    def __init__(self, sticker):
        self.sticker = sticker
        self.document = None


@decorators.action(ChatAction.TYPING)
@decorators.restricted
@decorators.failwithmessage
@decorators.logconversation
def on_export_command(update: Update, _):
    logger.info('/export')

    update.message.reply_text(Strings.EXPORT_PACK_SELECT)

    return Status.WAITING_STICKER


@decorators.action(ChatAction.UPLOAD_DOCUMENT)
@decorators.failwithmessage
@decorators.logconversation
def on_sticker_receive(update: Update, context: CallbackContext):
    logger.info('usuário enviou um sticker do pacote para exportar')

    if not update.message.sticker.set_name:
        update.message.reply_text(Strings.EXPORT_PACK_NO_PACK)
        return Status.WAITING_STICKER

    sticker_set = context.bot.get_sticker_set(update.message.sticker.set_name)

    base_progress_message = Strings.EXPORT_PACK_START.format(html_escape(sticker_set.title))
    message_to_edit = update.message.reply_html(base_progress_message, quote=True)

    pack_emojis = dict()  # we need to create this dict just in case the pyrogram request fails

    with tempfile.TemporaryDirectory() as tmp_dir:
        logger.info('using %s as TemporaryDirectory', tmp_dir)

        with tempfile.TemporaryFile() as tmp_file:  # temporary zip file
            with zipfile.ZipFile(tmp_file, 'w') as zip_file:

                total = len(sticker_set.stickers)
                skipped_stickers = 0
                for i, sticker in enumerate(sticker_set.stickers):
                    # noinspection PyTypeChecker
                    sticker_file = StickerFile(
                        DummyMessage(sticker),  # we do not have a Message but we need it,
                        emojis=[sticker.emoji],  # we need to pass them explicitly so we avoid the Pyrogram request
                        tempfile_to_use=tempfile.NamedTemporaryFile(dir=tmp_dir)
                    )

                    # noinspection PyBroadException
                    try:
                        sticker_file.download()
                        pack_emojis[sticker.file_id] = sticker_file.emojis
                    except Exception:
                        logger.info('erro ao baixar e converter um adesivo que precisamos exportar', exc_info=True)
                        sticker_file.close()
                        skipped_stickers += 1
                        continue

                    # https://stackoverflow.com/a/54202259
                    zip_file.writestr(f'{sticker_file.file_unique_id}.{sticker_file.get_extension()}', sticker_file.sticker_tempfile.read())
                    sticker_file.close()

                    # edit message every 10 exported stickers, or when we're done
                    progress = i + 1
                    if progress == total or progress % 10 == 0:
                        try:
                            message_to_edit.edit_text(
                                '{} (progress: {}/{})'.format(base_progress_message, progress, total),
                                parse_mode=ParseMode.HTML
                            )
                            time.sleep(1)  # we do not want to get rate-limited
                        except (TelegramError, BadRequest) as e:
                            logger.warning('erro ao editar a mensagem de progresso: %s', e.message)

                stickers_emojis_dict = pack_emojis
                if config.pyrogram.enabled:
                    try:
                        stickers_emojis_dict = get_set_emojis_dict(update.message.sticker.set_name)
                    except Exception as e:
                        logger.error('erro ao tentar obter os emojis do pacote com pirograma: %s', str(e), exc_info=True)

                with tempfile.SpooledTemporaryFile() as tmp_json:
                    tmp_json.write(json.dumps(stickers_emojis_dict, indent=2).encode())
                    tmp_json.seek(0)
                    zip_file.writestr('emojis.json', tmp_json.read())

                message_to_edit.reply_text(Strings.EXPORT_PACK_UPLOADING, quote=True)

            tmp_file.seek(0)

            update.message.reply_document(
                tmp_file,
                filename='{}.zip'.format(sticker_set.name),
                caption='<a href="{}">{}</a>{}'.format(
                    utils.name2link(sticker_set.name),
                    html_escape(sticker_set.title),
                    Strings.EXPORT_SKIPPED_STICKERS.format(skipped_stickers) if skipped_stickers != 0 else ""
                ),
                parse_mode=ParseMode.HTML,
                quote=True
            )

    return ConversationHandler.END


@decorators.action(ChatAction.TYPING)
@decorators.failwithmessage
@decorators.logconversation
def on_animated_sticker_receive(update: Update, _):
    logger.info('usuário enviou um adesivos animados')

    update.message.reply_text(Strings.EXPORT_ANIMATED_STICKERS_NOT_SUPPORTED)

    return Status.WAITING_STICKER


@decorators.action(ChatAction.TYPING)
@decorators.failwithmessage
@decorators.logconversation
def on_ongoing_async_operation(update: Update, _):
    logger.info('user sent a message while the export is ongoing')

    update.message.reply_text(Strings.EXPORT_ONGOING)

    # end the conversations maybe?
    # return ConversationHandler.END  # end the conversations maybe?


stickersbot.add_handler(ConversationHandler(
    name='export_command',
    persistent=False,
    entry_points=[CommandHandler(['export', 'e', 'dump'], on_export_command)],
    states={
        Status.WAITING_STICKER: [
            MessageHandler(Filters.sticker, on_sticker_receive, run_async=True),
        ],
        # ConversationHandler.TIMEOUT: [MessageHandler(Filters.all, on_timeout)]
        ConversationHandler.WAITING: [MessageHandler(Filters.all, on_ongoing_async_operation)]
    },
    fallbacks=[CommandHandler(['cancel', 'c', 'done', 'd'], cancel_command)],
    # conversation_timeout=15 * 60
))
