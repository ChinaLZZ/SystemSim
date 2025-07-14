@echo off
chcp 65001 >nul
echo  超级Python模拟系统
echo ================================
echo.

REM 检查Python
python --version >nul 2>&1
if errorlevel 1 (
    echo  Python未安装
    pause
    exit /b 1
)

echo  Python已安装
echo.

REM 尝试运行快速启动脚本
python quick_start.py

pause 