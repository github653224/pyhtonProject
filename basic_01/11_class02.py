class Entity():
    def __init__(self, object_tye):
        self.object_type = object_tye
    
    def get_context_length(self):
        raise Exception('get_context_length not implemented')
    
    def print_title(self):
        print(self.title)


class Document(Entity):
    # 常量大写且写在类变量里面，其他任何成员函数都能访问
    WELCOME_STR = 'welcome! The context for this book is {}.'
    def __init__(self, title, author, context):
        print('init fuction called')
        # Entity.__init__(self, 'Document')
        super(Document, self).__init__('Document1')
        self.title = title
        self.author = author
        self.__ccontext = context
        print(self.title)
        print(self.author)
        print(self.__ccontext)
    
    # 成员函数
    def get_context_length(self):
        return len(self.__ccontext)


class Video(Entity):
    def __init__(self, title, author, video_length):
        print('Video class init called')
        Entity.__init__(self, 'Video')
        self.title = title
        self.author = author
        self.__video_length = video_length
    
    def get_context_length(self):
        return self.__video_length

if __name__ == "__main__":
    harry_potter_book = Document('Harry Potter book title', 'panxueyan', 'this is context')
    harry_potter_video = Video('Harry Potter video title', 'pxy', 120)

    print(harry_potter_book.object_type)
    print(harry_potter_video.object_type)

    # harry_potter_book.print_title()
    # harry_potter_video.print_title()

    # print(harry_potter_book.get_context_length())
    # print(harry_potter_video.get_context_length())
   