import asyncio
from typing import Dict, Any

from disnake import errors
from crxsnake import read_json

from src.main import DiscordBot
from src.utils import log


async def start_bot(server_dict: Dict[str, Any]) -> None:
    try:
        bot = DiscordBot(server_dict)
        await bot.start(server_dict["token"])

    except errors.LoginFailure:
        log.error(f"[BOT] Invalid token {server_dict["name"]}")
    except Exception as e:
        log.error(f"[BOT] A start-up error occurred {server_dict["name"]}\n╰─> Ошибка: {e}")


async def main() -> None:
    try:
        servers = await read_json("settings/servers.json")
        tasks = [
            asyncio.create_task(start_bot(server))
            for server in servers
        ]
        await asyncio.gather(*tasks)

    finally:
        input("Press Enter to close the programme...")

if __name__ == "__main__":
    asyncio.run(main())
