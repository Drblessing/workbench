from pathlib import Path

module_path = Path(__file__)
log_dir = module_path.parent / "logs"

# Create the log directory if it doesn't exist
log_dir.mkdir(parents=True, exist_ok=True)

import logging

# test logging to log_dir

logging.basicConfig(
    filename=log_dir / "log.log",
)

logging.critical("The nuclear reactor is about to explode!")
