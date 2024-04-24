import re
import json
import os
import datetime


# 定义一个函数，从txt文件中提取{}内的内容，并保存为json文件
def extract_and_save_as_json(txt_file, json_file):
    # 打开txt文件
    with open(txt_file, 'r', encoding='utf-8') as f:
        # 读取文件内容
        content = f.read()

    # 使用正则表达式找到所有{}内的内容
    matches = re.findall(r'\{([^}]*)\}', content)

    extracted_content = [json.loads('{' + match + '}') for match in matches if
                         json.loads('{' + match + '}')['instruction'] != '']

    # 打开json文件
    with open(json_file, 'w', encoding='utf-8') as f:
        # 将提取的内容写入json文件
        json.dump(extracted_content, f, ensure_ascii=False, indent=4)


def count_files_in_directory(directory):
    count = 0
    for _, _, files in os.walk(directory):
        count += len(files)
    return count


folder_path = r'/Users/zhangbinxuan/Downloads'
nums = count_files_in_directory(folder_path)



if __name__ == '__main__':
    outpath = r'/Users/zhangbinxuan/Downloads'
    final_path = os.path.join(outpath, f"{nums+1}.json")

    extract_and_save_as_json("/Users/zhangbinxuan/Downloads/1.txt", final_path)

    print("successfully extracted")

