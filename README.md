# 公主连接 Princess Connect Re:Dive 自建农场脚本

![build-pass](https://img.shields.io/badge/build-pass-green)

![test-fail](https://img.shields.io/badge/test-pass-green)

本项目基于[uiautomator](https://github.com/xiaocong/uiautomator)和[opencv2](https://opencv.org/)

可为游玩bilibili版本公主连接的用户提供自动登陆农场号，完成：每日扫荡、进入地下城借用支援角色并退出、领取任务奖励、领取礼物的任务。

## TODO

- [x] 扫荡关卡
- [x] 挑战地下城 
- [x] 领取任务奖励
- [x] 领取礼物
- [x] 切换账号

## Usage

使用前请打开**支持adb的安卓模拟器**（推荐使用[雷电模拟器](https://www.ldmnq.com/)），并**开启Bilibili版本**公主连接游戏，保持在标题界面，即如下图所示的界面：

![titlePage](./image/titlePage.png)

在当前目录（包含`src`等文件夹）新建`account`文件夹，在`account`文件夹中新建`account.json`文件，并在其中按照如下格式填写农场账号有关信息：

```json
[{
        "name": ...,
        "password": ...,
        "mail": ...,
        "mail_password": ...,
        "type": ...
    },
    ...
]
```

其中信息填写如下：

- name：（必要）填写登陆时的用户名
- password：（必要）填写登陆时的密码
- mail：填写绑定的邮箱
- mail_password：填写绑定邮箱的密码
- type：是否为行会会长（分类"master"和"member"类型）

除必要信息外，其他信息在现阶段脚本中无用，可能在后续开发中用到

```shell
cd src/
python main.py
```

为保证按键正确，可**根据自己的情况适当修改脚本**或者**严格按照以下的要求配置**：

1. 切换账号时必定先出现是否一键登录bilibili账号的通知（可自行更改`src/gameOp.py/game/login(self, account)`）
2. 登入后无出现新角色提示
3. 非首次进入简单地下城等区域（无首次进入剧情、无首次进入提示）
4. 进入主线故事时，未经移动的界面已存在三星通关并可以扫荡的关卡
5. 地下城需要租借的角色显示在支援界面的首位
6. 租借角色会出现租借确认提示
7. **当前租借角色能够在简单地下城第一层的战斗中存活至少25秒，同时在该过程中不能赢得战斗**（建议使用t作为支援角色，并开启一倍速）

## Issues

本项目仍存在如下问题，会导致脚本运行无法达到预期结果：

### `adb-server`运行时间较长时，容易出现卡顿

已添加`adb-server`重连机制：

1. 在完成主线扫荡后，进入地下城前重连
2. 在切换账号时重连

### 电脑配置不够时，模拟器出现卡顿

已添加在CPU占用率高于`80%`时，自动断开`adb-server`并等待`30`秒后重连机制

### 当网络连接不稳定时，按键时间间隔有可能长于加载时间

请尽量保证网络流畅，页面的加载时间小于5秒
