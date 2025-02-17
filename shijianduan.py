import cv2

# RTSP 地址
#url = "rtsp://admin:yjy226226@10.15.18.5/Streaming/Channels/2?starttime=20241114T100000Z&endtime=20241114T100003Z"
url = "rtsp://admin:hik12345@10.25.18.235/Streaming/Channels/2"
# 打开视频流
cap = cv2.VideoCapture(url)


ret, frame = cap.read()
if ret:
    frame_width = frame.shape[1]
    frame_height = frame.shape[0]
    print(f"Width: {frame_width}, Height: {frame_height}, FPS: {cap.get(cv2.CAP_PROP_FPS)}")
else:
    print("Failed to read frame.")


# 检查是否成功打开视频流
if not cap.isOpened():
    print("无法打开视频流")
    exit()

# 获取视频的宽、高和帧率
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

print(fps,frame_width,frame_height)
# # 定义输出视频文件名和编码格式
# output_file = "output.mp4"
# fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # MP4 格式
# out = cv2.VideoWriter(output_file, fourcc, fps, (frame_width, frame_height))
#
# print("开始保存视频...")
# num=0
# while True:
#     ret, frame = cap.read()
#     cv2.imshow("frame", frame)
#     print(num)
#     num=num+1
#     if not ret:
#
#         print("视频流结束或读取失败")
#         break
#
#     # 写入帧到输出文件
#     out.write(frame)
#
#     # 如果需要显示画面，可以使用以下代码（根据需求打开/关闭）
#     # cv2.imshow("Video", frame)
#     # if cv2.waitKey(1) & 0xFF == ord('q'):
#     #     break
#
# # 释放资源
# cap.release()
# out.release()
# cv2.destroyAllWindows()
#
# print(f"视频已保存为 {output_file}")
