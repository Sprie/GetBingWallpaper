# GetBingWallpaper
享受网络上美丽的壁纸吧~

## getBingWallpaper与getBingWallpaper-notSavePic的区别

getBingWallpaper会把每次获取的图片 **保存** 起来，而getBingWallpaper-notSavePic在设置完壁纸后就会将图片删除，**不保存** 图片，从而节省磁盘空间。

### 自动更新壁纸教程
1. 将getBingWallpaper.exe或getBingWallpaper-notSavePic.exe下载下来。
右键桌面我的电脑点击管理。

2. 选择 系统工具->任务计划程序->任务计划程序库 右键任务计划程序库，选择创建基本任务或创建任务，这里以创建基本任务为例。

3. 名称和描述可以随意填写，填完点击下一步。

4. 选择任务开始的时间，可以按天开始，也可以在计算机启动时开始都可以。这里选择按天开始。点击下一步。

5. 填上每天的开始时间（最好不要设置为00:00:00）。下一步。

6. 选择启动程序，点击浏览。将下载下来的getBingWallpaper.exe文件选中，确定，点击下一步。

7. 勾选下 "当点击完成时，打开属性。。"  因为还有一个条件需要设置。

8. 选中打开的属性中的条件，把网络下的选项勾选。因为获取图片需要联网，所以我们设置程序只在联网状态下启动。

9. 最后，点击条件旁边的设置，勾选“如果过了计划开始时间，立刻启动任务“，这样就不怕程序消极怠工不运行啦，最后点击确定就完成啦。

### 手动更新壁纸教程
如果不需要每天程序自动启动，只想需要的时候更换下壁纸，那只需要把getBingWallpaper.exe或getBingWallpaper-notSavePic.exe下载下来，需要时点击然后稍等一会就可以了。

测试系统：Windows 10

## 提示:

.exe文件仅支持64位操作系统，.py文件可以自己在32位电脑上打包成.exe文件。

本程序使用PyInstaller打包（`pyinstaller -F -w **.py`)。
