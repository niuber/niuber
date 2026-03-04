import json
import os

def modify_json(src_path, dest_path):
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
        print(f"❌ Error: {str(e)}")
        raise

if __name__ == "__main__":
    # 从环境变量读取路径（默认值用于本地测试）
    src_file = os.getenv('SRC_FILE', './tvbox1/api.json')
    dest_file = os.getenv('DEST_FILE', './tvbox1/TVBoxOSC/tvbox/api.json')
    
    modify_json(src_file, dest_file)
