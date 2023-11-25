class HashTable:
    def __init__(self, size=7):
        self.data_map = [None] * size

    def __hash(self, key):
        """
        This method returns the index in the address table based on the number of characters and type of characters in
        the key provided. This method does a mathematical calculation and returns on index where the key value par to be
        stored.

        Ordinal of letter gives ascii numerical value of the letter used 23 as it is prime number,
        and we can plug any prime number here in the position I have used 23
        we have used modulo % to get reminder after dividing using length of the address space

        :param key:
        :return: my_hash
        """
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash

    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] is None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

    def get_item(self, key):
        index = self.__hash(key)
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        return None

    def keys(self):
        all_keys = []
        for i in range(len(self.data_map)):
            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])):
                    all_keys.append(self.data_map[i][j][0])
        return all_keys


    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, " : ", val)


my_ht = HashTable()

my_ht.set_item('bolts', 100)
my_ht.set_item('washers', 50)
my_ht.set_item('lumber', 70)
my_ht.set_item('plyer', 55)

my_ht.print_table()

print(my_ht.get_item('lumber'))
print(my_ht.get_item('bolts'))
print(my_ht.get_item('paste'))

print(my_ht.keys())