
import urllib.request
# from bs4 import BeautifulSoup 
import re
import sys
#图片处理库
from PIL import Image 
import win32gui,win32con,win32api

import os


#windows API
def set_wallpaper(picpath):
    if sys.platform == 'win32':
        import win32api, win32con, win32gui
        k = win32api.RegOpenKey(win32con.HKEY_CURRENT_USER, 'Control Panel\Desktop', 0, win32con.KEY_ALL_ACCESS)
        curpath = win32api.RegQueryValueEx(k, 'Wallpaper')[0]
        if curpath == picpath:
            pass
        else:
            # win32api.RegSetValueEx(k, "WallpaperStyle", 0, win32con.REG_SZ, "2")#2 for tile,0 for center
            # win32api.RegSetValueEx(k, "TileWallpaper", 0, win32con.REG_SZ, "0")
            win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, picpath, 1+2)
        win32api.RegCloseKey(k)
    else:
        curpath = commands.getstatusoutput('gsettings get org.gnome.desktop.background picture-uri')[1][1:-1]
        if curpath == picpath:
            pass
        else:
            commands.getstatusoutput('DISPLAY=:0 gsettings set org.gnome.desktop.background picture-uri "%s"' % (picpath))

def setWallpaperFromBMP(imagepath):
    k = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER,"Control Panel\Desktop",0,win32con.KEY_SET_VALUE)
    win32api.RegSetValueEx(k, "WallpaperStyle", 0, win32con.REG_SZ, "2") #2拉伸适应桌面,0桌面居中
    win32api.RegSetValueEx(k, "TileWallpaper", 0, win32con.REG_SZ, "0")
    win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER,imagepath, 1+2)



#链接到http://cn.bing.com/?mkt=zh-CN&mkt=zh-CN&mkt=zh-CN&mkt=zh-CN   获取图片地址
def fun(path):

    # path = "H:\\BingWallpaper"
    # bmpPath = r'H:\bingWallpaper.bmp'
    # jpgPath = r'H:\bingWallpaper.jpg'

    try:
        html = urllib.request.urlopen(r'https://www.bing.com/?scope=web&FORM=MOZSBR&pc=MOZI')
        data = html.read()
        #soup = BeautifulSoup(data,'html.parser');
    except:
        print('ex')
    else:
        # 图片地址 http://s.cn.bing.net/az/hprichbg/rb/PinnaclesNP_ZH-CN9665317661_1920x1080.jpg
        # 前缀 http://www.bing.com
        # g_img={url: "/az/hprichbg/rb/SnowdoniaAlgae_ROW16437623621_1920x1080.jpg"
        ## change in 2019.3.11
        ## 图片地址 https://cn.bing.com/th?id=OHR.BagpipeOpera_EN-CN1622009392_1920x1080.jpg&rf=NorthMale_1920x1080.jpg&pid=hp
        ## 位置 heads
        ## <link id="bgLink" rel="preload" href="/th?id=OHR.BagpipeOpera_EN-CN1622009392_1920x1080.jpg&amp;rf=NorthMale_1920x1080.jpg&amp;pid=hp" as="image">
        data = str(data)

        # 搜索图片的链接
        # pattern = re.compile('g_img=\{.+?,')
        pattern = re.compile('<link id=\"bgLink\" .+?/>')

        imgUrl = re.findall(pattern,data)
        # <class 'list'>: ['<link id="bgLink" rel="preload" href="/th?id=OHR.LeopardNamibia_ZH-CN9585068449_1920x1080.jpg&amp;rf=NorthMale_1920x1080.jpg&amp;pid=hp" as="image" />']
        # print(imgUrl)

        if imgUrl:
            # 通过图片地址对图片进行命名
            link = re.findall(re.compile("\".+?\""),imgUrl[0])
            # 去除前缀
            imgUrl = r'https://cn.bing.com' + link[2].strip('\"')
            # https://cn.bing.com/th?id=OHR.BagpipeOpera_EN-CN1622009392_1920x1080.jpg

            # 取图片名称
            imgNameandType = link[2].split('=')
            # <class 'list'>: ['"/th?id', 'OHR.LeopardNamibia_ZH-CN9585068449_1920x1080.jpg&amp;rf', 'NorthMale_1920x1080.jpg&amp;pid', 'hp"']

            # 去除图片名称的多余文本
            imgNameandType = imgNameandType[1].split("&")[0]
            # MoscowSkyline_ZH-CN10266976296_1920x1080.jpg

            # 分割图片的文件名和文件格式
            imgName = imgNameandType.split('.')
            # ['MoscowSkyline_ZH-CN10266976296_1920x1080', 'jpg']
            imgType = imgName[-1]
            imgName = imgName[1]

            # 组装图片的路径和转化为bmp文件后的路径
            imgPath  = os.path.join(path,"wallpaper",imgName)
            imgPath = imgPath+"."+imgType
            # H:\BingWallpaper\wallpaper\MoscowSkyline_ZH-CN10266976296_1920x1080.jpg

            bmpPath = os.path.join(path,"BMPImage",imgName)
            bmpPath = bmpPath+".bmp"
            # H:\BingWallpaper\BMPImage\MoscowSkyline_ZH-CN10266976296_1920x1080.bmp

            # 保存图片到本地指定目录
            try:
                imgBit = urllib.request.urlopen(imgUrl)
            except:
                print(sys.exc_info())
                print('No picture!')
            else:
                # 保存图片
                file = open(imgPath,'wb')
                file.write(imgBit.read())
                file.close()
                # 转换图片格式为bmp
                img = Image.open(imgPath)
                img.save(bmpPath)

                # 将获取到的图片设置为桌面背景
                set_wallpaper(bmpPath)
                print("Set wallpaper succeed!")
        else:
            print("Don't find image link!")

def checkDirExists(path):
    if not os.path.exists(path):
        os.makedirs(path)
        print("文件夹创建成功")
    else:
        print("目录已存在")

if __name__ == "__main__":
    # 获取当前文件所在目录
    pyPath =  os.path.dirname(os.path.realpath(__file__))
    path = pyPath+"\BingWallpaper"
    # print(open("H:/BingWallpaper/test/testpic_1",'wb'))
    checkDirExists(path+"\BMPImage")
    checkDirExists(path+"\wallpaper")
    fun(path)


