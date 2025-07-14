# 🔧 问题解决指南

## 常见问题

### 1. "无法从源码解析导入 requests"
**问题**: 缺少requests库
**解决**: 
```bash
pip install requests
```
或者运行 `install.bat`

### 2. "无法从源码解析导入 psutil"
**问题**: 缺少psutil库
**解决**: 
```bash
pip install psutil
```
或者运行 `install.bat`

### 3. "'c:\Program' 不是内部或外部命令"
**问题**: 路径中包含空格
**解决**: 
- 将项目移动到没有空格的路径
- 或者使用引号包围路径

### 4. "无法访问 tuple 类的 ip 属性"
**问题**: psutil版本兼容性问题
**解决**: 
- 更新psutil: `pip install --upgrade psutil`
- 或者使用较新版本的Python

### 5. 游戏无法运行
**问题**: 某些游戏需要Windows系统
**解决**: 
- 贪吃蛇和俄罗斯方块仅在Windows上可用
- 其他游戏在所有系统上都可用

### 6. 网络功能无法使用
**问题**: 网络连接或权限问题
**解决**: 
- 检查网络连接
- 以管理员身份运行
- 检查防火墙设置

## 安装步骤

### 方法1: 自动安装 (推荐)
1. 双击 `install.bat`
2. 等待安装完成
3. 双击 `start.bat` 启动系统

### 方法2: 手动安装
```bash
# 安装依赖
pip install psutil requests

# 运行系统
python start.py
```

### 方法3: 使用requirements.txt
```bash
pip install -r requirements.txt
python main.py
```

## 测试系统

运行测试来检查系统是否正常工作:
```bash
python test.py
```
或者双击 `test.bat`

## 系统要求

- Python 3.6+
- Windows/Linux/macOS
- 网络连接 (用于下载和浏览器功能)

## 获取帮助

如果问题仍然存在:
1. 运行 `test.py` 查看具体错误
2. 检查Python版本: `python --version`
3. 检查pip版本: `pip --version`
4. 尝试重新安装依赖包

## 联系支持

如果以上方法都无法解决问题，请提供:
- 操作系统版本
- Python版本
- 错误信息
- 运行 `test.py` 的输出结果 