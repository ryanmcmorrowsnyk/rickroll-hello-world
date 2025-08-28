#!/usr/bin/env python3
"""
Build Executable Script for Rick Roll Hello World
Creates standalone executables for different platforms using PyInstaller
"""

import os
import sys
import subprocess
import shutil
import platform

def print_banner():
    """Print build banner"""
    print("=" * 60)
    print("🚀 RICK ROLL HELLO WORLD - EXECUTABLE BUILDER 🚀")
    print("=" * 60)

def check_pyinstaller():
    """Check if PyInstaller is installed"""
    try:
        import PyInstaller
        print("✅ PyInstaller is available")
        return True
    except ImportError:
        print("❌ PyInstaller not found")
        print("Installing PyInstaller...")
        
        try:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pyinstaller'])
            print("✅ PyInstaller installed successfully")
            return True
        except subprocess.CalledProcessError:
            print("❌ Failed to install PyInstaller")
            return False

def create_spec_file():
    """Create PyInstaller spec file for custom build"""
    spec_content = '''# -*- mode: python ; coding: utf-8 -*-

a = Analysis(
    ['hello_world_rickroll.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('never_gonna_give_you_up.mid', '.'),
        ('never_gonna_give_you_up_trimmed.mid', '.'),
        ('rick_astley_8bit_dancing.gif', '.'),
        ('README.md', '.'),
        ('LICENSE_NOTICE.md', '.'),
    ],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='RickRollHelloWorld',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=None,
)
'''
    
    with open('rickroll.spec', 'w') as f:
        f.write(spec_content)
    
    print("✅ Created rickroll.spec file")

def build_executable():
    """Build the executable"""
    print("\n🔨 Building executable...")
    
    try:
        # Create spec file
        create_spec_file()
        
        # Build executable
        cmd = [
            sys.executable, '-m', 'PyInstaller',
            '--clean',
            '--noconfirm',
            'rickroll.spec'
        ]
        
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            print("✅ Executable built successfully!")
            
            # Find the executable
            dist_dir = 'dist'
            if os.path.exists(dist_dir):
                exe_files = []
                for file in os.listdir(dist_dir):
                    file_path = os.path.join(dist_dir, file)
                    if os.path.isfile(file_path):
                        exe_files.append(file_path)
                
                if exe_files:
                    print(f"\n📦 Executable created:")
                    for exe in exe_files:
                        size = os.path.getsize(exe) / (1024 * 1024)
                        print(f"   {exe} ({size:.1f} MB)")
                    
                    return exe_files[0]  # Return path to main executable
            
        else:
            print("❌ Build failed:")
            print(result.stderr)
            return None
            
    except Exception as e:
        print(f"❌ Build error: {e}")
        return None

def create_distribution_package():
    """Create a distribution package for friends"""
    print("\n📦 Creating distribution package...")
    
    package_name = f"RickRollHelloWorld_{platform.system()}_{platform.machine()}"
    package_dir = f"dist/{package_name}"
    
    # Create package directory
    os.makedirs(package_dir, exist_ok=True)
    
    # Copy executable
    if platform.system() == "Windows":
        exe_name = "RickRollHelloWorld.exe"
    else:
        exe_name = "RickRollHelloWorld"
    
    exe_path = f"dist/{exe_name}"
    if os.path.exists(exe_path):
        shutil.copy2(exe_path, package_dir)
    
    # Copy documentation
    docs = ['README.md', 'LICENSE_NOTICE.md']
    for doc in docs:
        if os.path.exists(doc):
            shutil.copy2(doc, package_dir)
    
    # Create instructions
    instructions = f"""# Rick Roll Hello World - Ready to Share! 🎵

## How to Run
Simply double-click the `{exe_name}` file!

## What It Does
- Opens a "Hello World" window
- Click the red "World" text to get rickrolled!
- Features dancing 8-bit Rick Astley and MIDI music
- Click "World" again to stop

## System Requirements
- {platform.system()} {platform.machine()}
- No additional software needed!

## Sharing
Send this entire folder to your friends to rickroll them!

---
Never gonna give you up! 🎶
"""
    
    with open(f"{package_dir}/HOW_TO_RUN.txt", "w") as f:
        f.write(instructions)
    
    print(f"✅ Distribution package created: {package_dir}/")
    
    # Create zip file for easy sharing
    try:
        shutil.make_archive(package_name, 'zip', 'dist', package_name)
        zip_size = os.path.getsize(f"{package_name}.zip") / (1024 * 1024)
        print(f"✅ ZIP file created: {package_name}.zip ({zip_size:.1f} MB)")
        print(f"\n🎉 Ready to share! Send '{package_name}.zip' to your friends!")
    except Exception as e:
        print(f"⚠️  Could not create ZIP: {e}")
        print(f"   Share the folder '{package_dir}/' instead")

def main():
    """Main build function"""
    print_banner()
    
    # Check PyInstaller
    if not check_pyinstaller():
        return False
    
    # Build executable
    exe_path = build_executable()
    if not exe_path:
        return False
    
    # Create distribution package
    create_distribution_package()
    
    print("\n" + "=" * 60)
    print("🎵 BUILD COMPLETE - READY TO RICKROLL THE WORLD! 🎵")
    print("=" * 60)
    
    return True

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Build cancelled by user.")
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
    
    input("\nPress Enter to close...")
