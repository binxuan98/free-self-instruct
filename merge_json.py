import json
import re
import os

def extract_json_from_text(txt_path):
    with open(txt_path, 'r', encoding='utf-8') as f:
        content = f.read()

    json_data = []

    # 尝试从文本中提取 JSON 数据
    json_objs = get_objects_from_string(content)
    if json_objs:
        json_data.extend(json_objs)

    return json_data

def get_objects_from_string(s):
    json_objs = []

    # 尝试匹配 json object
    reg = r"\{[\s\S]*?\}"  # 修改正则表达式以非贪婪方式匹配多个 JSON 对象
    matches = re.findall(reg, s)
    for match in matches:
        try:
            json_obj = json.loads(match)
            # 检查 JSON 对象是否为空，或者只包含空字符串或者空格
            if json_obj and not all(value.strip() == "" for value in json_obj.values()):
                json_objs.append(json_obj)
        except Exception as e:
            pass

    return json_objs

def merge_json_files(json_files, merged_file):
    merged_data = []
    for file in json_files:
        json_data = extract_json_from_text(file)
        if json_data:
            merged_data.extend(json_data)

    # 写入到文件中
    with open(merged_file, 'w', encoding='utf-8') as f:
        json.dump(merged_data, f, indent=4, ensure_ascii=False)
        print("Merged JSON data saved to:", merged_file)

def main():
    # 输入json文件路径
    json_folder = "/Users/zhangbinxuan/Desktop/微调数据集/攻坚队收集" # 替换成你存放 JSON 文件的文件夹路径
    json_files = [os.path.join(json_folder, file) for file in os.listdir(json_folder) if file.endswith('.json')]

    if not json_files:
        print("No JSON files found in the specified folder.")
        return

    merged_file = "/Users/zhangbinxuan/Desktop/微调数据集/攻坚队收集/4_27.json" # 替换成你想要保存的合并后的 JSON 文件的路径
    merge_json_files(json_files, merged_file)

if __name__ == "__main__":
    main()
