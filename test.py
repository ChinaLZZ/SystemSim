#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
系统功能测试脚本
"""

import sys
import os

def test_imports():
    """测试导入"""
    print("🔍 测试模块导入...")
    
    try:
        import psutil
        print("✅ psutil 导入成功")
    except ImportError as e:
        print(f"❌ psutil 导入失败: {e}")
        return False
    
    try:
        import requests
        print("✅ requests 导入成功")
    except ImportError as e:
        print(f"❌ requests 导入失败: {e}")
        return False
    
    try:
        import webbrowser
        print("✅ webbrowser 导入成功")
    except ImportError as e:
        print(f"❌ webbrowser 导入失败: {e}")
        return False
    
    return True

def test_basic_functions():
    """测试基本功能"""
    print("\n🔍 测试基本功能...")
    
    try:
        from main import SuperCommandLineSystem
        system = SuperCommandLineSystem()
        print("✅ 系统类创建成功")
        
        # 测试一些基本方法
        system.cmd_date([])
        system.cmd_time([])
        system.cmd_echo(["Hello", "World"])
        
        print("✅ 基本功能测试通过")
        return True
    except Exception as e:
        print(f"❌ 基本功能测试失败: {e}")
        return False

def test_file_operations():
    """测试文件操作"""
    print("\n🔍 测试文件操作...")
    
    try:
        from main import SuperCommandLineSystem
        system = SuperCommandLineSystem()
        
        # 测试创建文件
        test_file = "test_file.txt"
        with open(test_file, 'w') as f:
            f.write("测试文件内容")
        
        # 测试文件操作命令
        system.cmd_type([test_file])
        
        # 清理测试文件
        if os.path.exists(test_file):
            os.remove(test_file)
        
        print("✅ 文件操作测试通过")
        return True
    except Exception as e:
        print(f"❌ 文件操作测试失败: {e}")
        return False

def main():
    """主测试函数"""
    print("🚀 超级Python模拟系统 - 功能测试")
    print("=" * 50)
    
    tests = [
        ("模块导入", test_imports),
        ("基本功能", test_basic_functions),
        ("文件操作", test_file_operations)
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        print(f"\n📋 测试: {test_name}")
        if test_func():
            passed += 1
            print(f"✅ {test_name} 测试通过")
        else:
            print(f"❌ {test_name} 测试失败")
    
    print("\n" + "=" * 50)
    print(f"📊 测试结果: {passed}/{total} 通过")
    
    if passed == total:
        print("🎉 所有测试通过! 系统可以正常运行")
        print("运行 python start.py 启动系统")
    else:
        print("❌ 部分测试失败，请检查依赖包或代码")
    
    input("\n按回车键退出...")

if __name__ == "__main__":
    main() 