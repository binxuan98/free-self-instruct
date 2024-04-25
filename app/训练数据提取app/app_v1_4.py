import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from threading import Thread
from datetime import datetime
import json_extractor
from document_processor import DocumentProcessor
import json

class GUI:
    def __init__(self, master):
        self.master = master
        master.title("多轮问答数据生成器")

        master.iconbitmap("icon.ico")  # 设置窗口图标，替换 "your_icon.ico" 为你的图标文件路径
        self.should_pause = False  # 暂停标志

        # 初始化 GUI
        self.setup_gui()

    def setup_gui(self):
        # 创建文本框用于显示模板内容
        self.template_content = tk.StringVar()
        self.template_text = tk.Text(self.master, height=5, width=50)
        self.template_text.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        self.label = tk.Label(self.master, text="选择文档：")
        self.label.grid(row=1, column=0, padx=10, pady=5)

        self.select_button = tk.Button(self.master, text="选择", command=self.select_file)
        self.select_button.grid(row=1, column=1, padx=10, pady=5)

        self.output_text = tk.Text(self.master, height=10, width=50)
        self.output_text.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        self.label_template = tk.Label(self.master, text="选择模板：")
        self.label_template.grid(row=3, column=0, padx=10, pady=5)

        self.selected_template = tk.StringVar(self.master)
        self.selected_template.set("模板1")  # 默认选择第一个模板
        self.template_option = tk.OptionMenu(self.master, self.selected_template, "模板1", "模板2", "模板3", "模板4",
                                             command=self.update_template_text)
        self.template_option.grid(row=3, column=1, padx=10, pady=5)

        self.process_button = tk.Button(self.master, text="开始生成", command=self.process_text)
        self.process_button.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

        self.status_label = tk.Label(self.master, text="")
        self.status_label.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

        self.pause_button = tk.Button(self.master, text="暂停", command=self.pause_resume_process)
        self.pause_button.grid(row=6, column=0, columnspan=2, padx=10, pady=5)

        self.doc_processor = DocumentProcessor()

        self.collect_json_label = tk.Label(self.master, text="点击按钮收集 JSON 数据")
        self.collect_json_label.grid(row=8, column=0, columnspan=2, padx=10, pady=5)

        self.collect_json_button = tk.Button(self.master, text="收集 JSON", command=self.collect_json_data)
        self.collect_json_button.grid(row=9, column=0, columnspan=2, padx=10, pady=5)

        # 定义模板内容
        self.templates = [
            '''
            根据以下文旅知识：
            "{content}"
            请你为我构造一个多轮问答数据,包含用户的问题instruction和你认为的标准答案output,你认为的标准答案请尽可能的字数多一点，输出结构化 JSON 对象：
            { "instruction": "", "input": "", "output": " "  },
            ''',
            '''
            根据以下文旅知识：
            "{content}"
            从【文旅管理单位】的角度出发,请你为我构造一个多轮问答数据,包含用户的问题instruction和你认为的标准答案output,你认为的标准答案请尽可能的字数多一点，输出结构化 JSON 对象：
            { "instruction": "", "input": "", "output": " "  },
            ''',
            '''
            根据以下文旅知识：
            "{content}"
            从【游客】的角度出发，请你为我构造一个多轮问答数据,包含用户的问题instruction和你认为的标准答案output,你认为的标准答案请尽可能的字数多一点，输出结构化 JSON 对象：
            { "instruction": "", "input": "", "output": " "  },
            ''',
            '''
            根据以下文旅知识：
            "{content}"
            从【旅游平台】的角度出发，请你为我构造一个多轮问答数据,包含用户的问题instruction和你认为的标准答案output,你认为的标准答案请尽可能的字数多一点，输出结构化 JSON 对象：
            { "instruction": "", "input": "", "output": " "  },
            '''
        ]

        # 初始化模板文本框显示模板1的
        self.update_template_text("模板1")

        # 创建变量用于存储当前复制粘贴的内容
        self.copy_content = tk.StringVar()

    def select_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Word 文档", "*.docx")])
        if file_path:
            self.label.config(text="已选择文档：" + file_path)
            self.doc_processor.load_document(file_path)
            self.update_status_label()
        else:
            self.label.config(text="未选择文档")

    def process_text(self):
        if self.doc_processor.content:
            # 显示开始生成提示信息
            self.output_text.insert(tk.END, f"{datetime.now().strftime('%Y.%m.%d-%H:%M:%S')} 开始生成\n")
            self.output_text.see(tk.END)
            self.master.update()

            self.process_button.config(state="disabled")
            Thread(target=self.process_text_thread).start()
        else:
            messagebox.showinfo("提示", "请选择一个 Word 文档")

    def pause_resume_process(self):
        if self.should_pause:  # 如果当前处于暂停状态
            self.should_pause = False  # 设置为继续状态
            self.pause_button.config(text="暂停")  # 修改按钮文本为“暂停”
            self.pause_status_label.config(text="")  # 清空状态信息
        else:
            self.should_pause = True  # 设置为暂停状态
            self.pause_button.config(text="继续")  # 修改按钮文本为“继续”
            timestamp = datetime.now().strftime('%Y.%m.%d-%H:%M:%S')
            # 获取当前处理到的段落索引
            current_index = self.doc_processor.current_paragraph
            # 在文本框中插入指定信息
            self.output_text.insert(tk.END,
                                    f"{timestamp} 当前处理到第{current_index}段，程序已经暂停，如需继续运行，请点击（继续）按钮\n")
            self.output_text.see(tk.END)  # 滚动到文本末尾

    def process_text_thread(self):
        if self.doc_processor.content:
            self.process_button.config(state="disabled")  # 禁用开始按钮
            selected_template = self.selected_template.get()
            template_index = int(selected_template[-1])  # 提取模板编号
            template = self.templates[template_index - 1]  # 根据模板编号获取模板

            for index, part in enumerate(self.doc_processor.content.split('\n'), 1):
                while self.should_pause:  # 检查是否需要暂停
                    self.master.update()  # 更新界面
                    continue  # 继续等待暂停解除

                # 显示当前的文本内容和时间
                timestamp = datetime.now().strftime('%Y.%m.%d-%H:%M:%S')
                self.output_text.insert(tk.END, f"{timestamp} 第{index}段 复制成功，请将鼠标放置在模型对话框中⌛️\n")
                # 滚动到文本末尾
                self.output_text.see(tk.END)
                # 更新界面以显示实时内容
                self.master.update()

                if part.strip():
                    self.doc_processor.process_paragraphs(template, index)  # 处理每个段落
                    self.master.after(0, self.update_status_label)  # 更新状态标签

            self.master.after(0, self.show_generation_complete_message)  # 显示生成完成提示信息
            self.process_button.config(state="normal")  # 启用开始按钮
        else:
            messagebox.showinfo("提示", "请选择一个 Word 文档")

    def show_generation_complete_message(self):
        messagebox.showinfo("提示", "生成完成！")

    def update_status_label(self):
        status_text = f"文档总段落数：{self.doc_processor.total_paragraphs}，当前处理到第 {self.doc_processor.current_paragraph} 段"
        self.status_label.config(text=status_text)

    def update_template_text(self, selected_template):
        template_index = int(selected_template[-1])  # 提取模板编号
        self.template_text.delete('1.0', tk.END)  # 清空文本框内容
        self.template_text.insert(tk.END, self.templates[template_index - 1])  # 插入对应模板内容

    def collect_json_data(self):
        txt_path = filedialog.askopenfilename(filetypes=[("Text 文本文件", "*.txt")])  # 选择文本文件
        if txt_path:
            json_data = json_extractor.extract_json_from_text(txt_path)  # 调用新的功能模块中的函数

            if json_data:
                save_path = filedialog.asksaveasfilename(defaultextension=".json",
                                                         filetypes=[("JSON 文件", "*.json")])  # 选择保存路径
                if save_path:
                    with open(save_path, 'w', encoding='utf-8') as f:
                        json.dump(json_data, f, indent=4, ensure_ascii=False)  # 写入 JSON 数据到文件中
                    messagebox.showinfo("提示", "JSON 数据提取完成并保存到文件中！")
                else:
                    messagebox.showinfo("提示", "未选择保存路径！")
            else:
                messagebox.showinfo("提示", "未找到有效的 JSON 数据！")
        else:
            messagebox.showinfo("提示", "未选择文本文件！")

root = tk.Tk()
app = GUI(root)
root.mainloop()
