# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

binaries = [
   ('C:\\Windows\\System32\\libusb0.dll', '.'),
]

a = Analysis(['JoeyKeyGen.py'],
             pathex=['D:\\OneDrive\\Dokumenter\\GitHub\\JoeyKeygen'],
             binaries=binaries,
             datas=[],
             hiddenimports=['usb'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='JoeyKeyGen',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=['vcruntime140.dll'],
          runtime_tmpdir=None,
          console=True , icon='Key.ico')
