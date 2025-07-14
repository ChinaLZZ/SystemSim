#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
简单依赖安装脚本
"""

import subprocess
import sys

def install_package(package):
    """安装单个包"""
    try:
        print(f"📦 正在安装 {package}...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        print(f"✅ {package} 安装成功!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {package} 安装失败: {e}")
        return False

def main():
    """主函数"""
    print("🚀 超级Python模拟系统 - 依赖安装")
    print("=" * 50)
    
    # 需要安装的包
    packages = ["psutil", "requests"]
    
    success_count = 0
    for package in packages:
        if install_package(package):
            success_count += 1
    
    print("\n" + "=" * 50)
    if success_count == len(packages):
        print("🎉 所有依赖包安装完成!")
        print("现在可以运行 python main.py 启动系统")
    else:
        print(f"⚠️  部分依赖包安装失败 ({success_count}/{len(packages)})")
        print("请检查网络连接或手动安装失败的包")
    
    input("\n按回车键退出...")

if __name__ == "__main__":
    main() 