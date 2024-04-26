import tkinter as tk
from tkinter import messagebox
import webbrowser
from gui import GUI

class GUIWithMenu(GUI):
    def __init__(self, master):
        super().__init__(master)

        # 创建菜单栏
        self.menu_bar = tk.Menu(master)
        self.master.config(menu=self.menu_bar)

        # 创建直达大模型菜单
        self.model_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="大模型网页传送门", menu=self.model_menu)
        self.model_menu.add_command(label="ChatGPT", command=self.open_model_link_1)
        self.model_menu.add_command(label="智谱清言", command=self.open_model_link_2)
        self.model_menu.add_command(label="文新一言", command=self.open_model_link_3)
        self.model_menu.add_command(label="通义千问", command=self.open_model_link_4)

        # 创建帮助菜单
        self.help_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="帮助", menu=self.help_menu)
        self.help_menu.add_command(label="关于", command=self.show_about)

        # 创建科学上网攻略子菜单
        self.internet_guide_menu = tk.Menu(self.help_menu, tearoff=0)
        self.help_menu.add_cascade(label="科学上网攻略", menu=self.internet_guide_menu)
        self.internet_guide_menu.add_command(label="一键跳转", command=self.open_internet_guide)
        self.internet_guide_menu.add_command(label="文字攻略", command=self.show_internet_guide)

    def show_about(self):
        about_message = "本程序由斌轩开发，遇到任何问题请联系zhangbinxuan21@163.com"
        messagebox.showinfo("关于", about_message)

    def show_internet_guide(self):
        guide_message = "请访问以下网页，“https://ikuuu.pw/auth/register?code=Wo7O”\n如遇到问题请联系zhangbinxuan21@163.com"
        messagebox.showinfo("科学上网攻略", guide_message)

    def open_internet_guide(self):
        link = "https://ikuuu.pw/auth/register?code=Wo7O"
        webbrowser.open_new(link)

    def open_model_link_1(self):
        # 创建自定义对话框
        dialog = tk.Toplevel(self.master)
        dialog.title("科学上网确认")

        # 计算对话框的位置
        x = self.master.winfo_x() + (self.master.winfo_width() // 2) - (dialog.winfo_reqwidth() // 2)
        y = self.master.winfo_y() + (self.master.winfo_height() // 2) - (dialog.winfo_reqheight() // 2)

        # 设置对话框的位置
        dialog.geometry("+{}+{}".format(x, y))

        # 将对话框设置为置顶
        dialog.attributes("-topmost", True)

        # 添加提示文本
        label = tk.Label(dialog, text="您是否可以科学上网？请选择您的回答：")
        label.pack(padx=10, pady=5)

        # 添加按钮
        def open_link_and_close():
            self.open_link("https://chat.openai.com/")
            dialog.destroy()  # 关闭对话框

        btn_yes = tk.Button(dialog, text="我会", command=open_link_and_close)
        btn_yes.pack(side=tk.LEFT, padx=10, pady=5)

        def show_guide_and_close():
            dialog.destroy()  # 关闭对话框

            self.show_internet_guide()

        btn_no = tk.Button(dialog, text="还不会", command=show_guide_and_close)
        btn_no.pack(side=tk.RIGHT, padx=10, pady=5)


    def open_link(self, link):
        webbrowser.open_new(link)

    def open_model_link_2(self):
        link = "https://chatglm.cn/"
        webbrowser.open_new(link)

    def open_model_link_3(self):
        link = "https://yiyan.baidu.com/"
        webbrowser.open_new(link)

    def open_model_link_4(self):
        link = "https://tongyi.aliyun.com/qianwen/"
        webbrowser.open_new(link)

