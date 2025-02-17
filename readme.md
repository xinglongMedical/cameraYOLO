# 海康威视摄像头智能识别物体

通过YOLO框架，实现对海康威视摄像头的智能识别物体。
本项目来源于国家健康医疗大数据研究院工程中心，请通过邮箱wych@sdu.edu.cn联系我们

## 目录

1. [简介](#简介)
2. [安装](#安装)
3. [使用方法](#使用方法)
4. [示例](#示例)
5. [参考](#参考)

## 简介

本项目使用YOLO（You Only Look Once）框架，对海康威视摄像头捕获的视频流进行实时物体识别。YOLO是一种高效的目标检测算法，能够在保持高准确率的同时实现快速检测。

## 安装

请按照以下步骤安装所需的依赖项：

1. 克隆本项目代码：
    ```bash
    git clone https://github.com/yourusername/cameraYOLO.git
    cd cameraYOLO
    ```

2. 安装Python依赖项：
    ```bash
    pip install -r requirements.txt
    ```

3. 配置海康威视摄像头的连接信息。

## 使用方法

1. 启动摄像头并运行YOLO检测：
    ```bash
    python detect.py --source your_camera_source
    ```

2. 检测结果将实时显示在窗口中，并保存到指定目录。

## 示例

以下是一个使用YOLO检测海康威视摄像头视频流的示例：

![示例图像](path/to/example_image.jpg)

## 参考

- [YOLO官方文档](https://pjreddie.com/darknet/yolo/)
- [海康威视摄像头API文档](https://www.hikvision.com/cn/support/download/)
