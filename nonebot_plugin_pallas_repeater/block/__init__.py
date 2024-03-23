import os
import threading
import time
from typing import List, Union

from nonebot import get_bots
from nonebot import on_message, on_notice
from nonebot.adapters import Bot
from nonebot.adapters.onebot.v11 import GroupIncreaseNoticeEvent, GroupMessageEvent, PokeNotifyEvent, permission
from nonebot.exception import IgnoredException
from nonebot.message import event_preprocessor
from nonebot.rule import Rule
from nonebot.typing import T_State

from ..config import BotConfig, plugin_config


class AccountManager:
    def __init__(self, accounts_dir: str) -> None:
        self.accounts_dir = accounts_dir
        self.accounts: List[int] = []
        self.refresh_time = 0
        self.refresh_lock = threading.Lock()

    def refresh_accounts(self) -> None:
        if time.time() - self.refresh_time < 60 and self.accounts:
            return

        with self.refresh_lock:
            self.refresh_time = time.time()
            if os.path.exists(self.accounts_dir):
                go_cqhttp_plugin_accounts: List[int] = [
                    int(d) for d in os.listdir(self.accounts_dir) if d.isnumeric()
                ]
            onebot_accounts: List[int] = [
                int(self_id) for self_id, bot in get_bots().items() if self_id.isnumeric() and bot.type == 'OneBot V11'
            ]
            self.accounts = list(set(go_cqhttp_plugin_accounts + onebot_accounts))

    async def is_other_bot(self, bot: Bot, event: GroupMessageEvent, state: T_State) -> bool:
        self.refresh_accounts()
        return event.user_id in self.accounts

    async def is_sleep(self, bot: Bot, event: Union[GroupMessageEvent, GroupIncreaseNoticeEvent, PokeNotifyEvent],
                       state: T_State) -> bool:
        if not event.group_id:
            return False
        return BotConfig(event.self_id, event.group_id).is_sleep()


account_manager = AccountManager('accounts')

other_bot_msg = on_message(
    priority=1,
    block=True,
    rule=Rule(account_manager.is_other_bot),
    permission=permission.GROUP
)

any_msg = on_message(
    priority=4,
    block=True,
    rule=Rule(account_manager.is_sleep),
    permission=permission.GROUP
)

any_notice = on_notice(
    priority=4,
    block=True,
    rule=Rule(account_manager.is_sleep)
)


@event_preprocessor
async def _(event: GroupMessageEvent):
    if event.user_id in plugin_config.blacklist:
        raise IgnoredException(reason=f'黑名单用户{event.user_id}')
