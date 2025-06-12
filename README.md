# ClipConcat

## 项目名称

这是一个用于视频剪辑拼接、信息提取和批量处理的 Python 工具库，主要依赖 `moviepy` 和 `pymediainfo` 库，同时部分功能依赖于 `ffmpeg`。

---

## 目录结构

以下为项目目录结构：

```
/ (项目根目录)
├── cls/                # 存放待处理或已重命名的视频文件（由 `namemaker.py` 处理）
├── ppt/                # 存放 PPT 视频文件，用于视频拼接
├── testlist/           # 测试列表目录，可存放测试数据或结果文件
├── clip_concat.py      # 主视频拼接脚本：遍历 cls 和 ppt 目录中的视频文件进行拼接，并记录处理日志
├── clip_concat_small.py# 简化版视频拼接脚本，示例如何调用视频拼接函数处理单组视频文件
├── clip_load.py        # 加载视频文件并输出视频基本信息（时长、fps、尺寸）
├── namemaker.py        # 依据视频文件的编码时间来重命名存放在 cls 目录下的视频文件
├── process.bat         # 批处理脚本：利用 ffmpeg 对 cls 和 ppt 目录中的视频进行重编码及输出到指定目录
├── search_file.py      # 遍历并搜索指定目录下的视频文件，打印文件名和完整路径
├── small_clip.py       # 截取两个视频文件的前 10 秒，生成子片段后合成新的叠加视频
├── LICENSE             # GNU GPLv3 开源许可证文件
└── README.md           # 当前文件，对项目的介绍和使用说明
```

---

## 目录及文件介绍

- **cls/**  
  存放需要处理的视频文件。文件通常由 `namemaker.py` 脚本根据视频编码信息重命名为格式为 `计算方法_YYYY_MM_DD_HH_MM.mp4` 的名称。

- **ppt/**  
  存放 PPT 相关的视频文件，用于与 cls 目录中的视频进行叠加拼接。

- **testlist/**  
  用于存放测试用例或者结果的目录，可根据需要自行添放测试文件。

- **clip_concat.py**  
  主要逻辑为：  
  - 加载 cls 和 ppt 两个目录下的视频文件列表。  
  - 对应序列的视频文件调用 `clip_concat` 函数，利用 `moviepy.editor` 进行视频叠加处理。  
  - 输出处理后的视频文件，并生成一个 `timelog.txt` 日志文件记录每次处理的开始时间、结束时间和耗时。

- **clip_concat_small.py**  
  为主脚本的简化版本，示例如何对指定视频文件（例如 `"output-1.mp4"` 与 `"output-2.mp4"`）进行拼接操作，便于调试和小规模处理。

- **clip_load.py**  
  通过 `VideoFileClip` 类加载指定视频文件（例如 `"output-2.mp4"`），并打印视频的基本信息（时长、帧率、尺寸）。

- **namemaker.py**  
  读取 cls 目录下所有视频文件，提取视频编码时间（使用 `pymediainfo`），并转换成自定义的时间格式（如 `计算方法_YYYY_MM_DD_HH_MM.mp4`），然后重命名文件。

- **process.bat**  
  批处理脚本，主要功能有：  
  - 检查输出目录（`outputcls` 和 `outputppt`）是否存在，不存在则创建。  
  - 分别对 `cls` 和 `ppt` 目录下的所有 mp4 文件利用 `ffmpeg` 进行视频编码转换（设置 `codec`, `preset`, 帧率及音频拷贝），输出至对应目录。

- **search_file.py**  
  遍历指定目录（默认 `cls`）下的文件，打印文件名与完整路径。可用于检查文件存在情况。  
  
  > 注意：脚本中返回的是排序后的列表（通过 `list.sort()`），但此函数返回值为 None，请根据需求调整排序逻辑。
  
- **small_clip.py**  
  主要功能为：  
  - 加载两段视频（例如 `"计算方法_2024_04_09_08_00~2.mp4"` 与 `"计算方法_2024_04_09_08_00_ppt~2.mp4"`），截取它们的前 10 秒作为子片段；  
  - 利用 `CompositeVideoClip` 将两个子片段合成一个叠加视频，便于预览或生成小样。

- **LICENSE**  
  GPLv3 开源许可证，规定了代码的使用、修改与分发的相关条款。

- **README.md**  
  当前文件，包含项目介绍、目录结构、各脚本功能说明及使用方法等信息。

---

## 环境要求和依赖

- Python 3.x 环境  
- 安装依赖包：  
  ```sh
  pip install moviepy pymediainfo
  ```
- 需要安装 [`ffmpeg`](https://ffmpeg.org/)，确保 `ffmpeg` 命令在系统 PATH 中可用。

---

## 使用方法

1. **视频重命名**  
    运行 `namemaker.py` 脚本，将 cls 目录下的文件重命名为格式化的名称：  
    
    ```sh
    python namemaker.py
    ```
    
2. **视频转码处理**  
    运行批处理脚本 `process.bat` 进行批量视频处理。直接在 Windows 命令提示符中执行：  
    
    ```bat
    process.bat
    ```
    
3. **查看视频信息**  
    使用 `clip_load.py` 加载视频并打印信息：  
    
    ```sh
    python clip_load.py
    ```
    
4. **视频子片段及叠加合成**  
    运行 `small_clip.py` 获取视频的前 10 秒并合成新视频：  
    
    ```sh
    python small_clip.py
    ```
    
5. **视频拼接操作**  
    - 使用 `clip_concat.py` 对 `cls` 与 `ppt` 目录下的视频进行拼接：  
      ```sh
      python clip_concat.py
      ```
    - 或者测试简化版脚本 `clip_concat_small.py` 验证视频拼接。

---

## 注意事项

- 确保把 `cls` 和 `ppt` 目录中放置的视频文件格式正确，并且视频文件均为 mp4 格式。  
- 视频拼接时调整参数（例如拼接位置、缩放比例 `alpha`）可根据实际需求进行修改。  
- 运行批处理脚本前请先确保输出目录不存在冲突数据。  
- 使用 `pymediainfo` 获取视频编码时间时，请确保视频文件中包含 `encoded_date` 信息，否则可能需要调整解析逻辑。

---

## 拾遗

新增`ppt_gen.py`，针对PPT视频，智能生成课件图片。图片保存在与PPT视频同名的文件夹下。
```sh
python ppt_gen.py
```