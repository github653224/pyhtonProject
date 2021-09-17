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


class SimpleEngine(SearchEngineBase):
    def __init__(self):
        super(SimpleEngine, self).__init__()
        self.__id_to_texts = {}
    
    def process_corpus(self, id, text):
        self.__id_to_texts[id] = text
    
    def search(self, query):
        results = []
        for id, text in self.__id_to_texts.items():
            if query in text:
                results.append(id)
        return results


if __name__ == "__main__":
    search_engine = SimpleEngine()
    main(search_engine)