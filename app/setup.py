from document_processor import DocumentProcessor
from tkinter.scrolledtext import ScrolledText
import tkinter as tk

class SetupGUI:
    @classmethod
    def setup_gui(cls, master):
        label = tk.Label(master, text="选择文档：")
        label.pack()

        select_button = tk.Button(master, text="选择", command=cls.select_file)
        select_button.pack()

        output_text = tk.scrolledtext.ScrolledText(master)
        output_text.pack()

        label_template = tk.Label(master, text="选择模板：")
        label_template.pack()

        selected_template = tk.StringVar(master)
        selected_template.set("模板1")  # 默认选择第一个模板
        template_option = tk.OptionMenu(master, selected_template, "模板1", "模板2", "模板3", "模板4")
        template_option.pack()

        process_button = tk.Button(master, text="开始生成", command=cls.process_text)
        process_button.pack()

        status_label = tk.Label(master, text="")
        status_label.pack()

        pause_button = tk.Button(master, text="暂停", command=cls.pause_process)
        pause_button.pack()

    # 定义模板内容
        cls.templates = [
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

        def select_file():
            file_path = filedialog.askopenfilename(filetypes=[("Word 文档", "*.docx")])
            if file_path:
                label.config(text="已选择文档：" + file_path)
                doc_processor.load_document(file_path)
                update_status_label()
            else:
                label.config(text="未选择文档")

        def process_text(self):
            if self.doc_processor.content:
                self.process_button.config(state="disabled")
                Thread(target=self.process_text_thread).start()
            else:
                messagebox.showinfo("提示", "请选择一个 Word 文档")

        def pause_process(self):
            self.should_pause = True  # 设置暂停标志
