from PIL import Image, ImageTk
import os

# 加载 PNG 图标
icon_path = "app/icon.png"  # 替换为你的 PNG 图标文件路径
icon_image = Image.open(icon_path)

# 将图标转换为 .ico 格式
icon_ico_path = "app/icon.ico"  # 转换后的 .ico 文件路径
icon_image.save(icon_ico_path, format="ICO")

