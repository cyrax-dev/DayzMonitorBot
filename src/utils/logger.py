from loguru import logger
import sys

logger.remove()


logger.add(
    sys.stdout,
    format="<e>[{time:YY-MM-DD / HH:mm}]</> <g>({level}) →</> <w>{message}</>",
    level="DEBUG",
    colorize=True,
    filter=lambda record: record["level"].name == "INFO",
)

logger.add(
    sys.stdout,
    format="<e>[{time:YY-MM-DD / HH:mm}]</> <y>({level}) →</> <m>{message}</>",
    level="DEBUG",
    colorize=True,
    filter=lambda record: record["level"].name == "WARNING",
)

logger.add(
    sys.stdout,
    format="<e>[{time:YY-MM-DD / HH:mm}]</> <r>({level}) →</> <y>[{module}:{line}] →</> <r>{message}</>",
    level="DEBUG",
    colorize=True,
    enqueue=True,
    filter=lambda record: record["level"].name == "ERROR",
)

logger.add(
    "settings/logs/logfile.log",
    format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {module}:{line} | {message}",
    level="DEBUG",
    rotation="10 MB",
    compression="zip",
    backtrace=True,
    diagnose=True,
    filter=lambda record: record["level"].name == "ERROR",
)

log = logger
