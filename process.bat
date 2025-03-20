@echo off
REM 如果output文件夹不存在则创建
if not exist outputcls mkdir outputcls
if not exist outputppt mkdir outputppt

REM 遍历当前目录所有mp4文件
for %%f in (cls\*.mp4) do (
    echo 正在处理： %%f
    @REM ffmpeg -i "%%f" -c copy "output\%%~nxf"
    ffmpeg -i "%%f" -c:v libx264 -preset ultrafast -r 20 -c:a copy -progress pipe:1 "outputcls\%%~nxf"
)

REM 遍历当前目录所有ppt文件
for %%f in (ppt\*.mp4) do (
    echo 正在处理： %%f
    @REM ffmpeg -i "%%f" -c copy "output\%%~nxf"
    ffmpeg -i "%%f" -c:v libx264 -preset ultrafast -r 20 -c:a copy -progress pipe:1 "outputppt\%%~nxf"
)

echo.
echo 所有文件处理完成！
pause