import cv2
import os
import numpy as np
from tqdm import tqdm

## 从视频中提取幻灯片图片
# 文件路径
path0 = r"test.mp4"




def mse(imageA, imageB):    # 定义均方误差（MSE）函数，计算两张图片的差异
    err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)  # 计算像素差的平方和
    err /= float(imageA.shape[0] * imageA.shape[1])   # 除以总像素数，得到平均误差
    return err              # 返回误差值

def extract_slides(video_path, output_folder, threshold=500, resize_factor=0.25, skip_frames=5):
    # 定义函数：从视频中提取幻灯片图片
    if not os.path.exists(output_folder):     # 如果输出文件夹不存在
        os.makedirs(output_folder)            # 创建输出文件夹
    
    cap = cv2.VideoCapture(video_path)        # 打开视频文件
    if not cap.isOpened():                    # 如果视频无法打开
        print("无法打开视频文件")              # 输出错误信息
        return                                # 结束函数
    
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))  # 获取视频总帧数
    ret, frame = cap.read()                   # 读取第一帧
    if not ret:                               # 如果读取失败
        print("无法读取视频")                 # 输出错误信息
        return                                # 结束函数
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)         # 将第一帧转为灰度图
    small_gray = cv2.resize(gray, (0,0), fx=resize_factor, fy=resize_factor)  # 缩小图片尺寸
    
    slide_count = 1                           # 初始化幻灯片计数
    cv2.imwrite(os.path.join(output_folder, f"slide_{slide_count}.jpg"), frame)  # 保存第一帧为第一张幻灯片
    last_small_gray = small_gray              # 保存上一张幻灯片的灰度缩略图
    
    frame_count = 0                           # 初始化帧计数
    with tqdm(total=total_frames, desc="Processing Video") as pbar:  # 创建进度条
        while True:                           # 循环读取视频帧
            ret, frame = cap.read()           # 读取下一帧
            if not ret:                       # 如果读取失败
                break                         # 跳出循环
            frame_count += 1                  # 帧计数加一
            if frame_count % skip_frames != 0:    # 跳过部分帧，加快处理速度
                pbar.update(1)                # 更新进度条
                continue                      # 跳到下次循环
            
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)         # 当前帧转为灰度图
            small_gray = cv2.resize(gray, (0,0), fx=resize_factor, fy=resize_factor)  # 缩小图片
            
            similarity = mse(last_small_gray, small_gray)          # 计算与上一张幻灯片的差异
            if similarity > threshold:                             # 如果差异大于阈值，认为是新幻灯片
                slide_count += 1                                   # 幻灯片计数加一
                cv2.imwrite(os.path.join(output_folder, f"slide_{slide_count}.jpg"), frame)  # 保存当前帧
                last_small_gray = small_gray                       # 更新上一张幻灯片
            pbar.update(skip_frames)                               # 更新进度条
        
    cap.release()                              # 释放视频资源
    print(f"共提取 {slide_count} 张幻灯片。")   # 输出提取结果

if __name__ == "__main__":                     # 如果作为主程序运行
    video_path = path0
    video_name = os.path.splitext(os.path.basename(video_path))[0]
    output_folder = video_name
    extract_slides(video_path, output_folder, threshold=500, resize_factor=0.25, skip_frames=5)
    # 调用函数，提取幻灯片