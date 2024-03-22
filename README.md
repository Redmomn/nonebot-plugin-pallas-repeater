<p align="center">
  <a href="https://v2.nonebot.dev/"><img src="https://v2.nonebot.dev/logo.png" width="200" height="200" alt="nonebot"></a>
</p>

<div align="center">

# nonebot-plugin-pallas-repeater

✨ 复读鸡 ✨

<p align="center">
  <a href="https://github.com/Redmomn/nonebot-plugin-pallas-repeater/blob/master/LICENSE">
    <img src="https://img.shields.io/github/license/Redmomn/nonebot-plugin-pallas-repeater.svg" alt="license">
  </a>
  <img src="https://img.shields.io/badge/python-3.8+-blue.svg" alt="Python">
  <a href="https://pypi.org/project/nonebot-plugin-pallas-repeater">
    <img src="https://badgen.net/pypi/v/nonebot-plugin-pallas-repeater" alt="pypi">
  </a>
</p>

</div>

## 📖 介绍

复读鸡，从[PallasBot](https://github.com/MistEO/Pallas-Bot)单独拆分出来的插件版本  
已兼容pydantic v1&v2

## 💿 安装

<details open>
<summary>nb-cli</summary>

    nb plugin install nonebot-plugin-pallas-repeater

</details>

<details open>
<summary>pip</summary>

    pip install nonebot_plugin_pallas_repeater

</details>

## ⚙️ 配置

```text
# 黑名单，会导致所有插件都不能响应该用户的命令
BLACKLIST=[]
# mongodb 相关配置，如无特殊需求，保持注释即可
# 使用 docker-compose 部署时，请将MONGO_HOST设置为 mongodb 容器 的 service 名称，如：MONGO_HOST=mongodb

MONGO_HOST=127.0.0.1
MONGO_PORT=27017
MONGO_USER=
MONGO_PASSWORD=

# 复读机功能相关参数，推荐保持注释

# answer 相关阈值，值越大，牛牛废话越少；越小，牛牛废话越多
ANSWER_THRESHOLD = 3
# answer 阈值权重
ANSWER_THRESHOLD_WEIGHTS = [7, 23, 70]
# 上下文联想，记录多少个关键词（每个群）
TOPICS_SIZE = 16
# 上下文命中后，额外的权重系数
TOPICS_IMPORTANCE = 10000
# N 个群有相同的回复，就跨群作为全局回复
CROSS_GROUP_THRESHOLD = 2
# 复读的阈值，群里连续多少次有相同的发言，就复读
REPEAT_THRESHOLD = 3
# 主动发言的阈值，越小废话越多
SPEAK_THRESHOLD = 5
# 说过的话，接下来多少次不再说
DUPLICATE_REPLY = 10
# 按逗号分割回复语的概率
SPLIT_PROBABILITY = 0.5
# 连续主动说话的概率
SPEAK_CONTINUOUSLY_PROBABILITY = 0.5
# 主动说话加上随机戳一戳群友的概率
SPEAK_POKE_PROBABILITY = 0.6
# 连续主动说话最多几句话
SPEAK_CONTINUOUSLY_MAX_LEN = 2
# 每隔多久进行一次持久化（秒）
SAVE_TIME_THRESHOLD = 3600
# 单个群超过多少条聊天记录就进行一次持久化，与时间是或的关系
SAVE_COUNT_THRESHOLD = 1000
# 保存时，给内存中保留的大小
SAVE_RESERVED_SIZE = 100

# tts 功能相关配置

# 声码器，可选值：pwgan_aishell3、wavernn_csmsc
TTS_VOCODER=pwgan_aishell3
```

### 关于分词

默认安装`jieba`， 加群较多、需要处理消息量大的用户可以自行安装`jieba-fast`，以提升分词速度

插件会优先尝试导入`jieba-fast`库，如果导入失败则使用`jieba`库，无需手动修改代码

```shell
pip3 install jieba_fast
```

Windows下安装需要msvc编译器支持
Linux下安装需要build-essential

## 🎉 使用

### 牛牛有什么功能？

牛牛的功能就是废话和复读。牛牛几乎所有的发言都是从群聊记录中学习而来的，并非作者硬编码写入的。群友们平时怎么聊，牛牛就会怎么回，可以认为是高级版的复读机

### 那为什么牛牛说了一些群里从来没说过的话？

牛牛有跨群功能，若超过 N 个群都有类似的发言，就会作为全局发言，在任何群都生效

### 你说牛牛没有功能，为什么有时候查询信息、或者一些其它指令，牛牛会回复？

从别的机器人（可能是其他群）那里学来的

~~你这机器人功能不错呀，现在牛牛也会了！~~

### 有时候没人说话，牛牛自己突然蹦出来几句话

哈，是主动发言功能！内容同样从群聊里学来的！

### 怎么教牛牛说话呢？

正常聊天即可，牛牛会自动学。

如果想强行教的话，可以这样：

```text
—— 牛牛你好
—— 你好呀
—— 牛牛你好
—— 你好呀
—— 牛牛你好
—— 你好呀
```

如此重复 3 次以上，下一次再发送 “牛牛你好”，牛牛即会回复 “你好呀”

### 牛牛说了一些不合适的话，要怎么删除？

群管理员 **回复** 牛牛说的那句话 “不可以” 或直接撤回对应的消息即可，同样的若超过 N 个群都禁止了这句话，就会作为全局禁止，在任何群都不发

### 牛牛的一些其他小功能

- `牛牛喝酒` 进入狂暴醉酒状态（bushi，废话会特别多，喝醉后不会响应用户命令（优先级为4以下的）
- 随机修改自己的群名片为近期发言的人，夺舍！

## 💡 感谢

原项目[Pallas-Bot](https://github.com/MistEO/Pallas-Bot)(高性能废物牛牛子)  
本项目几乎所有代码都来源于原项目（包括README）
