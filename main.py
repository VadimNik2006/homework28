# Реализуйте модернизированную версию контекст-менеджера File:
#
# теперь при попытке открыть несуществующий файл менеджер должен автоматически создавать и
# открывать этот файл в режиме записи;
# на выходе из менеджера должны подавляться все исключения, связанные с файлами.\

class ContextManager:
    def __init__(self, file_name):
        print("Модернизированный контекст-менеджер")
        self.my_file = file_name

    def __enter__(self):
        if self.my_file is None:
            with open("my_file.txt", "a", encoding="utf-8") as false_file:
                false_file.write("b")
        else:
            with open(self.my_file, "w", encoding="utf-8") as true_file:
                true_file.write("c")

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print(exc_type)
            return True


with ContextManager(None) as abc:
    print(abc)
