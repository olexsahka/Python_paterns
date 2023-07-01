"""
Декоратор динамический

"""

class FileWithLogging:
    def __init__(self, file):
        self.file = file

    def write_lines(self,strings):
        self.file.writelines(strings)
        print(f'wrote {len(strings)} lines')

    def __getattr__(self, item):
        print(f"call gettatr, current dict:{self.__dict__}")
        return getattr(self.__dict__['file'],item)

    def __setattr__(self, key, value):
        print(f"call setAttr with key{key} and value {value}")
        if key == "file":
            self.__dict__[key] = value
        else:
            setattr(self.__dict__['file'],key)

    def __delattr__(self, item):
        delattr(self.__dict__["file"],item)

    def __iter__(self):
        return self.file.__iter__()

    def __next__(self):
        return self.file.__next__()


if __name__ == "__main__":
    file = FileWithLogging(open("test.txt","w"))
    file.write_lines(["hello","world"])
    file.write("testing")
    file.close
