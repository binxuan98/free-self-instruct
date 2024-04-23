import json
import re
import markdown

def extract_json_from_markdown(md_path):
    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()

    html = markdown.markdown(content)
    json_data = []

    # 尝试从段落中提取 JSON 数据
    json_objs = get_objects_from_string(html)
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
'''累积新增到固定json文件中'''
# def main():
#     md_path = "/Users/zhangbinxuan/Downloads/chat_ceshi.md"  # 替换成你的 Markdown 文件路径
#     json_data = extract_json_from_markdown(md_path)
#
#     if json_data:
#         save_path = "/Users/zhangbinxuan/Downloads/json_ceshi-2.json"   # 替换成你想要保存的 JSON 文件的路径
#
#         # 尝试读取已有的 JSON 数据
#         existing_data = []
#         try:
#             with open(save_path, 'r', encoding='utf-8') as f:
#                 existing_data = json.load(f)
#         except FileNotFoundError:
#             pass
#
#         # 将新的 JSON 数据追加到已有的数据中
#         existing_data.extend(json_data)
#
#         # 写入到文件中
#         with open(save_path, 'w', encoding='utf-8') as f:
#             json.dump(existing_data, f, indent=4, ensure_ascii=False)  # 设置 ensure_ascii=False
#             print("Saved all JSON data to:", save_path)
'''单独新增一个json文件'''
def main():
    md_path = "/Users/zhangbinxuan/Downloads/chat_ceshi.md"  # 替换成你的 Markdown 文件路径
    json_data = extract_json_from_markdown(md_path)

    if json_data:
        save_path = "/Users/zhangbinxuan/Downloads/json_ceshi-2.json"   # 替换成你想要保存的 JSON 文件的路径

        # 写入到文件中
        with open(save_path, 'w', encoding='utf-8') as f:
            json.dump(json_data, f, indent=4, ensure_ascii=False)  # 设置 ensure_ascii=False
            print("Saved all JSON data to:", save_path)

if __name__ == "__main__":
    main()
