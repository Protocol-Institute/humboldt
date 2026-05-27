"""Entry point for the Humboldt daemon."""

import logging
import os
import sys
from pathlib import Path

from dotenv import load_dotenv

load_dotenv(Path(__file__).parent.parent / ".env")

from .discord_client import HumboldtBot

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s  %(name)-24s  %(levelname)s  %(message)s",
)


def run():
    token = os.environ.get("DISCORD_BOT_TOKEN")
    if not token:
        raise RuntimeError("DISCORD_BOT_TOKEN not set — copy from .env.keys to .env")
    bot = HumboldtBot()
    bot.run(token, log_handler=None)
    # If close() was called because of a reload request (!reload DM or SIGUSR1),
    # replace the current process with a fresh one.  State is already saved.
    if bot.reload_requested:
        logging.getLogger("humboldt.runner").info("Reloading daemon process with updated code")
        os.execv(sys.executable, [sys.executable, "-m", "agent.humboldt", "daemon", "run"])
