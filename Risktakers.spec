# -*- mode: python ; coding: utf-8 -*-
import os
import shutil
import sys
def get_levels_data():
    levels_data = []
    for filename in os.listdir('levels'):
        if filename.endswith('.py'):
            levels_data.append((os.path.join('levels', filename), 'levels'))
    return levels_data
def get_images_data():
    images_data = []
    for filename in os.listdir('pictures'):
        if filename.endswith('.jpg'):
            images_data.append((os.path.join('pictures', filename), 'pictures'))
    return images_data
def get_sounds_data():
    sounds_data = []
    for filename in os.listdir('sounds'):
        if filename.endswith('.mp3') or filename.endswith('wav'):
            sounds_data.append((os.path.join('sounds', filename), 'sounds'))
    return sounds_data

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas= get_levels_data() + get_images_data() + get_sounds_data(),
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=None)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='Risktakers',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='C:\\Users\\HP\\Desktop\\MyGame1\\pythonProject1\\Risktakers.ico'
)



