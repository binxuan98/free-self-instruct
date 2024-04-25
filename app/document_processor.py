
import pyautogui
import pyperclip
from time import sleep
import platform
from docx import Document

class DocumentProcessor:
    def __init__(self):
        self.content = None
        self.total_paragraphs = 0
        self.current_paragraph = 0

    def load_document(self, file_path):
        doc = Document(file_path)
        self.content = ''
        for paragraph in doc.paragraphs:
            self.content += paragraph.text.strip() + '\n'
        self.total_paragraphs = len(self.content.split('\n'))

    # def process_paragraphs(self, template):
    #     paragraphs = self.content.split('\n')
    #     for index, part in enumerate(paragraphs, 1):
    #         if part.strip():
    #             prompt = template.replace('{content}', part)
    #             pyperclip.copy(prompt + '\n')
    #             if platform.system() == 'Windows':
    #                 pyautogui.hotkey('ctrl', 'v')
    #             elif platform.system() == 'Darwin':
    #                 pyautogui.hotkey('command', 'v')
    #             pyautogui.press('enter')
    #             sleep(20)
    #             self.current_paragraph = index

    def process_paragraphs(self, template, index):
        part = self.content.split('\n')[index - 1]  # 获取当前段落
        prompt = template.replace('{content}', part.strip())
        pyperclip.copy(prompt + '\n')
        if platform.system() == 'Windows':
            pyautogui.hotkey('ctrl', 'v')
        elif platform.system() == 'Darwin':
            pyautogui.hotkey('command', 'v')
        pyautogui.press('enter')
        sleep(20)
        self.current_paragraph = index  # 更新当前段落索引