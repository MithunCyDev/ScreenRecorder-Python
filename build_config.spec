# -*- mode: python ; coding: utf-8 -*-

import sys
from pathlib import Path

block_cipher = None

# Determine the correct path separator
sep = '\\' if sys.platform == 'win32' else '/'

a = Analysis(
    ['main.py'],
    pathex=[str(Path.cwd())],  # Use current working directory
    binaries=[],
    datas=[],
    hiddenimports=[
        'moviepy',
        'moviepy.editor',
        'moviepy.video.io.ffmpeg_tools',
        'sounddevice',
        'soundfile',
        'cv2',
        'numpy',
        'pyautogui',
        'PIL',
        'PIL._tkinter_finder'
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='ScreenRecorder',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='icon.ico' if Path('icon.ico').exists() else None
)