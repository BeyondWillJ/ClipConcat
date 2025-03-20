from moviepy.editor import VideoFileClip, CompositeVideoClip

# 加载两个视频文件
clip1 = VideoFileClip("计算方法_2024_04_09_08_00~2.mp4")
clip2 = VideoFileClip("计算方法_2024_04_09_08_00_ppt~2.mp4")




clip1_10 = clip1.subclip(0, 10)
clip2_10 = clip2.subclip(0, 10)
clip1_10.write_videofile("o1.mp4")
clip2_10.write_videofile("o2.mp4")
final_clip = CompositeVideoClip([clip1_10, clip2_10])

# 释放资源
clip1.close()
clip2.close()
final_clip.close()