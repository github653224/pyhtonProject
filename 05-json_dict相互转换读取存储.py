import json
import os


class Solution:
    """
    json有四种方法： json.dumps(), json.loads(),json.dump(), json.load()
    json.dumps(): 接受一个参数python基本数据类型的dict，转换为json字符串
    json.loads(): 接受一个参数json字符串，转换为python基本数据类型的dict
    json.dump(): 接受两个参数python基本数据类型的dict，和文件，并把转换为json字符串写入到文件中
    json.load(): 接受一个参数json字符串文件，读取转换为python基本数据类型的dict
    """
    def __init__(self) -> None:
        self.parameters = {
            'symbol': '123456',
            'type': 'list',
            'price': 123.4,
            'amout': 23
        }

    def dict_to_json_write_into_file(self, json_path):
        with open(json_path, 'w') as f:
            json_str = json.dump(self.parameters, f)
    
    def json_file_to_dict(self, json_path):
        with open(json_path, 'r') as f:
            dict_data = json.load(f)
            return dict_data
    
    def root_path(self):
        return os.path.dirname(__file__)


if __name__ == "__main__":
    solution = Solution()
    json_file_root_path = solution.root_path() + os.sep + 'test.json'
    solution.dict_to_json_write_into_file(json_file_root_path)
    dict_data = solution.json_file_to_dict(json_file_root_path)
    print(dict_data)
