@echo off
chcp 65001 >nul
echo  超级Python模拟系统
echo ================================
echo.

REM 检查Python是否安装
python --version >nul 2>&1
if errorlevel 1 (
    echo  Python未安装或未添加到PATH
    echo 请先安装Python 3.6+
    pause
    exit /b 1
)

echo  Python已安装
echo.

REM 运行启动脚本
python start.py

pause 