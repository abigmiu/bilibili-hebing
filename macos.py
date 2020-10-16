#用于macos
#pip3 install applescript
import applescript
import shutil
import os
import json

# 合并
files = os.listdir()
for file in files:
    #is video
    if os.path.isdir(file):
        path = os.path.abspath(file)
        #这是获取标题的，每个视频的标题格式可能不一样，注意自己写
        with open(path + '/entry.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
            title = data['page_data']['part']
        #print(path)
        #print(title)
        commend = 'ffmpeg -i '+ path + '/80/video.m4s -i '+ path + '/80/audio.m4s -codec copy ' + path + title+'.mp4'
        #print(commend)
        applescript.tell.app("Terminal",'do script "'+commend+'"')
		
