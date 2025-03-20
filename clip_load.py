from moviepy.editor import VideoFileClip, CompositeVideoClip

# 加载两个视频文件
clip1 = VideoFileClip("output-2.mp4", has_mask=True)

print(clip1.duration)
print(clip1.fps)
print(clip1.size)



# clip1_10 = clip1.subclip(0, 10)
# clip1_10.write_videofile("o1.mp4")


# # 释放资源
clip1.close()
