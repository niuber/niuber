import json
import os
from datetime import datetime
import pytz


def modify_api(src_path, dest_path):
    """从 src_api.json 复制 lives、parses、ads 属性到 api.json"""
    try:
        # 读取源文件
        with open(src_path, 'r', encoding='utf-8') as f:
            src_data = json.load(f)
        
        # 如果目标文件不存在，创建空字典
        if not os.path.exists(dest_path):
            dest_data = {}
        else:
            with open(dest_path, 'r', encoding='utf-8') as f:
                dest_data = json.load(f)
        
        # 要替换的属性列表
        attrs_to_replace = ['lives', 'parses', 'ads']
        
        # 复制属性
        for attr in attrs_to_replace:
            if attr in src_data:
                dest_data[attr] = src_data[attr]
        
        # 写入目标文件
        with open(dest_path, 'w', encoding='utf-8') as f:
            json.dump(dest_data, f, indent=4, ensure_ascii=False)
        
        print(f"✅ Successfully updated {dest_path}")
    
    except Exception as e:
        print(f"❌ 修改api.json出错: {str(e)}")
        raise

def modify_json(src_path):
    """修改niuber.json的更新时间"""
    try:
        # 读取源文件
        with open(src_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        # 确保data是一个包含数组的字典，并且数组非空
        if isinstance(data, dict) and isinstance(data.get('urls', []), list):
            # 获取数组的第一个元素（如果存在）
            if data['urls']:
                # 创建北京时间时区对象
                beijing_tz = pytz.timezone('Asia/Shanghai')
                # 获取当前北京时间
                beijing_time = datetime.now(beijing_tz)
                current_time = beijing_time.strftime('%Y-%m-%d %H:%M:%S')
                # 更新name属性，包括当前时间
                data['urls'][0]['name'] = f"🦅🦅更新于:{current_time}"

        # 将修改后的数据写回文件
        with open('niuber.json', 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    except Exception as e:
        print(f"❌ 修改niuber.json出错: {str(e)}")
        raise
def addTX2api(src_path):
    # 要添加的配置项（就是你现在发的这个）
    new_item = {
        "key": "TX视频",
        "name": "TX｜视频",
        "type": 3,
        "api": "./js/drpy2.min.js",
        "ext": "./js/腾讯视频.js"
    }

    # 读取目标文件
    try:
        with open(src_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        data = []   # 如果文件不存在，初始化为空列表

    # 如果目标 JSON 是列表，直接 append
    if isinstance(data, list):
        data.append(new_item)
    elif isinstance(data, dict):
        # 如果是字典，可以以 key 为键存入，或放入某个字段
        data['sites'] = data.get('sites', []) + [new_item]

    # 写回文件
    with open(src_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    print("已添加腾讯视频配置到目标 JSON")

if __name__ == "__main__":
    # 从环境变量读取路径（默认值用于本地测试）
    src_file = os.getenv('SRC_FILE', './tvbox/api.json')
    dest_file = os.getenv('DEST_FILE', './tvbox/TVBoxOSC/tvbox/api.json')
    #修改api.json 添加直播、解析、广告过滤
    modify_api(src_file, dest_file)

    #添加TX源
    addTX2api(dest_file)
    
    jsonpath = os.getenv('JSON_FILE', './niuber.json')
    #修改niuber.json更新时间
    modify_json(jsonpath)
