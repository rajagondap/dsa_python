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

    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, " : ", val)


my_ht = HashTable()

my_ht.print_table()
