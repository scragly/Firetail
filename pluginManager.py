from plugins import *


async def message_plugin(client, logger, config, message):
    for plugin in config.messageplugins:\
        await plugin.run(client, message)


async def tick_plugin(client, logger, config, message):
    for plugin in config.messageplugins:
        await plugin.run(client, message)