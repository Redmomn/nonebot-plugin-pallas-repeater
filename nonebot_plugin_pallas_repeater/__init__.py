from nonebot.plugin import PluginMetadata
from nonebot.log import logger
from . import block, drink
from .config import PluginConfig, plugin_config

if plugin_config.is_nb_store_testing:
    try:
        from . import repeater, take_name
    except:
        logger.warning('repeater, take_name 插件未加载')
        pass
else:
    from . import repeater, take_name

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
