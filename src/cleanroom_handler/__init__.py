from mcdreforged.plugin.si.plugin_server_interface import PluginServerInterface
from .cleanroom_handler import  CleanRoomHandler

def on_load(server:PluginServerInterface, prev_module):
    server.logger.info("-------------------------")
    server.logger.info("Loading Cleanroom handler")
    server.logger.info("-------------------------")
    server.register_server_handler(CleanRoomHandler())