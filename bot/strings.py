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

    ADD_STICKER_ANIMATED_UNSUPPORTED = ("Lamento, ainda não apoio autocolantes animados :(\n"
                                        "Por favor, envie um adesivo estático")

    ADD_STICKER_EXPECTING_DIFFERENT_TYPE = ("Uh-oh. Eu estava esperando por um {} stickers, não é um {} Um. "
                                            "Por favor, envie-me um novo adesivo, ou /cancel")

    ADD_STICKER_INVALID_MESSAGE = "Uhmm 🤔 Eu estava esperando os adesivos para adicionar. Envie-me um adesivo, ou /cancel"

    REMOVE_STICKER_SELECT_STICKER = "Envie-me os adesivos que você deseja remover de seu pack, ou /cancel"

    REMOVE_INVALID_MESSAGE = "Por favor, envie os adesivos que você deseja remover de seu pacote, ou /cancel"

    REMOVE_STICKER_SUCCESS = ("Sticker removido de <a href=\"{}\">seu pack</a>.\n"
                              "Envie-me outros adesivos para remover, ou /done quando terminar")

    REMOVE_STICKER_FOREIGN_PACK = ("Este adesivo é de um <a href=\"{}\">pack</a> você não criou através de mim. "
                                   "Tente com um adesivo válido, ou /done")

    REMOVE_STICKER_ALREADY_DELETED = ("Este adesivo não faz mais parte do <a href=\"{}\">o pack</a>, "
                                      "tente com outros adesivos, ou /done")

    REMOVE_STICKER_GENERIC_ERROR = (
        "Ocorreu um erro ao remover este adesivo de <a href=\"{}\">este pacote</a>: "
        "<code>{}</code>.\n"
        "Tente novamente, envie-me outros adesivos ou use /done quando terminar")

    READD_WAITING_STICKER = "Por favor, envie-me um adesivo do pacote que você " \
                                         "quero salvar entre os pacotes que eu gerencio.\n" \
                                         "Por favor, lembre-se que o pacote deve ter sido criado por mim. " \
                                         "Use /cancel para cancelar"

    READD_STICKER_NO_PACK = "Este adesivo não pertence a um pacote. Por favor, tente com outro pacote, ou /cancel"

    READD_STICKER_ANIMATED = "Isso só funciona com pacotes de adesivos estáticos (não animados). Por favor, tente com outro pacote, ou /cancel"

    READD_UNEXPECTED_MESSAGE = "Uuh, Eu não entendo o que você está tentando dizer.\n" \
                               "Por favor, envie-me o nome do pacote / link do pacote para adicionar (ou envie-me um adesivo do pacote), ou /cancel"

    READD_WRONG_PACK_NAME = "Sinto muito, parece que <a href=\"{}\">este pacote</a>'s name não termina por \"<code>{}</code>\", " \
                            "portanto, eu não o possuo: você só pode adicionar os pacotes que eu criei. Tente com outro pacote, ou /cancel"

    READD_INVALID_PACK_NAME_PATTERN = "Sinto muito, parece que este nome não é um nome de pacote válido. " \
                                      "O nome de um pacote de adesivos é o que vem depois de seu link de compartilhamento " \
                                      "(<code>https://t.me/addstickers/</code> link).\n\n" \
                                      "Tente novamente com outro nome/link, ou envie-me um adesivo para o pack, " \
                                      "ou /cancel"

    READD_PACK_EXISTS = "Parece que <a href=\"{}\">este pacote</a> já está salvo em seus pacotes. " \
                            "Tente com outro pacote, ou /cancel"

    READD_PACK_INVALID = "Sinto muito, parece que você não criou <a href=\"{}\">este pacote</a> comigo " \
                                  "(ou não existe). " \
                                  "Você só pode adicionar pacotes que foram criados por mim.\n\n" \
                                  "Tente com outro pacote, ou /cancel"

    READD_UNKNOWN_API_EXCEPTION = "Sinto muito, parece que você não criou <a href=\"{}\">este pacote</a> comigo, " \
                                  "ou não existe (error: <code>{}</code>). " \
                                  "Você só pode adicionar pacotes que foram criados por mim.\n\n" \
                                  "Tente com outro pacote, ou /cancel"

    READD_SAVED = "{} salvo com sucesso em seus pacotes!"

    READD_DUMMY_STICKER_NOT_REMOVED = "Enfim, para verificar se eu possuía esse pacote ou não, " \
                                      "Eu tive que adicionar um adesivo fictício ao pacote, que eu não consegui remover. " \
                                      "Você pode removê-lo manualmente usando o botão /remove comando"

    READD_DUMMY_STICKER_NOT_REMOVED_UNKNOWN = "Enfim, para verificar se eu possuía esse pacote ou não, " \
                                              "Eu tive que adicionar um adesivo fictício ao pacote, " \
                                              "que eu não consegui remover (<code>{}</code>). " \
                                              "Você pode removê-lo manualmente usando o botão /remove comando"

    FORGETME_SUCCESS = "Sucesso, eu apaguei todos os seus pacotes do meu banco de dados"

    CANCEL = "Bom, nós terminamos com isso"

    CANCEL_NO_CONVERSATION = "Não há nenhuma operação em andamento 😴"

    TIMEOUT = "😴 Parece que você está inativo, eu cancelei a operação atual"

    LIST_NO_PACKS = "Você não tem nenhum pacote. Use /create para criar um pack"

    LIST_FOOTER = "\n\n<b>s</b>: estático\n<b>a</b>: animado\n<b>v</b>: video"

    ANIMATED_STICKERS_NO_FILE = "Infelizmente eu não posso enviar-lhe adesivos animados de volta como arquivo :("

    EXPORT_PACK_SELECT = "Por favor, envie-me um adesivo do pacote que você deseja exportar, ou /cancel"

    EXPORT_PACK_NO_PACK = "Este adesivo não pertence a nenhum pacote. Por favor, envie-me um sticker de um pacote, ou /cancel"

    EXPORT_PACK_START = "Exportação de adesivos de <i>{}</i>... pode levar alguns minutos. Por favor, aguarde"

    EXPORT_PACK_UPLOADING = "Compactando arquivos png e carregando..."

    EXPORT_ANIMATED_STICKERS_NOT_SUPPORTED = "A exportação de pacotes animados ainda não é suportada"

    EXPORT_SKIPPED_STICKERS = " - Não consegui exportar {} stickers!"

    EXPORT_ONGOING = "Espere, a exportação está sendo processada..."

    CLEANUP_NO_PACK = ("Parece que todos os seus pacotes ainda estão lá. Nenhum pacote foi removido do banco de dados.\n"
                       "Se você acabou de excluir um pacote de @stickers, lembre-se de que pode levar algum tempo para os bots "
                       "ser informado da sua supressão.\n\n"
                       "Você pode usar /list para ver a lista de seus packs")

    CLEANUP_HEADER = "Estes são os pacotes que não existem mais e foram removido do banco de dados:\n"

    CLEANUP_WAIT = "Espere, esta operação pode levar algum tempo..."

    TO_FILE_MIME_TYPE = "mime-type: {}"

    TO_EMOJI_WAITING_STICKER = "Envie-me um adesivo estático, " \
                               "Vou enviar-lhe de volta um arquivo que você pode usar como emoji personalizado"

    TO_EMOJI_UNEXPECTED_MESSAGE = "Por favor, envie-me um <b>estático</b> stickers, ou /cancel"

    TO_EMOJI_NON_STATIC_STICKER = "Adesivos animados e de vídeo não precisam ser redimensionados, você pode usar " \
                                  "<code>/tofile</code> para converter um adesivo animado/estático em um " \
                                  "arquivo customizado emoji-pronto. Use /done quando terminar de usar este comando"

    EMOJI_TO_FILE_VIDEO_NOT_SUPPORTED = "Adesivos de vídeo não são suportados 😔"

    EMOJI_TO_FILE_TOO_MANY_ENTITIES = "Por favor, envie apenas um emoji personalizado"

    TO_FILE_WAITING_STICKER = "Por favor, envie os adesivos (estático/vídeo) ou o emoji personalizado para o qual você deseja converter " \
                              "arquivo ou /cancel"

    TO_FILE_UNEXPECTED_MESSAGE = "Eu não estava esperando isso 🤔 por favor, envie um adesivo ou um emoji personalizado, ou use /cancel"

    ENABLED_FLAGS = "Sinalizadores habilitados: "
