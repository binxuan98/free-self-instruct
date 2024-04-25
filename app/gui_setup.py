from tkinter.scrolledtext import ScrolledText
import tkinter as tk

class SetupGUI:
    @staticmethod
    def setup_gui(gui_instance):
        label = tk.Label(gui_instance.master, text="选择文档：")
        label.pack()

        select_button = tk.Button(gui_instance.master, text="选择", command=gui_instance.select_file)
        select_button.pack()

        output_text = ScrolledText(gui_instance.master)
        output_text.pack()

        label_template = tk.Label(gui_instance.master, text="选择模板：")
        label_template.pack()

        selected_template = tk.StringVar(gui_instance.master)
        selected_template.set("模板1")  # 默认选择第一个模板
        template_option = tk.OptionMenu(gui_instance.master, selected_template, "模板1", "模板2", "模板3", "模板4")
        template_option.pack()

        process_button = tk.Button(gui_instance.master, text="开始生成", command=gui_instance.process_text)
        process_button.pack()

        status_label = tk.Label(gui_instance.master, text="")
        status_label.pack()

        pause_button = tk.Button(gui_instance.master, text="暂停", command=gui_instance.pause_process)
        pause_button.pack()

