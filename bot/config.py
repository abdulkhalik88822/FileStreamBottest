from os import environ as env

class Telegram:
    API_ID = int(env.get("TELEGRAM_API_ID", 14982593))
    API_HASH = env.get("TELEGRAM_API_HASH", "86ce0656fecb2690a633dd60808e74d6")
    OWNER_ID = int(env.get("OWNER_ID", 5543917190))
    ALLOWED_USER_IDS = env.get("ALLOWED_USER_IDS", "").split()
    BOT_USERNAME = env.get("TELEGRAM_BOT_USERNAME", "@AmRobots_File_Stream_Bot")
    BOT_TOKEN = env.get("TELEGRAM_BOT_TOKEN", "7229199824:AAHV1xN5CRx5VQu2yohcCnCDHYF37Kc1374")
    CHANNEL_ID = int(env.get("TELEGRAM_CHANNEL_ID", -1001744824600))
    SECRET_CODE_LENGTH = int(env.get("SECRET_CODE_LENGTH", 12))

class Server:
    BASE_URL = env.get("BASE_URL", "http://vps.hostingup.icu:8080")
    BIND_ADDRESS = env.get("BIND_ADDRESS", "0.0.0.0")
    PORT = int(env.get("PORT", 8080))

# LOGGING CONFIGURATION
LOGGER_CONFIG_JSON = {
    'version': 1,
    'formatters': {
        'default': {
            'format': '[%(asctime)s][%(name)s][%(levelname)s] -> %(message)s',
            'datefmt': '%d/%m/%Y %H:%M:%S'
        },
    },
    'handlers': {
        'file_handler': {
            'class': 'logging.FileHandler',
            'filename': 'event-log.txt',
            'formatter': 'default'
        },
        'stream_handler': {
            'class': 'logging.StreamHandler',
            'formatter': 'default'
        }
    },
    'loggers': {
        'uvicorn': {
            'level': 'INFO',
            'handlers': ['file_handler', 'stream_handler']
        },
        'uvicorn.error': {
            'level': 'WARNING',
            'handlers': ['file_handler', 'stream_handler']
        },
        'bot': {
            'level': 'INFO',
            'handlers': ['file_handler', 'stream_handler']
        }
    }
}
