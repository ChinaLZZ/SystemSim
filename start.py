#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
启动脚本 - 超级Python模拟系统
"""

import sys
import os

def check_dependencies():
    """检查依赖包"""
    missing_packages = []
    
    try:
        import psutil
        print("✅ psutil 已安装")
    except ImportError:
        missing_packages.append("psutil")
        print("❌ psutil 未安装")
    
    try:
        import requests
        print("✅ requests 已安装")
    except ImportError:
        missing_packages.append("requests")
        print("❌ requests 未安装")
    
    return missing_packages

def main():
    """主函数"""
    print("🚀 超级Python模拟系统 - 启动检查")
    print("=" * 50)
    
    # 检查依赖
    missing = check_dependencies()
    
    if missing:
        print(f"\n❌ 缺少依赖包: {', '.join(missing)}")
        print("请运行以下命令安装依赖:")
        print("python install.py")
        print("或者手动安装:")
        for package in missing:
            print(f"pip install {package}")
        input("\n按回车键退出...")
        return
    
    print("\n✅ 所有依赖包已安装")
    print("正在启动系统...")
    print("=" * 50)
    
    try:
        # 导入并运行主系统
        from main import SuperCommandLineSystem
        system = SuperCommandLineSystem()
        system.run()
    except KeyboardInterrupt:
        print("\n👋 程序已退出")
    except Exception as e:
        print(f"❌ 启动失败: {e}")
        print("请检查代码或依赖包是否正确安装")

if __name__ == "__main__":
    main() 