import re


class SearchEngineBase(object):
    def __init__(self):
        pass

    def add_corpus(self, file_path):
        with open(file_path, 'r') as fin:
            text = fin.read()
        self.process_corpus(file_path, text)
    
    def process_corpus(self, id, text):
        raise Exception('process_corpus not implemented.')
    
    def search(self, query):
        raise Exception('search not implemented.')

def main(search_engine):
    for file_path in ['./test_file/1.txt', './test_file/2.txt', './test_file/3.txt', './test_file/4.txt']:
        search_engine.add_corpus(file_path)
    
    while True:
        query = input('enter your search word:')
        results = search_engine.search(query)
        print(f'found {len(results)} result(s):')
        for result in results:
            print(result)


class BOWEngine(SearchEngineBase):
    def __init__(self):
        super(BOWEngine, self).__init__()
        self.__id_to_words = {}
    
    def process_corpus(self, id, text):
        self.__id_to_words[id] = self.parse_text_to_words(text)
    
    def search(self, query):
        query_words = self.parse_text_to_words(query)
        results = []
        for id, words in self.__id_to_words.items():
            if self.query_match(query_words, words):
                results.append(id)
        return results
    
    @staticmethod
    def query_match(query_words, words):
        for query_word in query_words:
            if query_word not in words:
                return False
            return True
    
    @staticmethod
    def parse_text_to_words(text):
        # 使用正则表达式去除标点符号和换行符
        text = re.sub(r'[^\w]', ' ', text)
        # 转为小写
        text = text.lower()
        # 生成所有单词的列表
        word_list = text.split(' ')
        word_list = filter(None, word_list)
        return set(word_list)


if __name__ == "__main__":
    search_engine = BOWEngine()
    main(search_engine)