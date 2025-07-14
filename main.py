#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
超级Python模拟系统 - PartA
功能包括：基础框架、文件操作、系统信息、进程管理、网络工具、文本处理等
"""

import os
import sys
import shutil
import platform
import psutil
import datetime
import json
import hashlib
import zipfile
import tarfile
import subprocess
import threading
import time
import random
import string
import urllib.request
import urllib.parse
import webbrowser
try:
    import requests
    REQUESTS_AVAILABLE = True
except ImportError:
    REQUESTS_AVAILABLE = False
from pathlib import Path
from typing import List, Dict, Any, Optional

# ==================== PartA: 基础框架和核心功能 ====================

class SuperCommandLineSystem:
    def __init__(self):
        self.current_dir = os.getcwd()
        self.history = []
        self.aliases = {
            'ls': 'dir',
            'll': 'dir -l',
            'cp': 'copy',
            'mv': 'move',
            'rm': 'del',
            'cat': 'type',
            'clear': 'cls'
        }
        self.running = True
        self.prompt = ">>> "
        self.user_data = {
            'username': 'User',
            'level': 1,
            'experience': 0,
            'games_won': 0,
            'files_created': 0,
            'commands_used': 0
        }
        self.load_user_data()
        
    def load_user_data(self):
        """加载用户数据"""
        try:
            if os.path.exists('user_data.json'):
                with open('user_data.json', 'r', encoding='utf-8') as f:
                    self.user_data.update(json.load(f))
        except Exception:
            pass
    
    def save_user_data(self):
        """保存用户数据"""
        try:
            with open('user_data.json', 'w', encoding='utf-8') as f:
                json.dump(self.user_data, f, ensure_ascii=False, indent=2)
        except Exception:
            pass
        
    def run(self):
        """启动命令行系统"""
        self.print_banner()
        
        while self.running:
            try:
                command = input(f"{self.current_dir} {self.prompt}").strip()
                if command:
                    self.history.append(command)
                    self.user_data['commands_used'] += 1
                    self.execute_command(command)
            except KeyboardInterrupt:
                print("\n使用 'exit' 或 'quit' 退出系统")
            except EOFError:
                break
            except Exception as e:
                print(f"错误: {e}")
        
        self.save_user_data()
    
    def print_banner(self):
        """打印系统横幅"""
        banner = """
╔══════════════════════════════════════════════════════════════════════════════╗
                         🚀 超级Python模拟系统 v2.0 🚀                          
                                                                              
   用户: {username:<15} 等级: {level:<3} 经验: {exp:<6} 命令数: {cmd:<6}        
                                                                              
   📁 文件操作: dir, copy, move, del, type, mkdir, rmdir, tree, size         
   💻 系统信息: sysinfo, ps, top, disk, memory, network                      
   🌐 网络工具: ping, netstat, ipconfig, browser, download                   
   📝 文本处理: find, grep, sort, uniq, head, tail, wc                       
   📦 压缩工具: zip, unzip, tar, untar, backup                              
   🔒 安全工具: hash, md5, sha1, sha256, encrypt, decrypt                   
   🎮 小游戏: snake, tetris, guess, tictactoe, hangman                      
   🛠️  其他工具: calc, random, date, time, echo, history, help              
                                                                               
   输入 'help' 查看详细帮助  |  输入 'games' 查看游戏列表                     
