import os
import time
from pymediainfo import MediaInfo

path = './cls'
files = os.listdir(path)
namename = '计算方法'

def makename(path, namename):
    for file in files:
        p=os.path.join(path, file)
        ctime = MediaInfo.parse(p).to_data()['tracks'][0]['encoded_date']
        dtime=time.strptime(ctime,"%Y-%m-%d %H:%M:%S UTC")
        timename=time.strftime(f"{namename}_%Y_%m_%d_%H_%M",time.localtime(time.mktime(dtime)+28800))
        os.rename(p, os.path.join(path, timename+'_ppt.mp4'))
        print(f'{file} -> {timename}.mp4')

makename('./cls', namename)
makename('./ppt', namename)
