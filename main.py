from astrbot.api.event import filter, AstrMessageEvent, MessageEventResult
from astrbot.api.star import Context, Star, register

@register("demo_plugin", "YourName", "一个简单的示例插件", "1.0.0")
class DemoPlugin(Star):
    def __init__(self, context: Context):
        super().__init__(context)

    @filter.command("hello")
    async def hello(self, event: AstrMessageEvent):
        '''简单的问候指令'''
        user_name = event.get_sender_name()
        yield event.plain_result(f"Hello, {user_name}!")

    @filter.command("get_group_id")
    async def get_group_id(self, event: AstrMessageEvent):
        '''获取当前群聊的ID'''
        group_id = event.get_group_id()
        if group_id:
            yield event.plain_result(f"当前群聊的ID是: {group_id}")
        else:
            yield event.plain_result("这不是一个群聊消息，无法获取群聊ID。")