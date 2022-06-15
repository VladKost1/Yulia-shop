import random


class MyIterator:
    class MyIter:
        def __init__(self, iterable):
            self._iterable = iterable
            self.counter = 0

        def __next__(self):
            if self.counter == len(self._iterable.mydict):
                raise StopIteration()
            result = list(map(lambda kv: (kv[0], kv[1]), self._iterable.mydict.items()))[self.counter]
            self.counter += 1
            return result

    def __init__(self):
        self.mydict = {}

    def add_dict(self, item):
        self.mydict = item

    def __iter__(self):
        return self.MyIter(self)


my_dictionary = {1: "a", 2: "b", 3: "c"}
d = MyIterator()
d.add_dict(my_dictionary)
it = iter(d)
print(next(it))
print(next(it))
print(next(it))


def int_random_list(num):
    my_list = []
    string = "qwertyuiopasdfghjklzxcvbnm"
    length = random.randint(3, 12)
    for i in range(num):
        rand_string = "".join(random.choice(string) for j in range(length))
        my_list.append(rand_string)
    return my_list


print(int_random_list(4))
