#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
快速启动脚本 - 避免requests依赖问题
"""

import sys
import os

def check_basic_dependencies():
    """检查基本依赖"""
    missing = []
    
    try:
        import psutil
        print("✅ psutil 已安装")
    except ImportError:
        missing.append("psutil")
        print("❌ psutil 未安装")
    
    # 可选依赖
    try:
        import requests
        print("✅ requests 已安装")
    except ImportError:
        print("⚠️  requests 未安装 (网络功能将不可用)")
    
    return missing

def install_missing_packages(missing):
    """安装缺失的包"""
    if not missing:
        return True
    
    print(f"\n📦 正在安装缺失的包: {', '.join(missing)}")
    
    for package in missing:
        try:
            import subprocess
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
            print(f"✅ {package} 安装成功")
        except Exception as e:
            print(f"❌ {package} 安装失败: {e}")
            return False
    
    return True

def main():
    """主函数"""
    print("🚀 超级Python模拟系统 - 快速启动")
    print("=" * 50)
    
    # 检查依赖
    missing = check_basic_dependencies()
    
    if missing:
        print(f"\n📦 需要安装: {', '.join(missing)}")
        if not install_missing_packages(missing):
            print("❌ 依赖安装失败，请手动安装")
            input("按回车键退出...")
            return
    
    print("\n✅ 依赖检查完成")
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