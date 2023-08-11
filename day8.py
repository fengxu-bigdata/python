import imageio, os

path = input("请输入图片资源文件夹路径：")
gif_path = input("请输入GIF图片的保存路径：")
img_flie_list = os.listdir(path)
frames = []
for img_name in img_flie_list:
    img_path = str(path + "\\" + img_name)
    frames.append(imageio.imread_v2(img_path))

imageio.mimwrite(gif_path, frames, 'GIF', duration=2000)  # 后面的切换频率 时间单位是毫秒
