from abc import ABCMeta, abstractclassmethod


class Entity(metaclass=ABCMeta):
    """
    抽象类是一种特殊的类，它生下来就是作为父类存在的，一旦对象化就会报错。同样，抽象函数定义在抽象类之中，
    子类必须重写该函数才能使用。相应的抽象函数，则是使用装饰器
    @abstractmethod来表示。

    抽象类就是这么一种存在，它是一种自上而下的设计风范，你只需要用少量的代码描述清楚要做的事情，定义好接口，
    然后就可以交给不同开发人员去开发和对接。
    """
    @abstractclassmethod
    def get_title(self):
        pass

    @abstractclassmethod
    def set_title(self, title):
        pass


class Document(Entity):
    def get_title(self):
        return self.title
    
    def set_title(self, title):
        self.title = title


if __name__ == "__main__":
    document = Document()
    document.set_title('Harry Potter')
    print(document.get_title())

    entity = Entity()
