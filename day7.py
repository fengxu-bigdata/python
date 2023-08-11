import qrcode

url = input("请输入一个网址：")
code_path = input("请输入二维码保存地址：")

qr = qrcode.QRCode(
    version=2,  # 尺寸
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # 容错率
    box_size=10,  # 二维码格子的像素
    border=1  # 边框宽度
)
qr.add_data(url)  # 将内容写入二维码对象
img = qr.make_image()  # 生成图片对象
img.save(code_path)  # save操作
