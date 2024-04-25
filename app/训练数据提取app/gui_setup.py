import tkinter as tk

# def setup_gui(self):
#     # 模板内容显示区域
#     self.template_content = tk.StringVar()
#     self.template_text = tk.Text(self.template_frame, height=5, width=50)
#     self.template_text.pack(padx=10, pady=10)
#
#     # 文件选择区域
#     self.label = tk.Label(self.file_frame, text="选择文档：")
#     self.label.pack(side=tk.LEFT, padx=10, pady=5)
#
#     self.select_button = tk.Button(self.file_frame, text="选择", command=self.select_file)
#     self.select_button.pack(side=tk.LEFT, padx=10, pady=5)
#
#     # 输出文本区域
#     self.output_text = tk.Text(self.output_frame, height=10, width=50)
#     self.output_text.pack(padx=10, pady=10)
#
#     # 模板选择区域
#     self.label_template = tk.Label(self.template_selection_frame, text="选择模板：")
#     self.label_template.pack(side=tk.LEFT, padx=10, pady=5)
#
#     self.selected_template = tk.StringVar(self.master)
#     self.selected_template.set("模板1")  # 默认选择第一个模板
#     self.template_option = tk.OptionMenu(self.template_selection_frame, self.selected_template,
#                                          "模板1", "模板2", "模板3", "模板4", command=self.update_template_text)
#     self.template_option.pack(side=tk.LEFT, padx=10, pady=5)
#
#     # 功能按钮区域
#     self.process_button = tk.Button(self.button_frame, text="开始生成", command=self.process_text)
#     self.process_button.pack(side=tk.LEFT, padx=10, pady=5)
#
#     # 状态显示区域
#     self.status_label = tk.Label(self.status_frame, text="")
#     self.status_label.pack(padx=10, pady=5)
#
#     # 暂停按钮区域
#     self.pause_button = tk.Button(self.pause_frame, text="暂停", command=self.pause_resume_process)
#     self.pause_button.pack(side=tk.LEFT, padx=10, pady=5)
#
#     # 等待时间设置区域
#     self.sleep_label = tk.Label(self.sleep_frame, text="模型回复等待时间（秒）:")
#     self.sleep_label.pack(side=tk.LEFT, padx=10, pady=5)
#
#     self.sleep_value = tk.IntVar(self.master)
#     self.sleep_value.set(10)  # 设置默认等待时间为10秒
#     self.sleep_entry = tk.Entry(self.sleep_frame, textvariable=self.sleep_value)
#     self.sleep_entry.pack(side=tk.LEFT, padx=10, pady=5)
#
#     self.sleep_reminder_label = tk.Label(self.sleep_frame, text="如果模型回复慢，请增加这个数字")
#     self.sleep_reminder_label.pack(side=tk.LEFT, padx=10, pady=5)
#
#     # JSON 数据收集区域
#     self.collect_json_label = tk.Label(self.json_frame, text="点击收集 JSON 数据")
#     self.collect_json_label.pack(padx=10, pady=5)
#
#     self.collect_json_button = tk.Button(self.json_frame, text="收集 JSON", command=self.collect_json_data)
#     self.collect_json_button.pack(padx=10, pady=5)
#
#     # 定义模板内容
#     self.templates = [
#         '''
#         根据以下文旅知识：
#         "{content}"
#         请你为我构造一个多轮问答数据,包含用户的问题instruction和你认为的标准答案output,你认为的标准答案请尽可能的字数多一点，输出三条结构化 JSON 对象：
#         { "instruction": "", "input": "", "output": " "  },
#         ''',
#         '''
#         根据以下文旅知识：
#         "{content}"
#         从【文旅管理单位】的角度出发,请你为我构造一个多轮问答数据,包含用户的问题instruction和你认为的标准答案output,你认为的标准答案请尽可能的字数多一点，输出三条结构化 JSON 对象：
#         { "instruction": "", "input": "", "output": " "  },
#         ''',
#         '''
#         根据以下文旅知识：
#         "{content}"
#         从【游客】的角度出发，请你为我构造一个多轮问答数据,包含用户的问题instruction和你认为的标准答案output,你认为的标准答案请尽可能的字数多一点，输出三条结构化 JSON 对象：
#         { "instruction": "", "input": "", "output": " "  },
#         ''',
#         '''
#         根据以下文旅知识：
#         "{content}"
#         从【旅游平台】的角度出发，请你为我构造一个多轮问答数据,包含用户的问题instruction和你认为的标准答案output,你认为的标准答案请尽可能的字数多一点，输出三条结构化 JSON 对象：
#         { "instruction": "", "input": "", "output": " "  },
#         '''
#     ]
#
#     # 初始化模板文本框显示模板1的
#     self.update_template_text("模板1")
#
#     # 创建变量用于存储当前复制粘贴的内容
#     self.copy_content = tk.StringVar()
def setup_gui(self):
    # 模板内容显示区域
    self.template_content = tk.StringVar()
    self.template_text = tk.Text(self.template_frame, height=5, width=50)
    self.template_text.pack(padx=2, pady=2)

    # 文件选择区域
    self.label = tk.Label(self.file_frame, text="第1步:选择文档：")
    self.label.pack(side=tk.LEFT, padx=2, pady=2)

    self.select_button = tk.Button(self.file_frame, text="选择", command=self.select_file)
    self.select_button.pack(side=tk.LEFT, padx=2, pady=2)

    # 输出文本区域
    self.output_text = tk.Text(self.output_frame, height=10, width=50)
    self.output_text.pack(padx=2, pady=2)

    # 模板选择区域
    self.label_template = tk.Label(self.template_selection_frame, text="第2步:选择模板：")
    self.label_template.pack(side=tk.LEFT, padx=2, pady=2)

    self.selected_template = tk.StringVar(self.master)
    self.selected_template.set("模板1")  # 默认选择第一个模板
    self.template_option = tk.OptionMenu(self.template_selection_frame, self.selected_template,
                                         "模板1", "模板2", "模板3", "模板4", command=self.update_template_text)
    self.template_option.pack(side=tk.LEFT, padx=2, pady=2)

    # 功能按钮区域
    self.process_button = tk.Button(self.button_frame, text="点此\n开始运行",  height=3, width=5, command=self.process_text, bg="green",
                                    fg="black")
    self.process_button.pack(side=tk.LEFT, padx=10, pady=2)

    # 状态显示区域
    self.status_label = tk.Label(self.status_frame, text="", font=("Arial", 10))
    self.status_label.pack(padx=2, pady=2)

    # 暂停按钮区域
    self.pause_button = tk.Button(self.pause_frame, text="暂停", command=self.pause_resume_process, height=3, width=5, bg="orange",
                                  fg="black")
    self.pause_button.pack(side=tk.LEFT, padx=10, pady=2)

    # 等待时间设置区域
    self.sleep_label = tk.Label(self.sleep_frame, text="模型回复等待时间（秒）:",font=("Arial", 10))
    self.sleep_label.pack(side=tk.LEFT, padx=2, pady=2)

    self.sleep_value = tk.IntVar(self.master)
    self.sleep_value.set(10)  # 设置默认等待时间为10秒
    self.sleep_entry = tk.Entry(self.sleep_frame, textvariable=self.sleep_value)
    self.sleep_entry.pack(side=tk.LEFT, padx=2, pady=2)

    self.sleep_reminder_label = tk.Label(self.sleep_frame, text="如果模型回复慢，请增加这个数字", font=("Arial", 8))
    self.sleep_reminder_label.pack(side=tk.LEFT, padx=2, pady=2)

    # JSON 数据收集区域
    self.collect_json_label = tk.Label(self.json_frame, text="点击收集 JSON 数据", font=("Arial", 10))
    self.collect_json_label.pack(padx=2, pady=2)

    self.collect_json_button = tk.Button(self.json_frame, text="收集 JSON", command=self.collect_json_data,height=3, width=5, bg="blue",
                                         fg="black")
    self.collect_json_button.pack(padx=2, pady=2)

    # 定义模板内容
    self.templates = [
        '''
        根据以下文旅知识：
        "{content}"
        请你为我构造一个多轮问答数据,包含用户的问题instruction和你认为的标准答案output,你认为的标准答案请尽可能的字数多一点，输出三条结构化 JSON 对象：
        { "instruction": "", "input": "", "output": " "  },
        ''',
        '''
        根据以下文旅知识：
        "{content}"
        从【文旅管理单位】的角度出发,请你为我构造一个多轮问答数据,包含用户的问题instruction和你认为的标准答案output,你认为的标准答案请尽可能的字数多一点，输出三条结构化 JSON 对象：
        { "instruction": "", "input": "", "output": " "  },
        ''',
        '''
        根据以下文旅知识：
        "{content}"
        从【游客】的角度出发，请你为我构造一个多轮问答数据,包含用户的问题instruction和你认为的标准答案output,你认为的标准答案请尽可能的字数多一点，输出三条结构化 JSON 对象：
        { "instruction": "", "input": "", "output": " "  },
        ''',
        '''
        根据以下文旅知识：
        "{content}"
        从【旅游平台】的角度出发，请你为我构造一个多轮问答数据,包含用户的问题instruction和你认为的标准答案output,你认为的标准答案请尽可能的字数多一点，输出三条结构化 JSON 对象：
        { "instruction": "", "input": "", "output": " "  },
        '''
    ]

    # 初始化模板文本框显示模板1的
    self.update_template_text("模板1")

    # 创建变量用于存储当前复制粘贴的内容
    self.copy_content = tk.StringVar()