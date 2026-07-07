@echo off
setlocal enabledelayedexpansion

REM ===================================================
REM   Merge Audio - Camera video + Intercom audio
REM   Drag video + audio files onto this script
REM   OR put files in input\ folder and run
REM ===================================================

set "FFMPEG=ffmpeg"

where %FFMPEG% >nul 2>&1
if errorlevel 1 (
    set "FFMPEG=C:\ffmpeg\bin\ffmpeg.exe"
    if not exist "!FFMPEG!" (
        echo.
        echo  ERROR: FFmpeg not found!
        echo  Download from: https://www.gyan.dev/ffmpeg/builds/
        echo  Extract to: C:\ffmpeg\
        echo.
        pause
        exit /b 1
    )
)

REM --- Drag and drop mode: 2 files ---
if not "%~2"=="" (
    set "VIDEO=%~1"
    set "AUDIO=%~2"
    goto :merge
)

REM --- Folder mode: look in input\ ---
if not exist "input" mkdir input
if not exist "output" mkdir output

set VIDEO=
set AUDIO=

for %%f in (input\*.mp4 input\*.mov input\*.avi input\*.mkv) do (
    if not defined VIDEO set "VIDEO=%%f"
)
for %%f in (input\*.webm input\*.wav input\*.m4a input\*.ogg input\*.aac) do (
    if not defined AUDIO set "AUDIO=%%f"
)

if not defined VIDEO (
    echo.
    echo  No video file found in input\ folder
    echo  Put camera video file (mp4/mov/avi/mkv)
    echo  and intercom audio file (webm/wav/m4a)
    echo  in the input\ folder and run again
    echo.
    pause
    exit /b 1
)
if not defined AUDIO (
    echo.
    echo  No audio file found in input\ folder
    echo  Put intercom audio file (webm/wav/m4a)
    echo  in the input\ folder
    echo.
    pause
    exit /b 1
)

:merge
echo.
echo  ===================================
echo   Merge Video + Intercom Audio
echo  ===================================
echo.
echo  Video: %VIDEO%
echo  Audio: %AUDIO%
echo.

if not exist "output" mkdir output

for /f "tokens=1-3 delims=/ " %%a in ("%date%") do set "D=%%c-%%b-%%a"
for /f "tokens=1-2 delims=:." %%a in ("%time: =0%") do set "T=%%a-%%b"
set "OUTPUT=output\ride_%D%_%T%.mp4"

echo  Output: %OUTPUT%
echo.
echo  Merging... (video not re-encoded - fast)
echo.

%FFMPEG% -i "%VIDEO%" -i "%AUDIO%" -c:v copy -c:a aac -map 0:v:0 -map 1:a:0 -shortest -y "%OUTPUT%"

if errorlevel 1 (
    echo.
    echo  ERROR: Merge failed! Check that files are valid.
    pause
    exit /b 1
)

echo.
echo  ===================================
echo   Merge complete!
echo   Saved to: %OUTPUT%
echo  ===================================
echo.
pause
