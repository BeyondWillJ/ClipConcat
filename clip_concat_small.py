from moviepy.editor import VideoFileClip, CompositeVideoClip
import time
import os

def clip_concat(file1, file2, ofile,alpha=0.6):
    # ffmpeg -i 计算方法_2024_04_09_08_00.mp4 -c:v libx264 -r 20 -c:a aac -b:a 256k output-1.mp4
    # 加载两个视频文件
    clip1 = VideoFileClip(file1)
    clip2 = VideoFileClip(file2)

    # 将 clip2 缩小至原来大小的 50% 并移除其音频
    clip2_resized = clip2.resize(alpha).set_audio(None)

    # 将缩小后的 clip2 叠加在 clip1 的中心
    final_clip = CompositeVideoClip([
        clip1,
        clip2_resized.set_position(("center", "bottom"))
    ])


    start_time = time.time()
    # 输出最终视频，指定视频和音频编码
    orig_write = final_clip.write_videofile
    final_clip.write_videofile(ofile, codec='libx264', preset='ultrafast')

    end_time = time.time()
    total_seconds = end_time - start_time
    hours = int(total_seconds // 3600)
    minutes = int((total_seconds % 3600) // 60)
    seconds = total_seconds % 60
    print("处理总耗时: {}时 {}分 {:.2f}秒。".format(hours, minutes, seconds))

    with open("timelog.txt", "a+", encoding="utf-8") as log_file:
        log_file.write("开始时间: {} ".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(start_time))))
        log_file.write("结束时间: {}\n".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(end_time))))
        log_file.write(f"{file1} + {file2} -> {ofile} 处理总耗时: {end_time - start_time:.2f} 秒\n\n")

    # 释放资源
    clip1.close()
    clip2.close()
    final_clip.close()


file1 = "output-1.mp4"
file2 = "output-2.mp4"
ofile = "FFoutput-2.mp4"
# ffmpeg -i 计算方法_2024_04_09_08_00.mp4 -r 30 -c:v libx264 -preset fast -crf 23 -c:a aac -b:a 128k output.mp4

# ffmpeg -i 计算方法_2024_04_09_08_00.mp4 -c:v libx264 -r 20 -c:a copy output-1.mp4

clip_concat(file1, file2, ofile, alpha=0.6)