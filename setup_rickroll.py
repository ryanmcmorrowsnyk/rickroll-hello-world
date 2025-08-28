#!/usr/bin/env python3
"""
Rick Roll Hello World - Easy Setup Script
Automatically installs dependencies and runs the app for your friends!
"""

import os
import sys
import subprocess
import platform

def print_banner():
    """Print a fun banner"""
    banner = """
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║              🎵 RICK ROLL HELLO WORLD SETUP 🎵               ║
║                                                              ║
║        Get ready to rickroll yourself and your friends!     ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
    """
    print(banner)

def check_python_version():
    """Check if Python version is compatible"""
    version = sys.version_info
    if version < (3, 6):
        print("❌ Error: This app requires Python 3.6 or higher")
        print(f"   Your version: {version.major}.{version.minor}.{version.micro}")
        print("   Please update Python and try again.")
        return False
    
    print(f"✅ Python {version.major}.{version.minor}.{version.micro} detected - Compatible!")
    return True

def install_dependencies():
    """Install required packages"""
    print("\n📦 Installing dependencies...")
    
    try:
        # Check if requirements.txt exists
        if not os.path.exists('requirements.txt'):
            print("❌ requirements.txt not found!")
            return False
        
        # Install requirements
        result = subprocess.run([
            sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'
        ], capture_output=True, text=True)
        
        if result.returncode == 0:
            print("✅ Dependencies installed successfully!")
            return True
        else:
            print("❌ Error installing dependencies:")
            print(result.stderr)
            return False
            
    except Exception as e:
        print(f"❌ Error during installation: {e}")
        return False

def check_required_files():
    """Check if all required files are present"""
    required_files = [
        'hello_world_rickroll.py',
        'requirements.txt',
        'never_gonna_give_you_up.mid'
    ]
    
    print("\n📁 Checking required files...")
    
    missing_files = []
    for file in required_files:
        if os.path.exists(file):
            print(f"✅ {file}")
        else:
            print(f"❌ {file} - MISSING!")
            missing_files.append(file)
    
    if missing_files:
        print(f"\n❌ Missing files: {', '.join(missing_files)}")
        print("   Please make sure all files are in the same directory.")
        return False
    
    return True

def get_system_info():
    """Display system information"""
    print(f"\n💻 System Information:")
    print(f"   OS: {platform.system()} {platform.release()}")
    print(f"   Architecture: {platform.machine()}")
    print(f"   Python: {sys.version}")

def run_app():
    """Launch the Rick Roll app"""
    print("\n🚀 Launching Rick Roll Hello World...")
    print("   Click 'World' in the app to get rickrolled! 🎵")
    print("   Close this window after launching if you want.")
    
    try:
        # Launch the app
        if platform.system() == "Windows":
            subprocess.Popen([sys.executable, 'hello_world_rickroll.py'], 
                           creationflags=subprocess.CREATE_NEW_CONSOLE)
        else:
            subprocess.Popen([sys.executable, 'hello_world_rickroll.py'])
        
        print("✅ App launched successfully!")
        print("\n🎉 Enjoy your rickroll experience!")
        
    except Exception as e:
        print(f"❌ Error launching app: {e}")
        print("   Try running manually: python3 hello_world_rickroll.py")

def main():
    """Main setup function"""
    print_banner()
    
    # Step 1: Check Python version
    if not check_python_version():
        input("\nPress Enter to exit...")
        return False
    
    # Step 2: Show system info
    get_system_info()
    
    # Step 3: Check files
    if not check_required_files():
        input("\nPress Enter to exit...")
        return False
    
    # Step 4: Install dependencies
    if not install_dependencies():
        print("\n💡 If installation failed, try running manually:")
        print("   pip3 install pygame pillow mido")
        input("\nPress Enter to exit...")
        return False
    
    # Step 5: Launch app
    run_app()
    
    print("\n" + "="*60)
    print("🎵 NEVER GONNA GIVE YOU UP, NEVER GONNA LET YOU DOWN! 🎵")
    print("="*60)
    
    return True

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Setup cancelled by user. Goodbye!")
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        print("Please report this issue if it persists.")
    
    # Keep window open on Windows
    if platform.system() == "Windows":
        input("\nPress Enter to close...")
