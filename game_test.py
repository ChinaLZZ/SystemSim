#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
游戏功能测试脚本
"""

def test_game_commands():
    """测试游戏命令"""
    print("🎮 游戏命令测试")
    print("=" * 30)
    
    try:
        from main import SuperCommandLineSystem
        system = SuperCommandLineSystem()
        
        # 测试游戏命令是否存在
        game_commands = ['snake', 'tetris', 'guess', 'tictactoe', 'hangman']
        
        for cmd in game_commands:
            if hasattr(system, f'cmd_{cmd}'):
                print(f"✅ {cmd} 命令存在")
            else:
                print(f"❌ {cmd} 命令不存在")
        
        # 测试games命令
        print("\n📋 测试 games 命令:")
        system.cmd_games([])
        
        print("\n🎯 测试 guess 命令 (简单游戏):")
        print("注意: 这个测试会启动猜数字游戏")
        response = input("是否要测试猜数字游戏? (y/n): ")
        if response.lower() == 'y':
            system.cmd_guess([])
        
    except Exception as e:
        print(f"❌ 测试失败: {e}")

def main():
    """主函数"""
    print("🚀 游戏功能测试")
    print("=" * 30)
    
    test_game_commands()
    
    print("\n" + "=" * 30)
    print("测试完成!")
    print("如果所有命令都显示为存在，那么游戏功能应该正常工作")
    print("您可以在主系统中使用以下命令启动游戏:")
    print("- snake (贪吃蛇)")
    print("- tetris (俄罗斯方块)")
    print("- guess (猜数字)")
    print("- tictactoe (井字棋)")
    print("- hangman (猜词游戏)")
    print("- games (查看游戏列表)")
    
    input("\n按回车键退出...")

if __name__ == "__main__":
    main() 