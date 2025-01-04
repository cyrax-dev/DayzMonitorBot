import a2s
import asyncio

from typing import Optional, Dict, Any

from disnake.ext import commands
from disnake import Activity, ActivityType
from crxsnake import restart

from src.utils import log


class DiscordBot(commands.InteractionBot):

    def __init__(self, server_dict: Dict[str, Any]):
        super().__init__()
        self.server_dict = server_dict

    def get_time_emoji(self, keywords: str) -> str:
        try:
            time_str = keywords.split(",")[-1].strip()
            return "🌕" if "05:00" <= time_str < "20:00" else "🌑"
        except (IndexError, ValueError):
            return "🕑"

    async def on_ready(self) -> None:
        log.info(f"[BOT] {self.server_dict['name']} started")
        await self.update_status(self)

    async def get_server_info(self) -> Optional[a2s.SourceInfo]:
        try:
            return await a2s.ainfo((self.server_dict["ip"], self.server_dict["port"]))
        except Exception:
            return False

    async def update_status(self, bot: commands.Bot) -> None:
        try:
            while True:
                server_info = await self.get_server_info()
                if server_info:

                    status = self.server_dict["status_online"].format(
                        player = server_info.player_count,
                        slot = server_info.max_players,
                        time = server_info.keywords.split(",")[-1],
                        emoji = self.get_time_emoji(server_info.keywords)
                    )
                    log.info(f"[BOT] {self.server_dict['name']} - {status}")
                else:
                    status = self.server_dict["status_offline"]
                    log.info(f"[BOT] {self.server_dict['name']} - {status}")

                await bot.change_presence(activity=Activity(type=ActivityType.custom, name="-", state=status))
                await asyncio.sleep(60)

        except Exception as e:
            log.error(f"[BOT] An error occurred during status updates {self.server_dict['name']}\n╰─> Error: {e}")
            await asyncio.sleep(15)
            restart()