╚══════════════════════════════════════════════════════════════════════════════╝
        """.format(
            username=self.user_data['username'],
            level=self.user_data['level'],
            exp=self.user_data['experience'],
            cmd=self.user_data['commands_used']
        )
        print(banner)
    
    def execute_command(self, command: str):
        """执行命令"""
        parts = command.split()
        if not parts:
            return
            
        cmd = parts[0].lower()
        args = parts[1:] if len(parts) > 1 else []
        
        # 检查别名
        if cmd in self.aliases:
            alias_cmd = self.aliases[cmd]
            if ' ' in alias_cmd:
                alias_parts = alias_cmd.split()
                cmd = alias_parts[0]
                args = alias_parts[1:] + args
            else:
                cmd = alias_cmd
        
        # 命令映射
        commands = {
            # 文件操作
            'dir': self.cmd_dir,
            'ls': self.cmd_dir,
            'copy': self.cmd_copy,
            'cp': self.cmd_copy,
            'move': self.cmd_move,
            'mv': self.cmd_move,
            'del': self.cmd_delete,
            'rm': self.cmd_delete,
            'type': self.cmd_type,
            'cat': self.cmd_type,
            'mkdir': self.cmd_mkdir,
            'rmdir': self.cmd_rmdir,
            'cd': self.cmd_cd,
            'pwd': self.cmd_pwd,
            'cls': self.cmd_clear,
            'clear': self.cmd_clear,
            'tree': self.cmd_tree,
            'size': self.cmd_size,
            'touch': self.cmd_touch,
            
            # 系统信息
            'sysinfo': self.cmd_sysinfo,
            'ps': self.cmd_ps,
            'top': self.cmd_top,
            'disk': self.cmd_disk,
            'memory': self.cmd_memory,
            'network': self.cmd_network,
            
            # 网络工具
            'ping': self.cmd_ping,
            'netstat': self.cmd_netstat,
            'ipconfig': self.cmd_ipconfig,
            'browser': self.cmd_browser,
            'download': self.cmd_download,
            
            # 文本处理
            'find': self.cmd_find,
            'grep': self.cmd_grep,
            'sort': self.cmd_sort,
            'uniq': self.cmd_uniq,
            'head': self.cmd_head,
            'tail': self.cmd_tail,
            'wc': self.cmd_wc,
            
            # 压缩工具
            'zip': self.cmd_zip,
            'unzip': self.cmd_unzip,
            'tar': self.cmd_tar,
            'untar': self.cmd_untar,
            'backup': self.cmd_backup,
            
            # 安全工具
            'hash': self.cmd_hash,
            'md5': self.cmd_md5,
            'sha1': self.cmd_sha1,
            'sha256': self.cmd_sha256,
            'encrypt': self.cmd_encrypt,
            'decrypt': self.cmd_decrypt,
            
            # 其他工具
            'date': self.cmd_date,
            'time': self.cmd_time,
            'echo': self.cmd_echo,
            'history': self.cmd_history,
            'calc': self.cmd_calc,
            'random': self.cmd_random,
            'help': self.cmd_help,
            'exit': self.cmd_exit,
            'quit': self.cmd_exit,
            'alias': self.cmd_alias,
            'unalias': self.cmd_unalias,
            'profile': self.cmd_profile,
            'games': self.cmd_games,
            'level': self.cmd_level,
            
            # 游戏命令
            'snake': self.cmd_snake,
            'tetris': self.cmd_tetris,
            'guess': self.cmd_guess,
            'tictactoe': self.cmd_tictactoe,
            'hangman': self.cmd_hangman
        }
        
        if cmd in commands:
            try:
                commands[cmd](args)
            except Exception as e:
                print(f"命令执行错误: {e}")
        else:
            print(f"未知命令: {cmd}")
            print("输入 'help' 查看可用命令")
    
    # ==================== 文件操作命令 ====================
    
    def cmd_dir(self, args):
        """列出目录内容"""
        path = args[0] if args else "."
        full_path = os.path.join(self.current_dir, path)
        
        if not os.path.exists(full_path):
            print(f"路径不存在: {path}")
            return
        
        if os.path.isfile(full_path):
            self._print_file_info(full_path)
            return
        
        try:
            items = os.listdir(full_path)
            files = []
            dirs = []
            
            for item in items:
                item_path = os.path.join(full_path, item)
                if os.path.isdir(item_path):
                    dirs.append(item)
                else:
                    files.append(item)
            
            # 排序
            dirs.sort()
            files.sort()
            
            print(f"\n📁 目录: {os.path.abspath(full_path)}")
            print("=" * 70)
            
            if dirs:
                print("\n📁 [目录]")
                for d in dirs:
                    print(f"  📁 {d}/")
            
            if files:
                print("\n📄 [文件]")
                for f in files:
                    file_path = os.path.join(full_path, f)
                    size = os.path.getsize(file_path)
                    mtime = datetime.datetime.fromtimestamp(os.path.getmtime(file_path))
                    size_str = self._format_size(size)
                    print(f"  📄 {f:<35} {size_str:>10}  {mtime.strftime('%Y-%m-%d %H:%M:%S')}")
            
            print(f"\n📊 总计: {len(dirs)} 个目录, {len(files)} 个文件")
            
        except PermissionError:
            print(f"❌ 权限不足: {path}")
        except Exception as e:
            print(f"❌ 错误: {e}")
    
    def cmd_copy(self, args):
        """复制文件或目录"""
        if len(args) < 2:
            print("用法: copy <源> <目标>")
            return
        
        src = os.path.join(self.current_dir, args[0])
        dst = os.path.join(self.current_dir, args[1])
        
        try:
            if os.path.isdir(src):
                shutil.copytree(src, dst, dirs_exist_ok=True)
                print(f"✅ 目录已复制: {src} -> {dst}")
            else:
                shutil.copy2(src, dst)
                print(f"✅ 文件已复制: {src} -> {dst}")
        except Exception as e:
            print(f"❌ 复制失败: {e}")
    
    def cmd_move(self, args):
        """移动文件或目录"""
        if len(args) < 2:
            print("用法: move <源> <目标>")
            return
        
        src = os.path.join(self.current_dir, args[0])
        dst = os.path.join(self.current_dir, args[1])
        
        try:
            shutil.move(src, dst)
            print(f"✅ 已移动: {src} -> {dst}")
        except Exception as e:
            print(f"❌ 移动失败: {e}")
    
    def cmd_delete(self, args):
        """删除文件或目录"""
        if not args:
            print("用法: del <文件或目录>")
            return
        
        for item in args:
            path = os.path.join(self.current_dir, item)
            try:
                if os.path.isdir(path):
                    shutil.rmtree(path)
                    print(f"✅ 目录已删除: {item}")
                else:
                    os.remove(path)
                    print(f"✅ 文件已删除: {item}")
            except Exception as e:
                print(f"❌ 删除失败 {item}: {e}")
    
    def cmd_type(self, args):
        """显示文件内容"""
        if not args:
            print("用法: type <文件>")
            return
        
        file_path = os.path.join(self.current_dir, args[0])
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                print(f"📄 文件内容: {args[0]}")
                print("=" * 50)
                print(content)
        except Exception as e:
            print(f"❌ 读取文件失败: {e}")
    
    def cmd_mkdir(self, args):
        """创建目录"""
        if not args:
            print("用法: mkdir <目录名>")
            return
        
        for dir_name in args:
            try:
                os.makedirs(os.path.join(self.current_dir, dir_name), exist_ok=True)
                print(f"✅ 目录已创建: {dir_name}")
                self.user_data['files_created'] += 1
            except Exception as e:
                print(f"❌ 创建目录失败 {dir_name}: {e}")
    
    def cmd_rmdir(self, args):
        """删除空目录"""
        if not args:
            print("用法: rmdir <目录名>")
            return
        
        for dir_name in args:
            try:
                os.rmdir(os.path.join(self.current_dir, dir_name))
                print(f"✅ 目录已删除: {dir_name}")
            except Exception as e:
                print(f"❌ 删除目录失败 {dir_name}: {e}")
    
    def cmd_cd(self, args):
        """切换目录"""
        if not args:
            print("用法: cd <目录>")
            return
        
        path = args[0]
        if path == "..":
            new_dir = os.path.dirname(self.current_dir)
        elif path == ".":
            new_dir = self.current_dir
        else:
            new_dir = os.path.join(self.current_dir, path)
        
        try:
            os.chdir(new_dir)
            self.current_dir = os.getcwd()
        except Exception as e:
            print(f"❌ 切换目录失败: {e}")
    
    def cmd_pwd(self, args):
        """显示当前目录"""
        print(f"📍 当前目录: {self.current_dir}")
    
    def cmd_clear(self, args):
        """清屏"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def cmd_tree(self, args):
        """显示目录树"""
        path = args[0] if args else "."
        full_path = os.path.join(self.current_dir, path)
        
        def print_tree(dir_path, prefix=""):
            try:
                items = os.listdir(dir_path)
                items.sort()
                
                for i, item in enumerate(items):
                    item_path = os.path.join(dir_path, item)
                    is_last = i == len(items) - 1
                    
                    if os.path.isdir(item_path):
                        print(f"{prefix}{'└── ' if is_last else '├── '}📁 {item}/")
                        new_prefix = prefix + ("    " if is_last else "│   ")
                        print_tree(item_path, new_prefix)
                    else:
                        print(f"{prefix}{'└── ' if is_last else '├── '}📄 {item}")
            except PermissionError:
                print(f"{prefix}└── ❌ [权限不足]")
        
        print(f"🌳 目录树: {os.path.abspath(full_path)}")
        print_tree(full_path)
    
    def cmd_size(self, args):
        """显示文件大小"""
        if not args:
            print("用法: size <文件或目录>")
            return
        
        def get_size(path):
            total = 0
            try:
                if os.path.isfile(path):
                    return os.path.getsize(path)
                elif os.path.isdir(path):
                    for root, dirs, files in os.walk(path):
                        for file in files:
                            file_path = os.path.join(root, file)
                            try:
                                total += os.path.getsize(file_path)
                            except OSError:
                                continue
                    return total
            except OSError:
                return 0
            return total
        
        for item in args:
            item_path = os.path.join(self.current_dir, item)
            size = get_size(item_path)
            size_str = self._format_size(size)
            print(f"📊 {item}: {size_str}")
    
    def cmd_touch(self, args):
        """创建空文件"""
        if not args:
            print("用法: touch <文件>")
            return
        
        for file_name in args:
            file_path = os.path.join(self.current_dir, file_name)
            try:
                Path(file_path).touch()
                print(f"✅ 文件已创建: {file_name}")
                self.user_data['files_created'] += 1
            except Exception as e:
                print(f"❌ 创建文件失败 {file_name}: {e}")
    
    def _format_size(self, size):
        """格式化文件大小"""
        if size < 1024:
            return f"{size} B"
        elif size < 1024**2:
            return f"{size/1024:.1f} KB"
        elif size < 1024**3:
            return f"{size/1024**2:.1f} MB"
        else:
            return f"{size/1024**3:.1f} GB"
    
    def _print_file_info(self, file_path):
        """打印文件信息"""
        try:
            stat = os.stat(file_path)
            size = stat.st_size
            mtime = datetime.datetime.fromtimestamp(stat.st_mtime)
            size_str = self._format_size(size)
            
            print(f"📄 文件: {os.path.basename(file_path)}")
            print(f"📊 大小: {size_str}")
            print(f"🕒 修改时间: {mtime.strftime('%Y-%m-%d %H:%M:%S')}")
        except Exception as e:
            print(f"❌ 获取文件信息失败: {e}")

