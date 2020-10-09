# ffmpeg -i video.m4s -i audio.m4s -codec copy outname.mp4
# 上面是ffmpeg 合并 视频和声音的 命令

import shutil
import os
import json

# 合并
files = os.listdir()
for file in files:
	if os.path.isdir(file):
		os.chdir('./'  + file)
		with open('./entry.json','r', encoding='UTF-8') as f:
			data = json.load(f)
			title = data['page_data']['part']
		os.chdir('./80')
		temp = (str(title) + '.mp4').replace(' ','-')		
		os.system('ffmpeg -i video.m4s -i audio.m4s -codec copy '+temp)
		os.system('move '+ temp+ ' ../../')
		os.chdir('../')
		os.chdir('../')

#删除文件夹
files = os.listdir()
for file in files:
	if os.path.isdir(file):
		#删除文件夹需要用到shutil 库
		shutil.rmtree(file)
