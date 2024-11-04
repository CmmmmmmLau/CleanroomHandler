import re

from mcdreforged.handler.impl import ForgeHandler
from typing_extensions import override

class CleanRoomHandler(ForgeHandler):
    """
    A handler for Cleanroom <https://github.com/CleanroomMC/Cleanroom>__ Minecraft servers.

    Cleanroom follows the same format as Forge but leaves an empty square bracket if there is no logger name.
    """

    @classmethod
    @override
    def get_content_parsing_formatter(cls):
        # [09:47:06] [Server thread/INFO] [minecraft/DedicatedServer]: Done (4.816s)! For help, type "help" or "?"
        # [09:47:16] [Server thread/INFO] [minecraft/PlayerList]: Cmmmmmm[/127.0.0.1:9819] logged in with entity id 173 at ([world]-79.5, 85.0, -156.5)
        # [09:47:24] [Async Chat Thread - #0/INFO] []: <Cmmmmmm> hi
        # [09:47:25] [Async Chat Thread - #0/INFO] []: <Cmmmmmm> test
        # [09:47:28] [Server thread/INFO] [minecraft/NetHandlerPlayServer]: Cmmmmmm lost connection: Disconnected
        return re.compile(
            r'\[(?P<hour>\d+):(?P<min>\d+):(?P<sec>\d+)]'  # Time
            r' \[(?P<thread>[^[]+)/(?P<logging>[^[]+)]'    # Thread name and log level
            r'( \[(.*)?])'                                 # Logger name, could be a empty square bracket
            r': (?P<content>.*)'                           # Output Content
        )