import requests
import json

def fetch_json_from_url(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch JSON from URL:", url)
        return None

def main():
    url = "https://chat.openai.com/share/22c5556b-74f2-4502-8fdc-8e52d98a72b3"  # 替换成你要读取的网页的URL
    json_content = fetch_json_from_url(url)
    if json_content:
        # 创建一个列表来保存所有的 JSON 内容
        all_json_data = []

        # 将每个 JSON 内容添加到列表中
        for data in json_content:
            all_json_data.append(data)

        # 设置保存的 JSON 文件路径
        save_path = "/Users/zhangbinxuan/all_json_data.json"  # 替换成你想要保存的路径

        # 将整个列表保存到指定路径的 JSON 文件中
        with open(save_path, 'w') as f:
            json.dump(all_json_data, f, indent=4)
            print("Saved all JSON data to:", save_path)

if __name__ == "__main__":
    main()
