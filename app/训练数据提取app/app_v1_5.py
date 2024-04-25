import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from threading import Thread
from datetime import datetime
import json_extractor
from document_processor import DocumentProcessor
import json
import gui_setup

class GUI:
    def __init__(self, master):
        self.master = master
        master.title("多轮问答数据生成器")
        master.iconbitmap("icon.ico")


        self.should_pause = False  # 暂停标志

        self.doc_processor = DocumentProcessor()

        # 创建各个功能区域的 Frame
        self.template_frame = tk.Frame(master)
        self.template_frame.grid(row=0, column=0, padx=10, pady=10)

        self.file_frame = tk.Frame(master)
        self.file_frame.grid(row=1, column=0, padx=10, pady=5)

        self.output_frame = tk.Frame(master)
        self.output_frame.grid(row=2, column=0, padx=10, pady=10)

        self.template_selection_frame = tk.Frame(master)
        self.template_selection_frame.grid(row=3, column=0, padx=10, pady=5)

        self.button_frame = tk.Frame(master)
        self.button_frame.grid(row=4, column=0, padx=10, pady=5)

        self.status_frame = tk.Frame(master)
        self.status_frame.grid(row=5, column=0, padx=10, pady=5)

        self.pause_frame = tk.Frame(master)
        self.pause_frame.grid(row=6, column=0, padx=10, pady=5)

        self.sleep_frame = tk.Frame(master)
        self.sleep_frame.grid(row=7, column=0, padx=10, pady=5)

        self.json_frame = tk.Frame(master)
        self.json_frame.grid(row=8, column=0, padx=10, pady=5)

        # 直接调用 setup_gui 函数
        gui_setup.setup_gui(self)



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
            # 获取用户输入的等待时间
            sleep_time = self.sleep_value.get()

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
                    self.doc_processor.process_paragraphs(template, index, sleep_time)  # 处理每个段落
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
