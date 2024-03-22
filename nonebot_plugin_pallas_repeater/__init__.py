from nonebot.plugin import PluginMetadata

from . import block, drink, repeater, take_name
from .config import PluginConfig

__plugin_meta__ = PluginMetadata(
    name="nonebot-plugin-pallas-repeater",
    description="复读鸡",
    usage="",
    type="application",
    homepage="https://github.com/Redmomn/nonebot-plugin-pallas-repeater",
    supported_adapters={"~onebot.v11"},
    config=PluginConfig,
    extra={"author": "Redmomn"}
)

__all__ = ['block', 'drink', 'repeater', 'take_name']
