import logging
from colorlog import ColoredFormatter

# Configureer de logging-instellingen
formatter = ColoredFormatter(
    "%(blue)s%(asctime)s - %(log_color)s%(levelname)s - %(white)s%(message)s",
    datefmt=None,
    reset=True,
    log_colors={
        'DEBUG': 'cyan',
        'INFO': 'green',
        'WARNING': 'yellow',
        'ERROR': 'red',
        'CRITICAL': 'bold_red',
    }
)

ch = logging.StreamHandler()
ch.setFormatter(formatter)

logger = logging.getLogger(__name__)
logger.addHandler(ch)
logger.setLevel(logging.DEBUG)

# Voorbeeldgebruik van de logger
logger.debug("Dit is een debug-bericht")
logger.info("Dit is een informatief bericht")
logger.warning("Dit is een waarschuwingsbericht")
logger.error("Dit is een foutbericht")
logger.critical("Dit is een kritiek bericht")
