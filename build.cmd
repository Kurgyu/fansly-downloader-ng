@echo off

rem Build "Fansly Downloader NG.exe"
pyinstaller ^
    -n "Fansly Downloader NG" ^
    --onefile ^
    --windowed ^
    --noupx ^
    --icon=resources\fansly_ng.ico ^
    fansly_downloader_ng.py
