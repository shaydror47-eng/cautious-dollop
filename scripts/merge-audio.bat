@echo off
chcp 65001 >nul
setlocal enabledelayedexpansion

REM ═══════════════════════════════════════════════════════════════
REM   סקריפט מיזוג שמע - וידאו מהמצלמה + שמע מהדיבורית
REM   שימוש: גרור קובץ וידאו + קובץ שמע על הסקריפט
REM   או: שים את הקבצים בתיקיית input והפעל
REM ═══════════════════════════════════════════════════════════════

set "FFMPEG=ffmpeg"

REM --- בדיקה ש-FFmpeg מותקן ---
where %FFMPEG% >nul 2>&1
if errorlevel 1 (
    set "FFMPEG=C:\ffmpeg\bin\ffmpeg.exe"
    if not exist "!FFMPEG!" (
        echo.
        echo  FFmpeg לא נמצא!
        echo  הורד מ: https://www.gyan.dev/ffmpeg/builds/
        echo  חלץ ל: C:\ffmpeg\
        echo.
        pause
        exit /b 1
    )
)

REM --- מצב גרירה: 2 קבצים ---
if not "%~2"=="" (
    set "VIDEO=%~1"
    set "AUDIO=%~2"
    goto :merge
)

REM --- מצב תיקייה: חיפוש בתיקיית input ---
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
    echo  לא נמצא קובץ וידאו בתיקיית input\
    echo  שים את קובץ הוידאו מהמצלמה ^(mp4/mov/avi/mkv^)
    echo  ואת קובץ השמע מהדיבורית ^(webm/wav/m4a^)
    echo  בתיקיית input\ והפעל שוב
    echo.
    pause
    exit /b 1
)
if not defined AUDIO (
    echo.
    echo  לא נמצא קובץ שמע בתיקיית input\
    echo  שים את קובץ השמע מהדיבורית ^(webm/wav/m4a^)
    echo  בתיקיית input\
    echo.
    pause
    exit /b 1
)

:merge
echo.
echo  ════════════════════════════════════════
echo   מיזוג וידאו + שמע מדיבורית
echo  ════════════════════════════════════════
echo.
echo  וידאו: %VIDEO%
echo  שמע:   %AUDIO%
echo.

if not exist "output" mkdir output

REM --- יצירת שם קובץ עם תאריך ---
for /f "tokens=1-3 delims=/ " %%a in ("%date%") do set "D=%%c-%%b-%%a"
for /f "tokens=1-2 delims=:." %%a in ("%time: =0%") do set "T=%%a-%%b"
set "OUTPUT=output\ride_%D%_%T%.mp4"

echo  פלט: %OUTPUT%
echo.
echo  ממזג... (הוידאו לא מקודד מחדש - מהיר)
echo.

%FFMPEG% -i "%VIDEO%" -i "%AUDIO%" -c:v copy -c:a aac -map 0:v:0 -map 1:a:0 -shortest -y "%OUTPUT%"

if errorlevel 1 (
    echo.
    echo  שגיאה במיזוג! בדוק שהקבצים תקינים.
    pause
    exit /b 1
)

echo.
echo  ════════════════════════════════════════
echo   המיזוג הושלם!
echo   הקובץ נשמר ב: %OUTPUT%
echo  ════════════════════════════════════════
echo.
pause
