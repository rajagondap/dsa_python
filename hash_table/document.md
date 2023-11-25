## Hash Table

hash table is a data structure in python. which basically store the data in the form of key value pairs and index the pair
in an array

Dictionary can be said as the build in hashtable where the data is stored in the form of key value pair


### What we Learn today about HT?

Today we will learn how we create hash table and store it in the array using indexing the address where these key value 
pairs will be store as nested list at particular address using the index

However, we learn more detailed here on how we are hashing the data using hash method, which is the heart of hash table off course

#### Hash Method
the hash method is the function which takes key as ots input and generates the index number which is 
intern index of array where the key value par to be saved as nested lists of key and values as their items 

To Demonstrate the has table lets consider a hardware store where we store nuts, bots, nails, and many other items

The way the hash table works is we are going to need 
a hash method. What we are going to do with this method is we perform a hash 
on the key ( hashing means chopping into 2 pieces and storing) to get the 
index. here the hash method is a mathematical function to get the index based on the key

And that index is going to be the address in the array where we are going to store that key value pair


### Characteristics of hash method

1. It is one way - meaning, when we run key through hash, we get index but inverse is not true
2. It is Deterministic - meaning, for a particular hash function, everytime we pass the same key, 
it will produce same index


Even though python includes has table in the form of dictionary, we are going to create our own has table
we will create our own address by creating a list and create methods to do various operations

we will use the hash method of our own which will take key and values and give list of key and value 
along with the index of our address space where we store the list which we have got from hash method

We get the item using key inputting to hash method, and we know that hash method is deterministic, we will get the exact same index which 
we got it while storing that key and its associated value in the form of nested list

### Collision

Collision happens when you put a key value pair in the address where there is already a key value pair exists

we do store another key value pair by using nested list, 
meaning we store list [key, value] pairs within same address space by using putting them into another list 


for example:
[[key1, val1],[key2, val2]] at same index say x (value of x is an int)

**Separate Chaining** - So, this technique of handing collision by putting two entries in the same address is called Separate Chaining.
1. one way of handling separate chaining is using list
2. another way is using linked list

**Note** - we will look into only separate chaining

**Linear Probing** - So, there is another technique of handling collision is to put the next key value pair in next empty cell 
and is called linear probing and that is a form of open addressing


**Important**

length od hash table address spce should be always considered to be a prime number, 
so that we can avoid the confusion while storing the data.

This is simple documentation on hashtable - lets build constructor code 


# Hash Table Big O

1. using linked list - 
2. big O hash method is O(1)
3. set items if also O(1)
4. get items is O(n) in worrst case if the items are saved at one index - but if the distributed data and rare collision
then it is O(1)


# Commonly asked interview Questions

write a python code to find if two lists have elements in common

        def item_in_common(list1, list2):
            my_dict = {}
            for i in list1:
                my_dict[i] = True
        
            for j in list2:
                if j in my_dict:
                    return True
        
            return False
        
        
        list1 = [1,3,5]
        list2 = [2,4,6] 


Above is the code for the solution 