@echo off
setlocal enabledelayedexpansion

REM ===================================================
REM   Merge Video + Audio
REM   Drag both files onto this script
REM   OR put them in the "input" folder and run
REM ===================================================

set "FFMPEG=ffmpeg"
where %FFMPEG% >nul 2>&1
if errorlevel 1 (
    set "FFMPEG=C:\ffmpeg\bin\ffmpeg.exe"
    if not exist "!FFMPEG!" (
        echo.
        echo  [ERROR] FFmpeg not found!
        echo.
        echo  Download: https://www.gyan.dev/ffmpeg/builds/
        echo  Pick: ffmpeg-release-essentials.zip
        echo  Extract to: C:\ffmpeg\
        echo.
        pause
        exit /b 1
    )
)

if not "%~2"=="" (
    set "FILE1=%~1"
    set "FILE2=%~2"

    set "VIDEO="
    set "AUDIO="

    for %%e in (.mp4 .mov .avi .mkv) do (
        if /i "%~x1"=="%%e" set "VIDEO=%~1"
        if /i "%~x2"=="%%e" set "VIDEO=%~2"
    )
    for %%e in (.webm .wav .m4a .ogg .aac .mp3) do (
        if /i "%~x1"=="%%e" set "AUDIO=%~1"
        if /i "%~x2"=="%%e" set "AUDIO=%~2"
    )

    if not defined VIDEO (
        echo  [ERROR] No video file found. Drag a video + audio file.
        pause
        exit /b 1
    )
    if not defined AUDIO (
        echo  [ERROR] No audio file found. Drag a video + audio file.
        pause
        exit /b 1
    )
    goto :merge
)

if not exist "input" mkdir input
set VIDEO=
set AUDIO=
for %%f in (input\*.mp4 input\*.mov input\*.avi input\*.mkv) do (
    if not defined VIDEO set "VIDEO=%%f"
)
for %%f in (input\*.webm input\*.wav input\*.m4a input\*.ogg input\*.aac input\*.mp3) do (
    if not defined AUDIO set "AUDIO=%%f"
)

if not defined VIDEO (
    echo.
    echo  No video file in input\ folder.
    echo  Put camera video (mp4/mov) + audio file (m4a/wav/webm)
    echo  in the input\ folder, then run again.
    echo.
    echo  OR drag both files onto this script.
    echo.
    pause
    exit /b 1
)
if not defined AUDIO (
    echo.
    echo  No audio file in input\ folder.
    echo  Put the audio recording (m4a/wav/webm) in input\
    echo.
    pause
    exit /b 1
)

:merge
echo.
echo  ===================================
echo   Merging Video + Intercom Audio
echo  ===================================
echo.
echo  Video: %VIDEO%
echo  Audio: %AUDIO%

if not exist "output" mkdir output

for /f "tokens=2 delims==" %%I in ('wmic os get localdatetime /value') do set "DT=%%I"
set "TIMESTAMP=%DT:~0,4%-%DT:~4,2%-%DT:~6,2%_%DT:~8,2%-%DT:~10,2%"
set "OUTPUT=output\ride_%TIMESTAMP%.mp4"

echo  Output: %OUTPUT%
echo.
echo  Working...
echo.

%FFMPEG% -i "%VIDEO%" -i "%AUDIO%" -c:v copy -c:a aac -b:a 192k -map 0:v:0 -map 1:a:0 -shortest -y "%OUTPUT%"

if errorlevel 1 (
    echo.
    echo  [ERROR] Merge failed. Check that both files are valid.
    pause
    exit /b 1
)

echo.
echo  ===================================
echo   Done! Saved: %OUTPUT%
echo  ===================================
echo.
pause
