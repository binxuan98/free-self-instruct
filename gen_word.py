import pyautogui
import pyperclip
from time import sleep
import platform
from docx import Document

'''
从 Word 文档中读取要输入到 chatgpt 的查询文本，问题的提示模板在下面构造，支持多提示。
'''

template1 = '''
根据以下文旅知识：
"{content}"
请你为我构造一个多轮问答数据，包含用户的问题instruction和你认为的标准答案output。格式为：
{ "instruction": "", "input": "", "output": " "  },
{ "instruction": "", "input": "", "output": " "  },
{ "instruction": "", "input": "", "output": " "  },
'''
template2 = '''
根据以下文旅知识：
"{content}"
从【文旅管理单位】的角度出发,请你为我构造一个多轮问答数据,包含用户的问题instruction和你认为的标准答案output,输出结构化 JSON 对象：
{ "instruction": "", "input": "", "output": " "  },
{ "instruction": "", "input": "", "output": " "  }
'''
template3 = '''
根据以下文旅知识：
"{content}"
从【游客】的角度出发，请你为我构造一个多轮问答数据，包含用户的问题instruction和你认为的标准答案output。格式为：
{ "instruction": "", "input": "", "output": " "  },
{ "instruction": "", "input": "", "output": " "  },
{ "instruction": "", "input": "", "output": " "  },
'''
template4 = '''
根据以下文旅知识：
"{content}"
从【旅游平台】的角度出发，请你为我构造一个多轮问答数据，包含用户的问题instruction和你认为的标准答案output。格式为：
{ "instruction": "", "input": "", "output": " "  },
{ "instruction": "", "input": "", "output": " "  },
{ "instruction": "", "input": "", "output": " "  },
'''



def read_word_file(file_path):
    # 打开 Word 文档
    doc = Document(file_path)
    content = ''
    # 提取文档中的所有段落内容
    for paragraph in doc.paragraphs:
        content += paragraph.text.strip() + '\n'

    return content.strip()


def process_text(content, selected_template):
    # 按换行符分割文本为段落
    paragraphs = content.split('\n')
    for part in paragraphs:
        if part.strip():  # 检查分段是否为空
            print(part)
            prompt = selected_template.replace('{content}', part)

            pyperclip.copy(prompt + '\n')  # 复制文本到剪贴板

            # 判断当前操作系统是Windows还是Mac，然后执行相应的粘贴操作
            if platform.system() == 'Windows':
                pyautogui.keyDown('ctrl')  # 按下 'ctrl' 键
                pyautogui.press('v')  # 模拟 'v' 键，进行粘贴
                pyautogui.keyUp('ctrl')  # 松开 'ctrl' 键
            elif platform.system() == 'Darwin':  # 'Darwin' 是 Mac OS X 的内核名称
                pyautogui.keyDown('command')  # 按下 'command' 键
                pyautogui.press('v')  # 模拟 'v' 键，进行粘贴
                pyautogui.keyUp('command')  # 松开 'command' 键

            # 检查 Enter 键是否按下成功
            enter_key_success = pyautogui.press('enter')
            if enter_key_success:
                print("Enter 键按下成功！")
            else:
                print("Enter 键按下失败，等待 5 秒后重试...")
                sleep(5)  # 等待 5 秒
                pyautogui.press('enter')  # 再次模拟按下 'enter' 键

            sleep(10)  # 等待 10 秒



sleep(5)  # 延迟 5 秒执行，请 5 秒内打开活动窗！

# 读取 Word 文档并提取内容
content = read_word_file('/Users/zhangbinxuan/Downloads/dunhuang.docx')

# 选择要使用的模板（1 或 2）
selected_template = template2  # 在这里指定要使用的模板


# 处理提取的内容v
process_text(content, selected_template)

