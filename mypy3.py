# Создайте класс LRU Cache, который хранит ограниченное количество объектов и,
# при превышении лимита, удаляет самые давние (самые старые) использованные элементы.
# Реализуйте методы добавления и извлечения элементов с использованием декораторов property и setter.
# @property
# def cache(self): # этот метод должен возвращать самый старый элемент
# ...
# @cache.setter
# def cache(self, new_elem): # этот метод должен добавлять новый элемент
# ...
# Советы
# Не забывайте обновлять порядок использованных элементов. В итоге должны удаляться давно использованные элементы,
# а не давно добавленные, так как давно добавленный элемент может быть популярен,
# и его удаление не поможет ускорить новые запросы.
#
# Пример:
#
# # Создаём экземпляр класса LRU Cache с capacity = 3
# cache = LRUCache(3)
# # Добавляем элементы в кэш
# cache.cache = ("key1", "value1")
# cache.cache = ("key2", "value2")
# cache.cache = ("key3", "value3")
# # # Выводим текущий кэш
# cache.print_cache() # key1 : value1, key2 : value2, key3 : value3
# # Получаем значение по ключу
# print(cache.get("key2")) # value2
# # Добавляем новый элемент, превышающий лимит capacity
# cache.cache = ("key4", "value4")
# # Выводим обновлённый кэш
# cache.print_cache() # key2 : value2, key3 : value3, key4 : value4
#
# Ожидаемый вывод в консоли:
#
# LRU Cache:
# key1 : value1
# key2 : value2
# key3 : value3
# value2
# LRU Cache:
# key3 : value3
# key2 : value2
# key4 : value4

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.__cache_dict = dict()

    @property
    def cache(self):
        return self.__cache_dict

    @cache.setter
    def cache(self, new_elem):
        self.__cache_dict[new_elem[0]] = new_elem[1]
        if len(self.__cache_dict.keys()) > self.capacity:
            for i in list(self.__cache_dict):
                self.__cache_dict.pop(i)
                break

    def print_cache(self):
        print("LRU Cache:")
        for key, val in self.cache.items():
            print(" : ".join((key, val)))

    def get(self, key):
        memory = self.cache.pop(key)
        for i in range(self.capacity):
            if i == self.capacity - 1:
                self.cache[key] = memory
        return memory


cache = LRUCache(3)
cache.cache = ("key1", "value1")
cache.cache = ("key2", "value2")
cache.cache = ("key3", "value3")
cache.print_cache() # key1 : value1, key2 : value2, key3 : value3
print(cache.get("key2")) # value2
cache.cache = ("key4", "value4")
cache.print_cache() # key2 : value2, key3 : value3, key4 : value4
