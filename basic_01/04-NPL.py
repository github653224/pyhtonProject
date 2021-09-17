import re
import os


class Solution:
    """
    1. 读取文件；
    2. 去除所有标点符号和换行符，并把所有大写变成小写
    3. 合并相同的词，统计每个词出现的频率，并按照词频从大到小排序；
    4. 将结果按行输出到文件 out
    """
    def __init__(self, text_file) -> None:
        self.lst = list()
        self.tmp_dict = dict()
        self.text_file_path = text_file
    
    def get_word_count(self, text):
        # 通过re正则子串替换字符串中所有非英文字母数字和换行空白（即把换行和标点符号全部使用空格代替）
        text = re.sub(r'[^\w]', ' ', text)

        # 所有单词字母小写
        text = text.lower()
        # 通过空格进行分割为列表
        word_list = text.split(' ')
        print(word_list)
        # 过滤去掉列表中所有空格的元素
        word_list = filter(None, word_list)
        # 再次转换为无空格的列表
        word_list = list(word_list)

        # 下面的循环把出现的单子增加到字典中
        for word in word_list:
            if word not in self.tmp_dict:
                self.tmp_dict[word] = 0
            self.tmp_dict[word] += 1

        # 根据字典的值的大小排序
        sorted_word_count_dict = sorted(self.tmp_dict.items(), key=lambda kv: kv[1], reverse=True)
        return sorted_word_count_dict
    
    def read_text_file(self, in_file_path):
        with open(in_file_path, 'r') as f:
            text = f.read()
            return text

    def write_word_count_into_file(self, text, out_file_path):
        if not os.path.exists(out_file_path):
            os.makedirs(out_file_path)
        try:
            word_count_list = self.get_word_count(text)
            with open(out_file_path + os.sep + f'{out_file_path}.text', 'w') as f:
                for word, req in word_count_list:
                    f.write(f"{word} {req} \n")
        except (FileExistsError, FileNotFoundError, IOError) as error:
            print(error)

    @classmethod
    def get_root_path(cls, text_file):
        root_path = os.path.dirname(__file__)
        file_path = root_path + os.sep + text_file
        return cls(file_path)


if __name__ == "__main__":
    solution = Solution.get_root_path('in/in.text')
    text_content = solution.read_text_file(solution.text_file_path)
    solution.write_word_count_into_file(text_content, 'out2')


    # solution = Solution()
    # root_path = solution.get_root_path()
    
    # in_file_path = root_path + os.sep + "in.text"
    # out_file_path = root_path + os.sep + "out.text"

    # solution.write_word_count_into_file(in_file_path, out_file_path)
