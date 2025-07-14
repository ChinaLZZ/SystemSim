#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
依赖包安装脚本
"""

import subprocess
import sys
import importlib

def check_and_install_package(package_name):
    """检查并安装包"""
    try:
        importlib.import_module(package_name)
        print(f"✅ {package_name} 已安装")
        return True
    except ImportError:
        print(f"📦 正在安装 {package_name}...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])
            print(f"✅ {package_name} 安装成功")
            return True
        except subprocess.CalledProcessError:
            print(f"❌ {package_name} 安装失败")
            return False

def main():
    """主函数"""
    print("🚀 超级Python模拟系统 - 依赖包安装")
    print("=" * 50)
    
    # 需要安装的包
    packages = [
        "psutil",
        "requests"
    ]
    
    all_success = True
    for package in packages:
        if not check_and_install_package(package):
            all_success = False
    
    print("\n" + "=" * 50)
    if all_success:
        print("🎉 所有依赖包安装完成!")
        print("现在可以运行 python main.py 启动系统")
    else:
        print("❌ 部分依赖包安装失败")
        print("请手动安装失败的包，或检查网络连接")
    
    input("\n按回车键退出...")

if __name__ == "__main__":
    main() 