# ==================== PartA 结束 ====================

# ==================== PartB: 系统信息和网络工具 ====================

    # ==================== 系统信息命令 ====================
    
    def cmd_sysinfo(self, args):
        """显示系统信息"""
        print("💻 系统信息:")
        print(f"🖥️  操作系统: {platform.system()} {platform.release()}")
        print(f"🏗️  架构: {platform.machine()}")
        print(f"⚡ 处理器: {platform.processor()}")
        print(f"🐍 Python版本: {platform.python_version()}")
        print(f"👤 当前用户: {os.getlogin()}")
        print(f"📍 当前目录: {self.current_dir}")
        print(f"🕒 系统时间: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    def cmd_ps(self, args):
        """显示进程列表"""
        print("📋 进程列表:")
        print(f"{'PID':<8} {'名称':<20} {'CPU%':<8} {'内存%':<8}")
        print("-" * 50)
        
        for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
            try:
                info = proc.info
                print(f"{info['pid']:<8} {info['name']:<20} {info['cpu_percent']:<8.1f} {info['memory_percent']:<8.1f}")
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue
    
    def cmd_top(self, args):
        """实时显示系统资源使用情况"""
        print("📊 按 Ctrl+C 停止监控")
        try:
            while True:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("📊 系统资源监控:")
                print(f"⚡ CPU使用率: {psutil.cpu_percent()}%")
                print(f"💾 内存使用率: {psutil.virtual_memory().percent}%")
                print(f"💿 磁盘使用率: {psutil.disk_usage('/').percent}%")
                print(f"🕒 时间: {datetime.datetime.now().strftime('%H:%M:%S')}")
                time.sleep(1)
        except KeyboardInterrupt:
            print("\n⏹️  监控已停止")
    
    def cmd_disk(self, args):
        """显示磁盘信息"""
        print("💿 磁盘信息:")
        for partition in psutil.disk_partitions():
            try:
                usage = psutil.disk_usage(partition.mountpoint)
                print(f"📁 设备: {partition.device}")
                print(f"📂 挂载点: {partition.mountpoint}")
                print(f"📋 文件系统: {partition.fstype}")
                print(f"📊 总大小: {usage.total // (1024**3)} GB")
                print(f"📈 已用: {usage.used // (1024**3)} GB")
                print(f"📉 可用: {usage.free // (1024**3)} GB")
                print(f"📊 使用率: {usage.percent}%")
                print("-" * 40)
            except Exception:
                continue
    
    def cmd_memory(self, args):
        """显示内存信息"""
        memory = psutil.virtual_memory()
        print("💾 内存信息:")
        print(f"📊 总内存: {memory.total // (1024**3)} GB")
        print(f"✅ 可用内存: {memory.available // (1024**3)} GB")
        print(f"📈 已用内存: {memory.used // (1024**3)} GB")
        print(f"📊 内存使用率: {memory.percent}%")
    
    def cmd_network(self, args):
        """显示网络信息"""
        print("🌐 网络信息:")
        try:
            # 获取网络接口信息
            net_io = psutil.net_io_counters()
            print(f"📤 发送字节: {self._format_size(net_io.bytes_sent)}")
            print(f"📥 接收字节: {self._format_size(net_io.bytes_recv)}")
            print(f"📤 发送包数: {net_io.packets_sent}")
            print(f"📥 接收包数: {net_io.packets_recv}")
            
            # 获取网络接口
            print("\n📡 网络接口:")
            for interface, addresses in psutil.net_if_addrs().items():
                print(f"  📡 {interface}:")
                for addr in addresses:
                    print(f"    📍 {addr.address}")
        except Exception as e:
            print(f"❌ 获取网络信息失败: {e}")
    
    # ==================== 网络工具命令 ====================
    
    def cmd_ping(self, args):
        """ping主机"""
        if not args:
            print("用法: ping <主机>")
            return
        
        host = args[0]
        print(f"🏓 Pinging {host}...")
        try:
            result = subprocess.run(['ping', '-n', '4', host] if os.name == 'nt' else ['ping', '-c', '4', host], 
                                  capture_output=True, text=True)
            print(result.stdout)
        except Exception as e:
            print(f"❌ ping失败: {e}")
    
    def cmd_netstat(self, args):
        """显示网络连接"""
        print("🌐 网络连接:")
        print(f"{'协议':<6} {'本地地址':<20} {'远程地址':<20} {'状态':<12}")
        print("-" * 60)
        
        try:
            for conn in psutil.net_connections():
                if conn.status == 'ESTABLISHED':
                    try:
                        # 安全地获取地址信息
                        local_addr = "N/A"
                        remote_addr = "N/A"
                        
                        # 使用getattr安全获取属性
                        try:
                            local_ip = getattr(conn.laddr, 'ip', None)
                            local_port = getattr(conn.laddr, 'port', None)
                            if local_ip and local_port:
                                local_addr = f"{local_ip}:{local_port}"
                        except:
                            pass
                        
                        if conn.raddr:
                            try:
                                remote_ip = getattr(conn.raddr, 'ip', None)
                                remote_port = getattr(conn.raddr, 'port', None)
                                if remote_ip and remote_port:
                                    remote_addr = f"{remote_ip}:{remote_port}"
                            except:
                                pass
                        
                        print(f"{conn.type:<6} {local_addr:<20} {remote_addr:<20} {conn.status:<12}")
                    except Exception:
                        continue
        except Exception as e:
            print(f"❌ 获取网络连接失败: {e}")
    
    def cmd_ipconfig(self, args):
        """显示网络配置"""
        print("🌐 网络配置:")
        try:
            for interface, addresses in psutil.net_if_addrs().items():
                print(f"📡 接口: {interface}")
                for addr in addresses:
                    print(f"  📍 地址: {addr.address}")
                    print(f"  🎯 网络掩码: {addr.netmask}")
                    print(f"  📢 广播地址: {addr.broadcast}")
                print("-" * 30)
        except Exception as e:
            print(f"❌ 获取网络配置失败: {e}")
    
    def cmd_browser(self, args):
        """打开浏览器访问网址"""
        if not args:
            print("用法: browser <网址>")
            print("示例: browser https://www.google.com")
            return
        
        url = args[0]
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url
        
        try:
            print(f"🌐 正在打开浏览器访问: {url}")
            webbrowser.open(url)
            print("✅ 浏览器已打开")
        except Exception as e:
            print(f"❌ 打开浏览器失败: {e}")
    
    def cmd_download(self, args):
        """下载文件"""
        if not REQUESTS_AVAILABLE:
            print("❌ 下载功能需要安装 requests 库")
            print("请运行: pip install requests")
            return
        
        if len(args) < 2:
            print("用法: download <URL> <文件名>")
            print("示例: download https://example.com/file.txt myfile.txt")
            return
        
        url = args[0]
        filename = args[1]
        
        try:
            print(f"📥 正在下载: {url}")
            print(f"📁 保存为: {filename}")
            
            response = requests.get(url, stream=True)
            response.raise_for_status()
            
            total_size = int(response.headers.get('content-length', 0))
            downloaded = 0
            
            with open(filename, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
                        downloaded += len(chunk)
                        if total_size > 0:
                            percent = (downloaded / total_size) * 100
                            print(f"\r📊 下载进度: {percent:.1f}%", end='', flush=True)
            
            print(f"\n✅ 下载完成: {filename}")
            print(f"📊 文件大小: {self._format_size(downloaded)}")
            
        except Exception as e:
            print(f"❌ 下载失败: {e}")

# ==================== PartB 结束 ====================

# ==================== PartC: 文本处理和压缩工具 ====================

    # ==================== 文本处理命令 ====================
    
    def cmd_find(self, args):
        """查找文件"""
        if len(args) < 2:
            print("用法: find <目录> <文件名模式>")
            return
        
        search_dir = os.path.join(self.current_dir, args[0])
        pattern = args[1]
        
        print(f"🔍 在 {search_dir} 中查找包含 '{pattern}' 的文件:")
        found_count = 0
        
        for root, dirs, files in os.walk(search_dir):
            for file in files:
                if pattern.lower() in file.lower():
                    full_path = os.path.join(root, file)
                    print(f"  📄 {full_path}")
                    found_count += 1
        
        print(f"📊 找到 {found_count} 个文件")
    
    def cmd_grep(self, args):
        """在文件中搜索文本"""
        if len(args) < 2:
            print("用法: grep <模式> <文件>")
            return
        
        pattern = args[0]
        file_path = os.path.join(self.current_dir, args[1])
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                print(f"🔍 在 {args[1]} 中搜索 '{pattern}':")
                print("=" * 50)
                found_count = 0
                for line_num, line in enumerate(f, 1):
                    if pattern.lower() in line.lower():
                        print(f"  {line_num:3d}: {line.rstrip()}")
                        found_count += 1
                print(f"📊 找到 {found_count} 个匹配")
        except Exception as e:
            print(f"❌ 搜索失败: {e}")
    
    def cmd_sort(self, args):
        """排序文件内容"""
        if not args:
            print("用法: sort <文件>")
            return
        
        file_path = os.path.join(self.current_dir, args[0])
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                lines.sort()
                print(f"📄 排序后的内容:")
                print("=" * 30)
                for line in lines:
                    print(line.rstrip())
        except Exception as e:
            print(f"❌ 排序失败: {e}")
    
    def cmd_uniq(self, args):
        """去除重复行"""
        if not args:
            print("用法: uniq <文件>")
            return
        
        file_path = os.path.join(self.current_dir, args[0])
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                seen = set()
                unique_lines = []
                for line in lines:
                    if line not in seen:
                        unique_lines.append(line)
                        seen.add(line)
                
                print(f"📄 去重后的内容:")
                print("=" * 30)
                for line in unique_lines:
                    print(line.rstrip())
                print(f"📊 原始行数: {len(lines)}, 去重后: {len(unique_lines)}")
        except Exception as e:
            print(f"❌ 去重失败: {e}")
    
    def cmd_head(self, args):
        """显示文件开头"""
        if len(args) < 1:
            print("用法: head <文件> [行数]")
            return
        
        file_path = os.path.join(self.current_dir, args[0])
        lines = int(args[1]) if len(args) > 1 else 10
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                print(f"📄 {args[0]} 的前 {lines} 行:")
                print("=" * 30)
                for i, line in enumerate(f):
                    if i >= lines:
                        break
                    print(line.rstrip())
        except Exception as e:
            print(f"❌ 读取文件失败: {e}")
    
    def cmd_tail(self, args):
        """显示文件结尾"""
        if len(args) < 1:
            print("用法: tail <文件> [行数]")
            return
        
        file_path = os.path.join(self.current_dir, args[0])
        lines = int(args[1]) if len(args) > 1 else 10
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                all_lines = f.readlines()
                start = max(0, len(all_lines) - lines)
                print(f"📄 {args[0]} 的后 {lines} 行:")
                print("=" * 30)
                for line in all_lines[start:]:
                    print(line.rstrip())
        except Exception as e:
            print(f"❌ 读取文件失败: {e}")
    
    def cmd_wc(self, args):
        """统计文件行数、单词数、字符数"""
        if not args:
            print("用法: wc <文件>")
            return
        
        file_path = os.path.join(self.current_dir, args[0])
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                lines = len(content.splitlines())
                words = len(content.split())
                chars = len(content)
                
                print(f"📊 文件统计: {args[0]}")
                print(f"📄 行数: {lines}")
                print(f"📝 单词数: {words}")
                print(f"🔤 字符数: {chars}")
        except Exception as e:
            print(f"❌ 统计失败: {e}")
    
    # ==================== 压缩工具命令 ====================
    
    def cmd_zip(self, args):
        """创建ZIP压缩包"""
        if len(args) < 2:
            print("用法: zip <压缩包名> <文件或目录>")
            return
        
        zip_name = args[0]
        items = args[1:]
        
        try:
            with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
                for item in items:
                    item_path = os.path.join(self.current_dir, item)
                    if os.path.isdir(item_path):
                        for root, dirs, files in os.walk(item_path):
                            for file in files:
                                file_path = os.path.join(root, file)
                                arcname = os.path.relpath(file_path, self.current_dir)
                                zipf.write(file_path, arcname)
                    else:
                        zipf.write(item_path, item)
            print(f"✅ ZIP压缩包已创建: {zip_name}")
        except Exception as e:
            print(f"❌ 创建压缩包失败: {e}")
    
    def cmd_unzip(self, args):
        """解压ZIP文件"""
        if not args:
            print("用法: unzip <压缩包>")
            return
        
        zip_path = os.path.join(self.current_dir, args[0])
        try:
            with zipfile.ZipFile(zip_path, 'r') as zipf:
                zipf.extractall(self.current_dir)
            print(f"✅ 文件已解压: {args[0]}")
        except Exception as e:
            print(f"❌ 解压失败: {e}")
    
    def cmd_tar(self, args):
        """创建TAR压缩包"""
        if len(args) < 2:
            print("用法: tar <压缩包名> <文件或目录>")
            return
        
        tar_name = args[0]
        items = args[1:]
        
        try:
            with tarfile.open(tar_name, 'w:gz') as tar:
                for item in items:
                    item_path = os.path.join(self.current_dir, item)
                    tar.add(item_path, arcname=item)
            print(f"✅ TAR压缩包已创建: {tar_name}")
        except Exception as e:
            print(f"❌ 创建TAR压缩包失败: {e}")
    
    def cmd_untar(self, args):
        """解压TAR文件"""
        if not args:
            print("用法: untar <压缩包>")
            return
        
        tar_path = os.path.join(self.current_dir, args[0])
        try:
            with tarfile.open(tar_path, 'r:*') as tar:
                tar.extractall(self.current_dir)
            print(f"✅ 文件已解压: {args[0]}")
        except Exception as e:
            print(f"❌ 解压失败: {e}")
    
    def cmd_backup(self, args):
        """备份文件"""
        if len(args) < 2:
            print("用法: backup <源文件> <备份目录>")
            return
        
        src = os.path.join(self.current_dir, args[0])
        backup_dir = os.path.join(self.current_dir, args[1])
        
        try:
            os.makedirs(backup_dir, exist_ok=True)
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            backup_name = f"{os.path.basename(src)}_{timestamp}"
            backup_path = os.path.join(backup_dir, backup_name)
            
            if os.path.isdir(src):
                shutil.copytree(src, backup_path)
            else:
                shutil.copy2(src, backup_path)
            
            print(f"✅ 备份已创建: {backup_path}")
        except Exception as e:
            print(f"❌ 备份失败: {e}")

# ==================== PartC 结束 ====================

# ==================== PartD: 安全工具和其他工具 ====================

    # ==================== 安全工具命令 ====================
    
    def cmd_hash(self, args):
        """计算文件哈希值"""
        if not args:
            print("用法: hash <文件>")
            return
        
        file_path = os.path.join(self.current_dir, args[0])
        try:
            with open(file_path, 'rb') as f:
                content = f.read()
                md5_hash = hashlib.md5(content).hexdigest()
                sha1_hash = hashlib.sha1(content).hexdigest()
                sha256_hash = hashlib.sha256(content).hexdigest()
                
                print(f"🔒 文件: {args[0]}")
                print(f"🔐 MD5: {md5_hash}")
                print(f"🔐 SHA1: {sha1_hash}")
                print(f"🔐 SHA256: {sha256_hash}")
        except Exception as e:
            print(f"❌ 计算哈希值失败: {e}")
    
    def cmd_md5(self, args):
        """计算MD5值"""
        if not args:
            print("用法: md5 <文件>")
            return
        
        file_path = os.path.join(self.current_dir, args[0])
        try:
            with open(file_path, 'rb') as f:
                content = f.read()
                md5_hash = hashlib.md5(content).hexdigest()
                print(f"🔐 MD5: {md5_hash}")
        except Exception as e:
            print(f"❌ 计算MD5失败: {e}")
    
    def cmd_sha1(self, args):
        """计算SHA1值"""
        if not args:
            print("用法: sha1 <文件>")
            return
        
        file_path = os.path.join(self.current_dir, args[0])
        try:
            with open(file_path, 'rb') as f:
                content = f.read()
                sha1_hash = hashlib.sha1(content).hexdigest()
                print(f"🔐 SHA1: {sha1_hash}")
        except Exception as e:
            print(f"❌ 计算SHA1失败: {e}")
    
    def cmd_sha256(self, args):
        """计算SHA256值"""
        if not args:
            print("用法: sha256 <文件>")
            return
        
        file_path = os.path.join(self.current_dir, args[0])
        try:
            with open(file_path, 'rb') as f:
                content = f.read()
                sha256_hash = hashlib.sha256(content).hexdigest()
                print(f"🔐 SHA256: {sha256_hash}")
        except Exception as e:
            print(f"❌ 计算SHA256失败: {e}")
    
    def cmd_encrypt(self, args):
        """简单加密文件"""
        if len(args) < 2:
            print("用法: encrypt <文件> <密码>")
            return
        
        file_path = os.path.join(self.current_dir, args[0])
        password = args[1]
        
        try:
            with open(file_path, 'rb') as f:
                content = f.read()
            
            # 简单的XOR加密
            encrypted = bytes([b ^ ord(password[i % len(password)]) for i, b in enumerate(content)])
            
            encrypted_path = file_path + '.enc'
            with open(encrypted_path, 'wb') as f:
                f.write(encrypted)
            
            print(f"✅ 文件已加密: {encrypted_path}")
        except Exception as e:
            print(f"❌ 加密失败: {e}")
    
    def cmd_decrypt(self, args):
        """解密文件"""
        if len(args) < 2:
            print("用法: decrypt <加密文件> <密码>")
            return
        
        file_path = os.path.join(self.current_dir, args[0])
        password = args[1]
        
        try:
            with open(file_path, 'rb') as f:
                encrypted = f.read()
            
            # 简单的XOR解密
            decrypted = bytes([b ^ ord(password[i % len(password)]) for i, b in enumerate(encrypted)])
            
            decrypted_path = file_path.replace('.enc', '.dec')
            with open(decrypted_path, 'wb') as f:
                f.write(decrypted)
            
            print(f"✅ 文件已解密: {decrypted_path}")
        except Exception as e:
            print(f"❌ 解密失败: {e}")
    
    # ==================== 其他工具命令 ====================
    
    def cmd_date(self, args):
        """显示当前日期"""
        now = datetime.datetime.now()
        print(f"📅 当前日期: {now.strftime('%Y-%m-%d %H:%M:%S')}")
    
    def cmd_time(self, args):
        """显示当前时间"""
        now = datetime.datetime.now()
        print(f"🕒 当前时间: {now.strftime('%H:%M:%S')}")
    
    def cmd_echo(self, args):
        """显示文本"""
        print(" ".join(args))
    
    def cmd_history(self, args):
        """显示命令历史"""
        print("📜 命令历史:")
        for i, cmd in enumerate(self.history[-20:], 1):
            print(f"{i:2d}: {cmd}")
    
    def cmd_calc(self, args):
        """简单计算器"""
        if not args:
            print("用法: calc <表达式>")
            print("示例: calc 2 + 3 * 4")
            return
        
        try:
            expression = " ".join(args)
            result = eval(expression)
            print(f"🧮 {expression} = {result}")
        except Exception as e:
            print(f"❌ 计算错误: {e}")
    
    def cmd_random(self, args):
        """生成随机数"""
        if len(args) < 2:
            print("用法: random <最小值> <最大值> [数量]")
            return
        
        try:
            min_val = int(args[0])
            max_val = int(args[1])
            count = int(args[2]) if len(args) > 2 else 1
            
            print(f"🎲 生成 {count} 个 {min_val}-{max_val} 之间的随机数:")
            for _ in range(count):
                print(random.randint(min_val, max_val))
        except ValueError:
            print("❌ 请输入有效的数字")
    
    def cmd_help(self, args):
        """显示帮助信息"""
        help_text = """
🎯 超级Python模拟系统 - 帮助信息

📁 文件操作:
  dir, ls          - 列出目录内容
  copy, cp         - 复制文件或目录
  move, mv         - 移动文件或目录
  del, rm          - 删除文件或目录
  type, cat        - 显示文件内容
  mkdir            - 创建目录
  rmdir            - 删除空目录
  cd               - 切换目录
  pwd              - 显示当前目录
  touch            - 创建空文件
  tree             - 显示目录树
  size             - 显示文件大小

💻 系统信息:
  sysinfo          - 显示系统信息
  ps               - 显示进程列表
  top              - 实时系统监控
  disk             - 显示磁盘信息
  memory           - 显示内存信息
  network          - 显示网络信息

🌐 网络工具:
  ping             - ping主机
  netstat          - 显示网络连接
  ipconfig         - 显示网络配置
  browser          - 打开浏览器
  download         - 下载文件

📝 文本处理:
  find             - 查找文件
  grep             - 搜索文本
  sort             - 排序文件内容
  uniq             - 去除重复行
  head             - 显示文件开头
  tail             - 显示文件结尾
  wc               - 统计文件行数

📦 压缩工具:
  zip              - 创建ZIP压缩包
  unzip            - 解压ZIP文件
  tar              - 创建TAR压缩包
  untar            - 解压TAR文件
  backup           - 备份文件

🔒 安全工具:
  hash             - 计算文件哈希值
  md5              - 计算MD5值
  sha1             - 计算SHA1值
  sha256           - 计算SHA256值
  encrypt          - 加密文件
  decrypt          - 解密文件

🎮 小游戏:
  snake            - 贪吃蛇游戏
  tetris           - 俄罗斯方块
  guess            - 猜数字游戏
  tictactoe        - 井字棋
  hangman          - 猜词游戏

🛠️  其他工具:
  calc             - 简单计算器
  random           - 生成随机数
  date             - 显示当前日期
  time             - 显示当前时间
  echo             - 显示文本
  history          - 显示命令历史
  profile          - 显示用户资料
  level            - 显示等级信息
  games            - 显示游戏列表
  alias            - 设置命令别名
  unalias          - 删除命令别名
  cls, clear       - 清屏
  help             - 显示此帮助
  exit, quit       - 退出系统

📋 用法示例:
  dir              - 列出当前目录内容
  copy file1 file2 - 复制file1到file2
  mkdir newdir     - 创建新目录
  cd newdir        - 切换到newdir目录
  type file.txt    - 显示file.txt内容
  sysinfo          - 显示系统信息
  browser google.com - 打开浏览器访问Google
  download https://example.com/file.txt myfile.txt - 下载文件
  snake            - 开始贪吃蛇游戏
  help             - 显示帮助信息
        """
        print(help_text)
    
    def cmd_exit(self, args):
        """退出系统"""
        print("👋 再见!")
        self.running = False
    
    def cmd_alias(self, args):
        """设置命令别名"""
        if len(args) < 2:
            print("用法: alias <别名> <命令>")
            return
        
        alias = args[0]
        command = " ".join(args[1:])
        self.aliases[alias] = command
        print(f"✅ 别名已设置: {alias} -> {command}")
    
    def cmd_unalias(self, args):
        """删除命令别名"""
        if not args:
            print("用法: unalias <别名>")
            return
        
        alias = args[0]
        if alias in self.aliases:
            del self.aliases[alias]
            print(f"✅ 别名已删除: {alias}")
        else:
            print(f"❌ 别名不存在: {alias}")
    
    def cmd_profile(self, args):
        """显示用户资料"""
        print("👤 用户资料:")
        print(f"👤 用户名: {self.user_data['username']}")
        print(f"⭐ 等级: {self.user_data['level']}")
        print(f"📈 经验值: {self.user_data['experience']}")
        print(f"🏆 游戏胜利: {self.user_data['games_won']}")
        print(f"📁 创建文件: {self.user_data['files_created']}")
        print(f"⌨️  使用命令: {self.user_data['commands_used']}")
    
    def cmd_level(self, args):
        """显示等级信息"""
        exp_needed = self.user_data['level'] * 100
        print(f"⭐ 当前等级: {self.user_data['level']}")
        print(f"📈 当前经验: {self.user_data['experience']}")
        print(f"🎯 升级需要: {exp_needed} 经验")
        print(f"📊 进度: {self.user_data['experience']}/{exp_needed}")
    
    def cmd_games(self, args):
        """显示游戏列表"""
        games_text = """
🎮 可用游戏:

🐍 snake      - 贪吃蛇游戏
🧩 tetris     - 俄罗斯方块
🎯 guess      - 猜数字游戏
⭕ tictactoe  - 井字棋
🎭 hangman    - 猜词游戏

输入游戏名称开始游戏，例如: snake
        """
        print(games_text)

# ==================== PartD 结束 ====================

# ==================== PartE: 小游戏功能 ====================

    # ==================== 游戏命令 ====================
    
    def cmd_snake(self, args):
        """贪吃蛇游戏"""
        print("🐍 贪吃蛇游戏")
        print("使用 WASD 键控制蛇的移动")
        print("按 Q 退出游戏")
        print("按任意键开始...")
        input()
        
        try:
            import msvcrt
            import os
            
            # 游戏设置
            width, height = 20, 15
            snake = [(width//2, height//2)]
            direction = (1, 0)
            food = (random.randint(0, width-1), random.randint(0, height-1))
            score = 0
            game_over = False
            
            while not game_over:
                # 清屏
                os.system('cls' if os.name == 'nt' else 'clear')
                
                # 绘制游戏区域
                print("=" * (width + 2))
                for y in range(height):
                    print("|", end="")
                    for x in range(width):
                        if (x, y) in snake:
                            print("█", end="")
                        elif (x, y) == food:
                            print("🍎", end="")
                        else:
                            print(" ", end="")
                    print("|")
                print("=" * (width + 2))
                print(f"得分: {score}")
                
                # 检查按键
                if msvcrt.kbhit():
                    key = msvcrt.getch().decode().lower()
                    if key == 'w' and direction != (0, 1):
                        direction = (0, -1)
                    elif key == 's' and direction != (0, -1):
                        direction = (0, 1)
                    elif key == 'a' and direction != (1, 0):
                        direction = (-1, 0)
                    elif key == 'd' and direction != (-1, 0):
                        direction = (1, 0)
                    elif key == 'q':
                        break
                
                # 移动蛇
                new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
                
                # 检查碰撞
                if (new_head[0] < 0 or new_head[0] >= width or 
                    new_head[1] < 0 or new_head[1] >= height or 
                    new_head in snake):
                    game_over = True
                    break
                
                snake.insert(0, new_head)
                
                # 检查是否吃到食物
                if new_head == food:
                    score += 10
                    food = (random.randint(0, width-1), random.randint(0, height-1))
                    while food in snake:
                        food = (random.randint(0, width-1), random.randint(0, height-1))
                else:
                    snake.pop()
                
                time.sleep(0.2)
            
            print(f"🎮 游戏结束! 最终得分: {score}")
            if score > 0:
                self.user_data['games_won'] += 1
                self.user_data['experience'] += score
                print(f"🏆 获得 {score} 经验值!")
            
        except ImportError:
            print("❌ 在Windows系统上才能运行此游戏")
        except Exception as e:
            print(f"❌ 游戏运行失败: {e}")
    
    def cmd_tetris(self, args):
        """俄罗斯方块游戏"""
        print("🧩 俄罗斯方块游戏")
        print("使用 A/D 移动，S 加速下落，W 旋转")
        print("按 Q 退出游戏")
        print("按任意键开始...")
        input()
        
        try:
            import msvcrt
            
            # 游戏设置
            width, height = 10, 20
            board = [[0] * width for _ in range(height)]
            score = 0
            level = 1
            
            # 方块形状
            shapes = [
                [[1, 1, 1, 1]],  # I
                [[1, 1], [1, 1]],  # O
                [[1, 1, 1], [0, 1, 0]],  # T
                [[1, 1, 1], [1, 0, 0]],  # L
                [[1, 1, 1], [0, 0, 1]],  # J
                [[1, 1, 0], [0, 1, 1]],  # S
                [[0, 1, 1], [1, 1, 0]]   # Z
            ]
            
            current_shape = random.choice(shapes)
            current_x, current_y = width // 2 - len(current_shape[0]) // 2, 0
            
            def draw_board():
                os.system('cls' if os.name == 'nt' else 'clear')
                print("=" * (width + 2))
                for y in range(height):
                    print("|", end="")
                    for x in range(width):
                        if board[y][x]:
                            print("█", end="")
                        else:
                            print(" ", end="")
                    print("|")
                print("=" * (width + 2))
                print(f"得分: {score} 等级: {level}")
            
            def check_collision(shape, x, y):
                for row in range(len(shape)):
                    for col in range(len(shape[row])):
                        if shape[row][col]:
                            new_x, new_y = x + col, y + row
                            if (new_x < 0 or new_x >= width or 
                                new_y >= height or 
                                (new_y >= 0 and board[new_y][new_x])):
                                return True
                return False
            
            def place_shape():
                for row in range(len(current_shape)):
                    for col in range(len(current_shape[row])):
                        if current_shape[row][col]:
                            board[current_y + row][current_x + col] = 1
            
            def clear_lines():
                nonlocal score
                lines_cleared = 0
                y = height - 1
                while y >= 0:
                    if all(board[y]):
                        del board[y]
                        board.insert(0, [0] * width)
                        lines_cleared += 1
                    else:
                        y -= 1
                if lines_cleared > 0:
                    score += lines_cleared * 100 * level
            
            game_over = False
            while not game_over:
                draw_board()
                
                # 检查按键
                if msvcrt.kbhit():
                    key = msvcrt.getch().decode().lower()
                    if key == 'a' and not check_collision(current_shape, current_x - 1, current_y):
                        current_x -= 1
                    elif key == 'd' and not check_collision(current_shape, current_x + 1, current_y):
                        current_x += 1
                    elif key == 's':
                        if not check_collision(current_shape, current_x, current_y + 1):
                            current_y += 1
                    elif key == 'w':
                        # 旋转
                        rotated = list(zip(*current_shape[::-1]))
                        if not check_collision(rotated, current_x, current_y):
                            current_shape = rotated
                    elif key == 'q':
                        break
                
                # 自动下落
                if not check_collision(current_shape, current_x, current_y + 1):
                    current_y += 1
                else:
                    place_shape()
                    clear_lines()
                    current_shape = random.choice(shapes)
                    current_x, current_y = width // 2 - len(current_shape[0]) // 2, 0
                    if check_collision(current_shape, current_x, current_y):
                        game_over = True
                
                time.sleep(0.5)
            
            print(f"🎮 游戏结束! 最终得分: {score}")
            if score > 0:
                self.user_data['games_won'] += 1
                self.user_data['experience'] += score // 10
                print(f"🏆 获得 {score // 10} 经验值!")
            
        except ImportError:
            print("❌ 在Windows系统上才能运行此游戏")
        except Exception as e:
            print(f"❌ 游戏运行失败: {e}")
    
    def cmd_guess(self, args):
        """猜数字游戏"""
        print("🎯 猜数字游戏")
        print("我想了一个1-100之间的数字，请你猜一猜!")
        
        number = random.randint(1, 100)
        attempts = 0
        max_attempts = 10
        
        while attempts < max_attempts:
            try:
                guess = int(input(f"第 {attempts + 1} 次猜测 (1-100): "))
                attempts += 1
                
                if guess < number:
                    print("📈 太小了，再大一点!")
                elif guess > number:
                    print("📉 太大了，再小一点!")
                else:
                    print(f"🎉 恭喜你猜对了! 数字是 {number}")
                    print(f"📊 你用了 {attempts} 次就猜对了!")
                    self.user_data['games_won'] += 1
                    self.user_data['experience'] += (11 - attempts) * 10
                    print(f"🏆 获得 {(11 - attempts) * 10} 经验值!")
                    return
                
                if attempts < max_attempts:
                    print(f"⏰ 还有 {max_attempts - attempts} 次机会")
                
            except ValueError:
                print("❌ 请输入有效的数字!")
                attempts -= 1
        
        print(f"😔 游戏结束! 正确答案是 {number}")
    
    def cmd_tictactoe(self, args):
        """井字棋游戏"""
        print("⭕ 井字棋游戏")
        print("你是 X，电脑是 O")
        print("输入 1-9 选择位置:")
        print("1 2 3")
        print("4 5 6")
        print("7 8 9")
        
        board = [' '] * 9
        positions = [str(i) for i in range(1, 10)]
        
        def print_board():
            print(f" {board[0]} | {board[1]} | {board[2]} ")
            print("---+---+---")
            print(f" {board[3]} | {board[4]} | {board[5]} ")
            print("---+---+---")
            print(f" {board[6]} | {board[7]} | {board[8]} ")
        
        def check_winner(board):
            lines = [
                [0, 1, 2], [3, 4, 5], [6, 7, 8],  # 横
                [0, 3, 6], [1, 4, 7], [2, 5, 8],  # 竖
                [0, 4, 8], [2, 4, 6]  # 斜
            ]
            for line in lines:
                if board[line[0]] == board[line[1]] == board[line[2]] != ' ':
                    return board[line[0]]
            return None
        
        def is_board_full(board):
            return ' ' not in board
        
        def computer_move(board):
            # 简单AI
            for i in range(9):
                if board[i] == ' ':
                    board_copy = board.copy()
                    board_copy[i] = 'O'
                    if check_winner(board_copy) == 'O':
                        return i
            
            for i in range(9):
                if board[i] == ' ':
                    board_copy = board.copy()
                    board_copy[i] = 'X'
                    if check_winner(board_copy) == 'X':
                        return i
            
            # 优先选择中心
            if board[4] == ' ':
                return 4
            
            # 随机选择
            empty = [i for i in range(9) if board[i] == ' ']
            return random.choice(empty)
        
        while True:
            print_board()
            
            # 玩家回合
            try:
                move = int(input("你的回合 (1-9): ")) - 1
                if move < 0 or move > 8 or board[move] != ' ':
                    print("❌ 无效的移动!")
                    continue
                board[move] = 'X'
            except ValueError:
                print("❌ 请输入1-9的数字!")
                continue
            
            if check_winner(board) == 'X':
                print_board()
                print("🎉 恭喜你赢了!")
                self.user_data['games_won'] += 1
                self.user_data['experience'] += 50
                print("🏆 获得 50 经验值!")
                break
            
            if is_board_full(board):
                print_board()
                print("🤝 平局!")
                break
            
            # 电脑回合
            print("🤖 电脑思考中...")
            time.sleep(1)
            computer_pos = computer_move(board)
            board[computer_pos] = 'O'
            
            if check_winner(board) == 'O':
                print_board()
                print("😔 电脑赢了!")
                break
            
            if is_board_full(board):
                print_board()
                print("🤝 平局!")
                break
    
    def cmd_hangman(self, args):
        """猜词游戏"""
        words = ['python', 'computer', 'programming', 'algorithm', 'database', 
                'network', 'security', 'software', 'hardware', 'internet']
        word = random.choice(words)
        guessed = set()
        wrong_guesses = 0
        max_wrong = 6
        
        print("🎭 猜词游戏")
        print(f"单词有 {len(word)} 个字母")
        
        while wrong_guesses < max_wrong:
            # 显示当前状态
            display = ''
            for letter in word:
                if letter in guessed:
                    display += letter
                else:
                    display += '_'
            print(f"📝 单词: {display}")
            print(f"❌ 错误次数: {wrong_guesses}/{max_wrong}")
            print(f"🔤 已猜字母: {', '.join(sorted(guessed))}")
            
            # 检查是否完成
            if '_' not in display:
                print(f"🎉 恭喜你猜对了! 单词是 '{word}'")
                self.user_data['games_won'] += 1
                self.user_data['experience'] += (max_wrong - wrong_guesses) * 10
                print(f"🏆 获得 {(max_wrong - wrong_guesses) * 10} 经验值!")
                return
            
            # 获取猜测
            try:
                guess = input("猜一个字母: ").lower()
                if len(guess) != 1:
                    print("❌ 请输入一个字母!")
                    continue
                if not guess.isalpha():
                    print("❌ 请输入字母!")
                    continue
                if guess in guessed:
                    print("❌ 这个字母已经猜过了!")
                    continue
                
                guessed.add(guess)
                if guess in word:
                    print("✅ 猜对了!")
                else:
                    print("❌ 猜错了!")
                    wrong_guesses += 1
                    
            except KeyboardInterrupt:
                print("\n👋 游戏结束!")
                return
        
        print(f"😔 游戏结束! 正确答案是 '{word}'")

# ==================== PartE 结束 ====================

# ==================== PartF: 主函数和程序入口 ====================

def main():
    """主函数"""
    try:
        print("🚀 正在启动超级Python模拟系统...")
        system = SuperCommandLineSystem()
        system.run()
    except KeyboardInterrupt:
        print("\n👋 程序已退出")
    except Exception as e:
        print(f"❌ 系统错误: {e}")
        print("💡 请检查依赖包是否安装完整")
        print("📦 需要安装的包: psutil, requests")

if __name__ == "__main__":
    main()
