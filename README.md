# 🚀 超级Python模拟系统 v2.0

一个功能全面的Python命令行模拟系统，包含文件操作、系统监控、网络工具、文本处理、压缩工具、安全工具和小游戏等功能。

## ✨ 主要功能

### 📁 文件操作
- `dir`, `ls` - 列出目录内容
- `copy`, `cp` - 复制文件或目录
- `move`, `mv` - 移动文件或目录
- `del`, `rm` - 删除文件或目录
- `type`, `cat` - 显示文件内容
- `mkdir` - 创建目录
- `rmdir` - 删除空目录
- `cd` - 切换目录
- `pwd` - 显示当前目录
- `touch` - 创建空文件
- `tree` - 显示目录树
- `size` - 显示文件大小

### 💻 系统信息
- `sysinfo` - 显示系统信息
- `ps` - 显示进程列表
- `top` - 实时系统监控
- `disk` - 显示磁盘信息
- `memory` - 显示内存信息
- `network` - 显示网络信息

### 🌐 网络工具
- `ping` - ping主机
- `netstat` - 显示网络连接
- `ipconfig` - 显示网络配置
- `browser` - 打开浏览器访问网址
- `download` - 下载文件

### 📝 文本处理
- `find` - 查找文件
- `grep` - 搜索文本
- `sort` - 排序文件内容
- `uniq` - 去除重复行
- `head` - 显示文件开头
- `tail` - 显示文件结尾
- `wc` - 统计文件行数

### 📦 压缩工具
- `zip` - 创建ZIP压缩包
- `unzip` - 解压ZIP文件
- `tar` - 创建TAR压缩包
- `untar` - 解压TAR文件
- `backup` - 备份文件

### 🔒 安全工具
- `hash` - 计算文件哈希值
- `md5` - 计算MD5值
- `sha1` - 计算SHA1值
- `sha256` - 计算SHA256值
- `encrypt` - 加密文件
- `decrypt` - 解密文件

### 🎮 小游戏
- `snake` - 贪吃蛇游戏
- `tetris` - 俄罗斯方块
- `guess` - 猜数字游戏
- `tictactoe` - 井字棋
- `hangman` - 猜词游戏

### 🛠️ 其他工具
- `calc` - 简单计算器
- `random` - 生成随机数
- `date` - 显示当前日期
- `time` - 显示当前时间
- `echo` - 显示文本
- `history` - 显示命令历史
- `profile` - 显示用户资料
- `level` - 显示等级信息
- `games` - 显示游戏列表
- `alias` - 设置命令别名
- `unalias` - 删除命令别名
- `cls`, `clear` - 清屏
- `help` - 显示帮助
- `exit`, `quit` - 退出系统

## 🚀 安装和运行

### Windows用户 (推荐)
1. **双击运行安装**: `install.bat`
2. **双击运行测试**: `test.bat` (可选)
3. **双击运行系统**: `start.bat`

### 手动安装
1. **安装依赖**:
   ```bash
   pip install -r requirements.txt
   ```
   或者运行:
   ```bash
   python install.py
   ```

2. **运行系统**:
   ```bash
   python start.py
   ```
   或者:
   ```bash
   python main.py
   ```

## 📋 使用示例

```bash
# 查看当前目录
dir

# 创建新目录
mkdir myfolder

# 切换到新目录
cd myfolder

# 创建文件
touch test.txt

# 显示系统信息
sysinfo

# 打开浏览器
browser google.com

# 下载文件
download https://example.com/file.txt myfile.txt

# 开始游戏
snake

# 查看帮助
help
```

## 🎯 特色功能

### 用户等级系统
- 使用命令获得经验值
- 玩游戏获得额外经验
- 等级提升解锁更多功能

### 游戏系统
- 5种经典小游戏
- 游戏胜利获得经验值
- 支持键盘控制

### 网络功能
- 内置浏览器功能
- 文件下载功能
- 网络状态监控

### 安全功能
- 多种哈希算法
- 文件加密解密
- 安全工具集合

## 🔧 系统要求

- Python 3.6+
- Windows/Linux/macOS
- 依赖包：psutil, requests

## 📝 注意事项

1. 某些游戏功能仅在Windows系统上可用
2. 网络功能需要网络连接
3. 系统会自动保存用户数据到user_data.json文件

## 🎮 游戏说明

### 贪吃蛇 (snake)
- 使用WASD键控制
- 吃到食物增加分数
- 撞墙或撞到自己游戏结束

### 俄罗斯方块 (tetris)
- 使用A/D移动，S加速下落，W旋转
- 消除行获得分数
- 方块堆到顶部游戏结束

### 猜数字 (guess)
- 猜1-100之间的数字
- 有10次机会
- 根据猜测次数获得经验

### 井字棋 (tictactoe)
- 你是X，电脑是O
- 输入1-9选择位置
- 三子连线获胜

### 猜词游戏 (hangman)
- 猜英语单词
- 有6次错误机会
- 根据剩余机会获得经验

## 📞 技术支持

如有问题或建议，请查看帮助信息或联系开发者。

---

**享受使用超级Python模拟系统！** 🎉 