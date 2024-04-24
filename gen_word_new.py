import pyautogui
import pyperclip
from time import sleep
import platform
from docx import Document

template1 = '''
根据以下文旅知识：
"{content}"
请你为我构造一个多轮问答数据,包含用户的问题instruction和你认为的标准答案output,你认为的标准答案请尽可能的字数多一点，输出结构化 JSON 对象：
{ "instruction": "", "input": "", "output": " "  },
'''
template2 = '''
根据以下文旅知识：
"{content}"
从【文旅管理单位】的角度出发,请你为我构造一个多轮问答数据,包含用户的问题instruction和你认为的标准答案output,你认为的标准答案请尽可能的字数多一点，输出结构化 JSON 对象：
{ "instruction": "", "input": "", "output": " "  },
'''
template3 = '''v
根据以下文旅知识：

"{content}"
从【游客】的角度出发，请你为我构造一个多轮问答数据,包含用户的问题instruction和你认为的标准答案output,你认为的标准答案请尽可能的字数多一点，输出结构化 JSON 对象：
{ "instruction": "", "input": "", "output": " "  },
'''
template4 = '''
根据以下文旅知识：
"{content}"
从【旅游平台】的角度出发，请你为我构造一个多轮问答数据,包含用户的问题instruction和你认为的标准答案output,你认为的标准答案请尽可能的字数多一点，输出结构化 JSON 对象：
{ "instruction": "", "input": "", "output": " "  },
'''


def read_word_file(file_path):
    doc = Document(file_path)
    content = ''
    for paragraph in doc.paragraphs:
        content += paragraph.text.strip() + '\n'
    return content.strip()


def process_text(content, selected_template):
    paragraphs = content.split('\n')
    for part in paragraphs:
        if part.strip():
            print(part)
            prompt = selected_template.replace('{content}', part)
            pyperclip.copy(prompt + '\n')

            if platform.system() == 'Windows':
                pyautogui.keyDown('ctrl')
                pyautogui.press('v')
                pyautogui.keyUp('ctrl')
            elif platform.system() == 'Darwin':
                pyautogui.keyDown('command')
                pyautogui.press('v')
                pyautogui.keyUp('command')

            enter_key_success = pyautogui.press('enter')
            if enter_key_success:
                print("Enter 键按下成功！")
                # 继续执行后续操作
                if platform.system() == 'Windows':
                    pyautogui.keyDown('ctrl')
                    pyautogui.press('v')
                    pyautogui.keyUp('ctrl')
                elif platform.system() == 'Darwin':
                    pyautogui.keyDown('command')
                    pyautogui.press('v')
                    pyautogui.keyUp('command')
                pyautogui.press('enter')  # 继续执行后续操作
            else:
                print("Enter 键按下失败，等待 5 秒后重试...")
                sleep(5)
                pyautogui.press('enter')

            sleep(20)


sleep(5)

content = read_word_file('/Users/zhangbinxuan/Downloads/dunhuang.docx')

selected_template = template2

process_text(content, selected_template)
