import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText
from threading import Thread

from document_processor import DocumentProcessor

class GUI:
    def __init__(self, master):
        self.master = master
        master.title("多轮问答数据生成器")

        self.should_pause = False  # 暂停标志

        # 初始化 GUI
        self.setup_gui()

    def setup_gui(self):
        # Frame1: 选择文件
        frame1 = tk.Frame(self.master)
        frame1.pack(pady=10)

        label = tk.Label(frame1, text="选择文档：")
        label.pack(side="left", padx=10)

        select_button = tk.Button(frame1, text="选择", command=self.select_file)
        select_button.pack(side="left", padx=10)

        # Frame2: 显示文档路径
        frame2 = tk.Frame(self.master)
        frame2.pack(pady=10)

        self.label = tk.Label(frame2, text="未选择文档")
        self.label.pack(side="left", padx=10)

        # Frame3: 选择模板
        frame3 = tk.Frame(self.master)
        frame3.pack(pady=10)

        label_template = tk.Label(frame3, text="选择模板：")
        label_template.pack(side="left", padx=10)

        self.selected_template = tk.StringVar(self.master)
        self.selected_template.set("模板1")  # 默认选择第一个模板
        self.template_option = tk.OptionMenu(frame3, self.selected_template, "模板1", "模板2", "模板3", "模板4")
        self.template_option.pack(side="left", padx=10)

        # Frame4: 生成按钮
        frame4 = tk.Frame(self.master)
        frame4.pack(pady=10)

        self.process_button = tk.Button(frame4, text="开始生成", command=self.process_text)
        self.process_button.pack(side="left", padx=10)

        self.pause_button = tk.Button(frame4, text="暂停", command=self.pause_process)
        self.pause_button.pack(side="left", padx=10)

        # Frame5: 显示处理状态
        frame5 = tk.Frame(self.master)
        frame5.pack(pady=10)

        self.status_label = tk.Label(frame5, text="")
        self.status_label.pack(side="left", padx=10)

        # Frame6: 显示处理结果
        frame6 = tk.Frame(self.master)
        frame6.pack(pady=10)

        self.output_text = ScrolledText(frame6)
        self.output_text.pack(side="left", padx=10, fill="both", expand=True)

        self.doc_processor = DocumentProcessor()

        # 定义模板内容
        self.doc_processor.templates = [
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
            self.process_button.config(state="disabled")
            Thread(target=self.process_text_thread).start()
        else:
            messagebox.showinfo("提示", "请选择一个 Word 文档")

    def pause_process(self):
        self.should_pause = True  # 设置暂停标志

    def process_text_thread(self):
        if self.doc_processor.content:
            self.process_button.config(state="disabled")  # 禁用开始按钮
            selected_template = self.selected_template.get()
            template_index = int(selected_template[-1])  # 提取模板编号
            template = self.doc_processor.templates[template_index - 1]  # 根据模板编号获取模板

            for index, part in enumerate(self.doc_processor.content.split('\n'), 1):
                if self.should_pause:  # 检查是否需要暂停
                    self.should_pause = False  # 重置暂停标志
                    self.process_button.config(state="normal")  # 启用开始按钮
                    return  # 退出线程

                if part.strip():
                    self.doc_processor.process_paragraphs(template, index)  # 处理每个段落
                    self.master.after(0, self.update_status_label)  # 更新状态标签

            self.master.after(0, messagebox.showinfo, "提示", "生成完成！")
            self.process_button.config(state="normal")  # 启用开始按钮
        else:
            messagebox.showinfo("提示", "请选择一个 Word 文档")
    def update_status_label(self):
        status_text = f"文档总段落数：{self.doc_processor.total_paragraphs}，当前处理到第 {self.doc_processor.current_paragraph} 段"
        self.status_label.config(text=status_text)

root = tk.Tk()
app = GUI(root)
root.mainloop()
