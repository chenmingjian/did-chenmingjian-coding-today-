class Singleton:
    __instance = None

    def __init__(self):
        if not Singleton.__instance:
            print("__init__ method called.")
        else:
            print("Instance already created:", self.getInstance())
        
    @classmethod
    def getInstance(cls):
        if not cls.__instance:
            cls.__instance = Singleton()
        return cls.__instance

s = Singleton()
s1 = Singleton()
print(s.getInstance())
print(s1.getInstance())
print(Singleton.getInstance())
print(Singleton().getInstance())
