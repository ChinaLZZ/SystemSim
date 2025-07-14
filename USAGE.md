# 🚀 超级Python模拟系统 - 使用说明

## 快速启动

### 方法1: 双击启动 (推荐)
双击 `run.bat` 文件

### 方法2: 命令行启动
```bash
python quick_start.py
```

### 方法3: 直接启动
```bash
python main.py
```

## 游戏命令

启动系统后，输入以下命令开始游戏：

- `snake` - 贪吃蛇游戏
- `tetris` - 俄罗斯方块
- `guess` - 猜数字游戏
- `tictactoe` - 井字棋
- `hangman` - 猜词游戏
- `games` - 查看游戏列表

## 其他常用命令

- `help` - 查看所有命令
- `dir` - 列出文件
- `sysinfo` - 系统信息
- `calc` - 计算器
- `date` - 显示日期
- `time` - 显示时间

## 安装依赖

如果遇到依赖问题，运行：
```bash
python simple_install.py
```

## 测试游戏功能

运行游戏测试：
```bash
python game_test.py
```

## 问题解决

如果游戏命令无法启动：
1. 确保已安装 psutil: `pip install psutil`
2. 运行测试脚本检查: `python game_test.py`
3. 查看错误信息并解决

## 游戏说明

### 贪吃蛇 (snake)
- 使用 WASD 键控制
- 按 Q 退出游戏
- 吃到食物增加分数

### 俄罗斯方块 (tetris)
- 使用 A/D 移动，S 加速，W 旋转
- 按 Q 退出游戏
- 消除行获得分数

### 猜数字 (guess)
- 猜1-100之间的数字
- 有10次机会
- 根据猜测次数获得经验

### 井字棋 (tictactoe)
- 你是 X，电脑是 O
- 输入1-9选择位置
- 三子连线获胜

### 猜词游戏 (hangman)
- 猜英语单词
- 有6次错误机会
- 根据剩余机会获得经验 