class Document():
    # 常量大写且写在类变量里面，其他任何成员函数都能访问
    WELCOME_STR = 'welcome! The context for this book is {}.'
    def __init__(self, title, author, context):
        print('init fuction called')
        self.title = title
        self.author = author
        self.__ccontext = context
        print(self.title)
        print(self.author)
        print(self.__ccontext)
    
    # 类函数
    @classmethod
    def create_empty_book(cls, title, author):
        # 这里很巧妙，返回了类实例化，类实例化时正好有调用构造方法
        return cls(title=title, author=author, context='nothing1')
    
    # 成员函数
    def get_context_length(self):
        return len(self.__ccontext)
    
    # 静态函数
    @staticmethod
    def get_welcome(context):
        return Document.WELCOME_STR.format(context)

if __name__ == "__main__":
    empty_book = Document.create_empty_book('this is title', 'panxueyan')
    
    print(empty_book.get_context_length())
    print(empty_book.get_welcome('harry boter'))