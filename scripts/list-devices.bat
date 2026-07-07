@echo off
chcp 65001 >nul

echo.
echo  ═══════════════════════════════════
echo   רשימת מכשירי וידאו ושמע
echo  ═══════════════════════════════════
echo.

set "FFMPEG=ffmpeg"
where %FFMPEG% >nul 2>&1
if errorlevel 1 (
    set "FFMPEG=C:\ffmpeg\bin\ffmpeg.exe"
    if not exist "!FFMPEG!" (
        echo  FFmpeg לא נמצא!
        echo  הורד מ: https://www.gyan.dev/ffmpeg/builds/
        pause
        exit /b 1
    )
)

%FFMPEG% -list_devices true -f dshow -i dummy 2>&1
echo.
echo  ═══════════════════════════════════
echo   חפש את שם הדיבורית ברשימה למעלה
echo  ═══════════════════════════════════
echo.
pause
