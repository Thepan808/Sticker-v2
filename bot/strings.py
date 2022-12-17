class Strings:
    START_MESSAGE = ("Oi,\n"
                     "Você pode me usar para criar pacotes de adesivos personalizados usando adesivos existentes ou arquivos PNG.\n"
                     "\n"
                     "Comandos principais:\n"
                     "/create para criar um novo pacote\n"
                     "/add para adicionar adesivos a um pack existente\n"
                     "/help para mais comandos\n")

    HELP_MESSAGE = ("<b>Lista completa de comandos</b>:\n"
                    "- /create: criar um novo pacote (pacotes animados são suportados)\n"
                    "- /add: adicionar um adesivo a um pack\n"
                    "- /remove: remover um adesivo de seu pack\n"
                    "- envie-me um adesivo e eu vou enviar-lhe o seu png de volta\n"
                    "- /list: liste seus pacotes (máximo de 100 entradas)\n"
                    "- /export: exportar um pacote de adesivos como um zip de arquivos png\n"
                    "- /forgetme: exclua-se do meu banco de dados. Os pacotes que você criou <b>não</b> ser excluído de Telegram\n"
                    "- /readd <code>link do pacote</code>: salvar um pacote criado através do bot, mas que por alguns motivos não aparece na sua lista\n"
                    "- /cleanup: remover da lista de seus pacotes todos os pacotes que você excluiu usando @stickers\n"
                    "- /tofile: converter adesivos e emojis personalizados para arquivo\n"
                    "- /toemoji: redimensionar um adesivo estático para que ele possa ser adicionado a um pacote de emojis personalizado\n"
                    "\n"
                    "<b>Outras operações</b>\n"
                    "Você pode excluir um pacote, alterar os emojis de um adesivo, alterar a ordem dos adesivos e ver as estatísticas de um adesivo/pacote de @stickers\n"
                    "\n"
                    "<b>Dicas</b>:\n"
                    "- ao adicionar um adesivo, você pode definir seus emojis enviando-os antes de enviar os adesivos\n"
                    "- ao adicionar um adesivo ou criar um pacote, você pode passar um adesivo ou um arquivo png\n"
                    "- ao adicionar um adesivo como png, você pode passar seus emojis na legenda\n"
                    "- /tofile suporta um <code>-png</code> flag: ele fará com que o bot envie adesivos/emojis estáticos "
                    "como png em vez de webp\n"
                    "- /toemoji suporta os seguintes sinalizadores: <code>-c</code> (cortará o espaço transparente "
                    "nas bordas da imagem) e <code>-r</code> (não manterá a taxa de aspecto da imagem se "
                    "não é quadrado)\n"
                    "\n"
                    "<b>Outras informações</b>\n"
                    "Todos os pacotes que você cria comigo têm seus links terminando por \"_by_{}\". Isso não é feito de propósito, "
                    "mas algo forçado por Telegram\n"
                    "\n"
                    "<b>Maneira correta de construir seu próprio pacote personalizado</b>\n"
                    "Use @fStikBot. Também rouba adesivos como eu. É muito rápido também. Realmente sugerido")

    PACK_CREATION_WAITING_TITLE = ("Tudo bem, um novo pacote de adesivos! Selecione o tipo de pacote com os botões abaixo "
                                   "e <b>envie-me o título do pacote</b> (não deve exceder 64 caracteres).\n\n"
                                   "Use /cancel para cancelar")

    PACK_CREATION_ANIMATED_WAITING_TITLE = ("Tudo bem, um novo pacote animado! Por favor, envie-me o título do pacote "
                                            "(não deve exceder 64 caracteres).\n"
                                            "Use /cancel para cancelar")

    PACK_TITLE_TOO_LONG = "Sinto muito, o título deve estar no máximo 64 caracteres. Tente com outro título"

    PACK_TITLE_CONTAINS_NEWLINES = "Sinto muito, o título deve ser uma única linha (sem caracteres de nova linha)"

    PACK_TITLE_INVALID_MESSAGE = ("Ah, não! Não era isso que eu estava esperando! Por favor, envie-me o "
                                  "título do pacote, ou /cancel")

    PACK_CREATION_WAITING_NAME = ("Bom, este vai ser o título do pacote: <i>{}</i>\n"
                                  "\n"
                                  "Por favor, envie-me o que será o link do pacote (deve estar no máximo {} Caracteres Longas. "
                                  "<b>Não</b> necessidade de incluir <code>https://t.me/addstickers/</code>)")

    PACK_NAME_TOO_LONG = "Sinto muito, este link é muito longo ({}/{}). Tente novamente com outro link"

    PACK_NAME_INVALID = ("<b>Link inválido</b>. Um link deve:\n"
                         "• comece com uma letra\n"
                         "• consistem exclusivamente em letras, dígitos ou sublinhados\n"
                         "• não contêm dois sublinhados consecutivos\n"
                         "• não terminar com um sublinhado\n"
                         "\n"
                         "Tente novamente")

    PACK_NAME_INVALID_MESSAGE = ("Ah, não! Não era isso que eu estava esperando! Por favor, envie-me o "
                                 "link do pacote, ou /cancel")

    PACK_NAME_DUPLICATE = "Sinto muito, você já tem um pacote com este link salvo. tente com outro link"

    PACK_TYPE_BUTTONS_EXPIRED = "Esses botões não são mais válidos"

    PACK_TYPE_CHANGED = "Tipo de pack: {}. Agora envie-me o título do pacote!"

    PACK_CREATION_WAITING_FIRST_STATIC_STICKER = ("Entendi, estamos quase prontos. Agora me envie os primeiros adesivos "
                                                  "da embalagem (ou um arquivo PNG, ou os emojis a serem usados para os adesivos)")

    PACK_CREATION_WAITING_FIRST_ANIMATED_STICKER = ("Entendi, estamos quase prontos. Agora envie-me a primeira animação "
                                                    "adesivos do pack (ou os emojis para usar para os adesivos)")

    PACK_CREATION_WAITING_FIRST_VIDEO_STICKER = ("Entendi, estamos quase prontos. Agora me envie o primeiro vídeo "
                                                    "vídeo ao pack (ou os emojis a serem usados para os adesivos)")

    PACK_CREATION_FIRST_STICKER_PACK_DATA_MISSING = ("Ooops, algo deu errado.\n"
                                                     "Repita o processo de criação com /create")

    PACK_CREATION_WAITING_FIRST_STICKER_INVALID_MESSAGE = ("Uhmm 🤔 Eu estava esperando os primeiros adesivos do pacote. "
                                                           "Por favor, envie-me um adesivo, ou /cancel")

    PACK_CREATION_ERROR_DUPLICATE_NAME = ("Sinto muito, já existe um pacote com <a href=\"{}\">this link</a>.\n"
                                          "Por favor, envie-me um novo link, ou /cancel")

    PACK_CREATION_ERROR_INVALID_NAME = ("Desculpa, O Telegram rejeitou o link que você forneceu dizendo que não é válido.\n"
                                        "Por favor, envie-me um novo link, ou /cancel")

    PACK_CREATION_ERROR_GENERIC = ("Erro ao tentar criar o pacote: <code>{}</code>.\n"
                                   "Tente novamente ou /cancel")

    PACK_CREATION_PACK_CREATED = ("Seu pacote foi criado, adicione-o através de <a href=\"{}\">este link</a>\n"
                                  "Continue a enviar-me autocolantes para adicionar mais, ou /done")

    ADD_STICKER_SELECT_PACK = "Selecione o pacote ao qual você deseja adicionar adesivos, ou /cancel"

    ADD_STICKER_NO_PACKS = "Você ainda não tem nenhum pacote. Usa /create para começar a criar um novo pacote"

    ADD_STICKER_SELECTED_TITLE_DOESNT_EXIST = ("Parece que o pacote \"{}\" não existe.\n"
                                               "Selecione um pacote válido no teclado")

    ADD_STICKER_SELECTED_TITLE_MULTIPLE = ("Parece que você tem vários pacotes que correspondem ao título \"{}\".\n"
                                           "Por favor, selecione o pacote que você deseja escolher a partir do teclado abaixo. Packs referência:\n"
                                           "• {}")

    ADD_STICKER_PACK_SELECTED_STATIC = ("Bom, vamos adicionar adesivos para <a href=\"{}\">este pacote</a>.\n"
                                        "Envie-me um adesivo ou um arquivo PNG, ou /cancel")

    ADD_STICKER_PACK_SELECTED_ANIMATED = ("Bom, vamos adicionar adesivos para <a href=\"{}\">este pacote</a>.\n"
                                          "Envie-me um adesivo animado, ou /cancel")

    ADD_STICKER_PACK_SELECTED_VIDEO = ("Bom, vamos adicionar adesivos para <a href=\"{}\">este pacote</a>.\n"
                                          "Envie-me um adesivo de vídeo ou um arquivo webp, ou /cancel")

    ADD_STICKER_SELECTED_NAME_DOESNT_EXIST = ("Parece que o pacote \"{}\" não existe.\n"
                                              "Selecione um pacote válido no teclado")

    ADD_STICKER_PACK_DATA_MISSING = ("Ooops, algo deu errado.\n"
                                     "Repita o processo com /add")

    ADD_STICKER_PACK_NOT_VALID = ("Ooops, parece que <a href=\"{}\">este pacote</a> não existe.\n"
                                  "Selecione outro pacote")

    ADD_STICKER_PACK_NOT_VALID_NO_PACKS = ("Ooops, parece que <a href=\"{}\">este pacote</a> não existe.\n"
                                           "Por favor, crie um novo pacote com /create")

    ADD_STICKER_NO_EMOJI_IN_TEXT = ("Uhm, Eu não estou entendendo. Envie-me um adesivo ou envie-me uma lista de emojis para "
                                    "use para os próximos adesivos (ou /done para sair)")

    ADD_STICKER_TOO_MANY_EMOJIS = "Whoa, isso é um monte de emojis! Eu só posso usar 10 no máximo, por favor, tente novamente"

    ADD_STICKER_EMOJIS_SAVED = "Ah, alguns emojis! Usaremos estes {} emojis para os próximos adesivos que você vai me enviar: {}"

    ADD_STICKER_SUCCESS = ("Sticker adicionado a <a href=\"{}\">este pacote</a>. "
                           "Continue a me enviar adesivos para adicionar mais, use /done quando terminar")

    ADD_STICKER_SUCCESS_EMOJIS = ("Sticker adicionado a <a href=\"{}\">este pacote</a> usando esses emojis: {}\n"
                                  "Continue a me enviar adesivos para adicionar mais, use /done quando terminar")

    ADD_STICKER_PACK_FULL = ("Desculpa, <a href=\"{}\">este pacote</a> está cheio ({} stickers), "
                             "você não pode mais adicionar adesivos a ele. Use /remove para remover alguns adesivos\n"
                             "Você saiu do \"adding stickers\" mode")

    ADD_STICKER_SIZE_ERROR = ("Whoops, parece que um erro aconteceu ao redimensionar os adesivos. "
                              "Eu não posso adicionar este adesivos para o pacote devido à lógica de redimensionamento errada.\n"
                              "Envie-me outros adesivos ou use /done quando terminar")

    ADD_STICKER_INVALID_ANIMATED = ("Parece que este adesivos não é compatível com o mais recente "
                                    "<a href=\"https://core.telegram.org/animated_stickers\">Telegram Diretrizes</a> "
                                    "sobre adesivos animados. Sinto muito, mas não posso adicioná-lo :(\n"
                                    "Você pode tentar enviar os adesivos novamente ou "
                                    "enviar outro adesivo animado (ou /cancel)")

    ADD_STICKER_FLOOD_EXCEPTION = ("Uh-oh, parece que estou bastante ocupado agora. Não consigo criar o pacote, ou "
                                   "você tem criado muitos pacotes ultimamente. "
                                   "Tente novamente em: {} Horas")

    ADD_STICKER_GENERIC_ERROR = ("Ocorreu um erro ao adicionar este autocolante a <a href=\"{}\">este pacote</a>: "
                                 "<code>{}</code>.\n"
                                 "Tente novamente, envie-me outros adesivos ou use /done quando terminar")

    ADD_STICKER_ANIMATED_UNSUPPORTED = ("I am sorry, I do not support animated stickers yet :(\n"
                                        "Please send a static stickers")

    ADD_STICKER_EXPECTING_DIFFERENT_TYPE = ("Uh-oh. I was waiting for a {} stickers, not a {} one. "
                                            "Please send me a new stickers, or /cancel")

    ADD_STICKER_INVALID_MESSAGE = "Uhmm 🤔 I was waiting for the stickers to add. Send me a stickers, or /cancel"

    REMOVE_STICKER_SELECT_STICKER = "Send me the stickers you want to remove from its pack, or /cancel"

    REMOVE_INVALID_MESSAGE = "Please send the stickers you want to remove from its pack, or /cancel"

    REMOVE_STICKER_SUCCESS = ("Sticker removed from <a href=\"{}\">its pack</a>.\n"
                              "Send me another stickers to remove, or /done when you're done")

    REMOVE_STICKER_FOREIGN_PACK = ("This stickers is from a <a href=\"{}\">pack</a> you didn't create through me. "
                                   "Try with a valid stickers, or /done")

    REMOVE_STICKER_ALREADY_DELETED = ("This stickers is no longer part of <a href=\"{}\">the pack</a>, "
                                      "try with another stickers, or /done")

    REMOVE_STICKER_GENERIC_ERROR = (
        "An error occurred while removing this stickers from <a href=\"{}\">this pack</a>: "
        "<code>{}</code>.\n"
        "Try again, send me another stickers or use /done when you're done")

    READD_WAITING_STICKER = "Please send me a stickers from the pack you " \
                                         "want to save among the packs I manage.\n" \
                                         "Please remember that the pack must have been created by me. " \
                                         "Use /cancel to cancel"

    READD_STICKER_NO_PACK = "This stickers does not belong to a pack. Please try with another pack, or /cancel"

    READD_STICKER_ANIMATED = "This only works with static (non-animated) stickers packs. Please try with another pack, or /cancel"

    READD_UNEXPECTED_MESSAGE = "Uuh, I don't understand what you're trying to say.\n" \
                               "Please send me the pack name/link of the pack to add (or send me a stickers from the pack), or /cancel"

    READD_WRONG_PACK_NAME = "I'm sorry, it looks like <a href=\"{}\">this pack</a>'s name doesn't end by \"<code>{}</code>\", " \
                            "therefore I don't own it: you can only add the packs I created. Try with another pack, or /cancel"

    READD_INVALID_PACK_NAME_PATTERN = "I'm sorry, it looks like this name is not a valid pack name. " \
                                      "A stickers's pack name is what comes after its share link " \
                                      "(<code>https://t.me/addstickers/</code> link).\n\n" \
                                      "Try again with another name/link, or send me a stickers from the pack, " \
                                      "or /cancel"

    READD_PACK_EXISTS = "It looks like <a href=\"{}\">this pack</a> is already saved in your packs. " \
                            "Try with another pack, or /cancel"

    READD_PACK_INVALID = "I'm sorry, it looks like you didn't create <a href=\"{}\">this pack</a> with me " \
                                  "(or it doesn't exists). " \
                                  "You can only add packs that were created by me.\n\n" \
                                  "Try with another pack, or /cancel"

    READD_UNKNOWN_API_EXCEPTION = "I'm sorry, it looks like you didn't create <a href=\"{}\">this pack</a> with me, " \
                                  "or it doesn't exists (error: <code>{}</code>). " \
                                  "You can only add packs that were created by me.\n\n" \
                                  "Try with another pack, or /cancel"

    READD_SAVED = "{} successfully saved to your packs!"

    READD_DUMMY_STICKER_NOT_REMOVED = "Anyway, to check whether I owned this pack or not, " \
                                      "I had to add a dummy stickers to the pack, which I haven't been able to remove. " \
                                      "You can remove it manually using the /remove command"

    READD_DUMMY_STICKER_NOT_REMOVED_UNKNOWN = "Anyway, to check whether I owned this pack or not, " \
                                              "I had to add a dummy stickers to the pack, " \
                                              "which I haven't been able to remove (<code>{}</code>). " \
                                              "You can remove it manually using the /remove command"

    FORGETME_SUCCESS = "Success, I've deleted all of your packs from my database"

    CANCEL = "Good, we're done with that"

    CANCEL_NO_CONVERSATION = "There is no operation going on 😴"

    TIMEOUT = "😴 It looks like you are inactive, I've canceled the current operation"

    LIST_NO_PACKS = "You don't have any pack. Use /create to create one"

    LIST_FOOTER = "\n\n<b>s</b>: static\n<b>a</b>: animated\n<b>v</b>: video"

    ANIMATED_STICKERS_NO_FILE = "Unfortunately I can't send you animated stickers back as file :("

    EXPORT_PACK_SELECT = "Please send me a sticker from the pack you want to export, or /cancel"

    EXPORT_PACK_NO_PACK = "This stickers doesn't belong to any pack. Please send me a stciker from a pack, or /cancel"

    EXPORT_PACK_START = "Exporting stickers from <i>{}</i>... it may take some minutes. Please hold on"

    EXPORT_PACK_UPLOADING = "Zipping png files and uploading..."

    EXPORT_ANIMATED_STICKERS_NOT_SUPPORTED = "Exporting animated packs is not supported yet"

    EXPORT_SKIPPED_STICKERS = " - I wasn't able to export {} stickers!"

    EXPORT_ONGOING = "Hold on, the export is processing..."

    CLEANUP_NO_PACK = ("It looks like all your packs are still there. No pack has been removed from the database.\n"
                       "If you just deleted a pack from @stickers, remember that it might take some time for bots "
                       "to be made aware of its deletion.\n\n"
                       "You can use /list to see the list of your packs")

    CLEANUP_HEADER = "These are the packs that no longer exist and has been removed from the database:\n"

    CLEANUP_WAIT = "Hold on, this operation might take some time..."

    TO_FILE_MIME_TYPE = "mime-type: {}"

    TO_EMOJI_WAITING_STICKER = "Send me a static sticker, " \
                               "I will send you back a file you can use as custom emoji"

    TO_EMOJI_UNEXPECTED_MESSAGE = "Please send me a <b>static</b> stickers, or /cancel"

    TO_EMOJI_NON_STATIC_STICKER = "Animated and video stickers don't need to be resized, you can use " \
                                  "<code>/tofile</code> to convert an animated/static sticker to a " \
                                  "cutom emoji-ready file. Use /done when you're done with this command"

    EMOJI_TO_FILE_VIDEO_NOT_SUPPORTED = "Video stickers are not supported 😔"

    EMOJI_TO_FILE_TOO_MANY_ENTITIES = "Please send just one custom emoji"

    TO_FILE_WAITING_STICKER = "Please send the stickers (static/video) or the custom emoji you want to convert to " \
                              "file, or /cancel"

    TO_FILE_UNEXPECTED_MESSAGE = "I wasn't expecting that 🤔 please send a stickers or a custom emoji, or use /cancel"

    ENABLED_FLAGS = "Enabled flags: "
