import docx
import json
import re

def extract_json_from_word(docx_path):
    doc = docx.Document(docx_path)
    json_data = []

    for paragraph in doc.paragraphs:
        text = paragraph.text.strip()
        try:
            # 尝试从段落中提取 JSON 数据
            json_obj = get_object_from_string(text)
            if json_obj:
                json_data.append(json_obj)
        except Exception as e:
            print("Error extracting JSON:", str(e))
        print("Extracted JSON object:", json_obj)  # 添加调试输出以验证提取的 JSON 对象

    return json_data

def get_object_from_string(s):
    json_str = None

    # 尝试匹配 json object
    reg = r"\{[\s\S]*?\}"  # 修改正则表达式以非贪婪方式匹配多个 JSON 对象
    matches = re.findall(reg, s)
    for match in matches:
        try:
            json_obj = json.loads(match)
            return json_obj
        except Exception as e:
            pass

    # 尝试匹配 ```json ```包裹中匹配
    regex = r"```json\n([\s\S]*?)\n```"
    match = re.search(regex, s)
    if match:
        json_str = match.group(1)
        try:
            return json.loads(json_str)
        except Exception as e:
            pass

    return None ## #shdsadasd   s

def main():
    docx_path = "/Users/zhangbinxuan/Downloads/chat_ceshi.md"  # 替换成你的 Word 文档路径
    json_data = extract_json_from_word(docx_path)

    if json_data:
        save_path = "/Users/zhangbinxuan/Downloads/json_ceshi.json"   # 替换成你想要保存的 JSON 文件的路径

        # 尝试读取已有的 JSON 数据
        existing_data = []
        try:
            with open(save_path, 'r', encoding='utf-8') as f:
                existing_data = json.load(f)
        except FileNotFoundError:
            pass

        # 将新的 JSON 数据追加到已有的数据中
        existing_data.extend(json_data)

        # 写入到文件中
        with open(save_path, 'w', encoding='utf-8') as f:
            json.dump(existing_data, f, indent=4, ensure_ascii=False)  # 设置 ensure_ascii=False
            print("Saved all JSON data to:", save_path)

if __name__ == "__main__":
    main()
