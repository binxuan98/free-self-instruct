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

        # 初始化 GUI
        self.setup_gui()

    def setup_gui(self):
        self.label = tk.Label(self.master, text="选择文档：")
        self.label.pack()

        self.select_button = tk.Button(self.master, text="选择", command=self.select_file)
        self.select_button.pack()

        self.output_text = ScrolledText(self.master)
        self.output_text.pack()

        self.label_template = tk.Label(self.master, text="选择模板：")
        self.label_template.pack()

        self.selected_template = tk.StringVar(self.master)
        self.selected_template.set("模板1")  # 默认选择第一个模板
        self.template_option = tk.OptionMenu(self.master, self.selected_template, "模板1", "模板2", "模板3", "模板4")
        self.template_option.pack()

        self.process_button = tk.Button(self.master, text="开始生成", command=self.process_text)
        self.process_button.pack()

        self.status_label = tk.Label(self.master, text="")
        self.status_label.pack()

        self.pause_button = tk.Button(self.master, text="暂停", command=self.pause_process)
        self.pause_button.pack()

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
