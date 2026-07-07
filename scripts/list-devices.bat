@echo off

echo.
echo  ===================================
echo   Video and Audio Devices
echo  ===================================
echo.

set "FFMPEG=ffmpeg"
where %FFMPEG% >nul 2>&1
if errorlevel 1 (
    set "FFMPEG=C:\ffmpeg\bin\ffmpeg.exe"
    if not exist "%FFMPEG%" (
        echo  ERROR: FFmpeg not found!
        echo  Download from: https://www.gyan.dev/ffmpeg/builds/
        pause
        exit /b 1
    )
)

%FFMPEG% -list_devices true -f dshow -i dummy 2>&1
echo.
echo  ===================================
echo   Find your intercom name above
echo  ===================================
echo.
pause
