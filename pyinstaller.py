import PyInstaller.__main__

PyInstaller.__main__.run([
    'bridge.py',
    '--onefile',
    '--windowed',
    '--add-data', 'config.json:config.json',
    '--name', 'titrek-bridge'
])
