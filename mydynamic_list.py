import ctypes

class MyList:

    def __init__(self, size):
        self.size = size
        self.num_of_element = 0
        self.mylist = self.__make_list(self.size)

    def __len__(self):
        return self.num_of_element 

    def append(self, item):
        if self.size == self.num_of_element:
            new_list = self.__make_list(self.size*2)
            self.size = self.size * 2
            for index in range(self.num_of_element):
                new_list[index] = item
            self.mylist = new_list
        self.mylist[self.num_of_element] = item
        self.num_of_element += 1
        

    def __str__(self):
        result = ''
        for index in range(self.num_of_element):
            result = result + str(self.mylist[index]) + ','
        return '[' + result[:-1] + ']'   

    def __make_list(self, size):
        # creating referential dynamic list by using c types array
        return (size*ctypes.py_object)()


if __name__ == '__main__':
    mylist = MyList(3)
    print(mylist)
    print(len(mylist)) 
    mylist.append(5)  
    mylist.append(5)  
    mylist.append(5)  
    mylist.append(5)  
    mylist.append(5)  
    mylist.append(5)  
    print(mylist)    
    print(len(mylist))  