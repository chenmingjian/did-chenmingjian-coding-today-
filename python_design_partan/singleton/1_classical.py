class SingletonList(list):
    def __new__(cls):
        print(cls)
        if not hasattr(cls, 'instance'):
            cls.instance = super(SingletonList, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        print(id(self))
        self += [1, 2, 3, 4]
        print(self)


print(f'{hasattr(SingletonList, "instance")=}')
sl1 = SingletonList()
print(f'{hasattr(SingletonList, "instance")=}')


print(f'{sl1=} {id(sl1)=}')
print(SingletonList.__mro__)
print()

sl2 = SingletonList()
print(f'{sl2=} {id(sl2)=}')
print()

print(f'{id(SingletonList.__new__(SingletonList))=}')
print()
