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


class BOWInvertedIndexEngine(SearchEngineBase):
    def __init__(self):
        super(BOWInvertedIndexEngine, self).__init__()
        self.inverted_index = {}
    
    def process_corpus(self, id, text):
        words = self.parse_text_to_words(text)
        for word in words:
            if word not in self.inverted_index:
                self.inverted_index[word] = []
            self.inverted_index[word].append(id)
    
    def search(self, query):
        query_words = list(self.parse_text_to_words(query))
        query_words_index = list()
        for query_word in query_words:
            query_words_index.append(0)
        for query_word in query_words:
            if query_word not in self.inverted_index:
                return []
        result = []
        while True:
            # 首先，获取当前状态下所有倒叙索引的index
            current_ids = []
            for idx, query_word in enumerate(query_words):
                current_index = query_words_index[idx]
                current_inverted_list = self.inverted_index[query_word]
                # 已经遍历到了某一个倒序索引的结尾，结束search
                if current_index >= len(current_inverted_list):
                    return result

                current_ids.append(current_inverted_list[current_index])
            # 然后，如果current_ids的所有元素都一样，那么表明这个单词在这个元素对应的文
            if all(x == current_ids[0] for x in current_ids):
                result.append(current_ids[0])
                query_words_index = [x + 1 for x in query_words_index]
                continue
            # 如果不是，我们就吧最小的元素加一
            min_val = min(current_ids)
            min_val_pos = current_ids.index(min_val)
            query_words_index[min_val_pos] += 1
    
    @staticmethod
    def parse_text_to_words(text):
        text = re.sub(r'[^\w]', ' ', text)
        text = text.lower()
        word_list = text.split(' ')
        word_list = filter(None, word_list)
        return set(word_list)

if __name__ == "__main__":
    search_engine = BOWInvertedIndexEngine()
    main(search_engine)


