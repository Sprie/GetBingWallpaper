
import urllib.request
# from bs4 import BeautifulSoup 
import re
import sys
import win32gui,win32con,win32api
#图片处理库
from PIL import Image 


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

# def setWallpaperFromBMP(imagepath):
    # k = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER,"Control Panel\Desktop",0,win32con.KEY_SET_VALUE)
    # win32api.RegSetValueEx(k, "WallpaperStyle", 0, win32con.REG_SZ, "2") #2拉伸适应桌面,0桌面居中
    # win32api.RegSetValueEx(k, "TileWallpaper", 0, win32con.REG_SZ, "0")
    # win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER,imagepath, 1+2)



#链接到http://cn.bing.com/?mkt=zh-CN&mkt=zh-CN&mkt=zh-CN&mkt=zh-CN   获取图片地址
def fun():

	bmpPath = r'H:\bingWallpaper.bmp'
	jpgPath = r'H:\bingWallpaper.jpg'

	try:
		html = urllib.request.urlopen(r'http://cn.bing.com/?mkt=zh-CN&mkt=zh-CN&mkt=zh-CN&mkt=zh-CN');
		data = html.read();
		#soup = BeautifulSoup(data,'html.parser');
	except:
		print('ex');
	else:
		#图片地址 http://s.cn.bing.net/az/hprichbg/rb/PinnaclesNP_ZH-CN9665317661_1920x1080.jpg
		#print(soup.find(re.compile("http://s.cn.bing.net/.+/.+/.+/.+\..+")))
		#print(soup.find("style"))
		#temp = soup.text()
		#temp = soup.find_all("style")
		#print(temp)
		
		# file = open(r'H:\2.txt','w')
		# file.write(str(data))
		# file.close
		data = str(data)
		#print(data)
		pattern = re.compile(r'http://[^"]+\.jpg');
		# pattern = re.compile(r'bing.net');
		#pattern = re.compile(r"a")
		imgUrl = pattern.search(data)
		if imgUrl:
			# print(imgUrl.group())
			# 保存图片到本地指定目录
			try:
				imgBit = urllib.request.urlopen(str(imgUrl.group()))
			except:
				print('no picture')
			else:
				# 保存图片
				file = open(jpgPath,'wb')
				file.write(imgBit.read())
				file.close()
				# 转换图片格式为bmp
				img = Image.open(jpgPath)
				img.save(bmpPath)
				
			# 将获取到的图片设置为桌面背景
			set_wallpaper(bmpPath)
			
		else:
			print("null")
		
		
			
if __name__ == "__main__":
	
	fun();


