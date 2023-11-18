
# Задание №2: Кэширование запросов


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache_dict = {}
        self.order_list = []

    @property
    def cache(self):
        if not self.order_list:
            return None
        get_key = self.order_list[-1]
        return get_key, self.cache_dict[get_key]

    @cache.setter
    def cache(self, new_elem):
        key, value = new_elem
        if key in self.order_list:
            self.order_list.remove(key)
            del self.cache_dict[key]
        if len(self.cache_dict) >= self.capacity:
            old = self.order_list.pop(0)
            del self.cache_dict[old]
        self.cache_dict[key] = value
        self.order_list.append(key)


    def get(self, key):
        if key in self.cache_dict:
            self.order_list.remove(key)
            self.order_list.append(key)
            return self.cache_dict[key]
        else:
            return None


    def print_cache(self):
        print("LRU Cache: ")
        for key in self.order_list:
            print(f"{key} : {self.cache_dict[key]}; ")

cache = LRUCache(3)

cache.cache = ("key1", "value1")
cache.cache = ("key2", "value2")
cache.cache = ("key3", "value3")

cache.print_cache()

print(cache.get("key2"))

cache.cache = ("key4", "value4")

cache.print_cache()






