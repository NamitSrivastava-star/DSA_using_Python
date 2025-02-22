# Certainly! In Python, a static variable is a class-level variable that is shared among all instances of the class. It is defined within the class but outside any instance methods. Here’s a simple example to illustrate how static variables work in Python:

class MyClass:
    # Static variable
    static_variable = 0

    def __init__(self, value):
        self.instance_variable = value
        # MyClass.static_variable += 1

    # def display(self):
    #     print(f"Instance Variable: {self.instance_variable}")
    #     print(f"Static Variable: {MyClass.static_variable}")

# Creating instances of MyClass
obj1 = MyClass(10)
obj2 = MyClass(20)

# Displaying values
# obj1.display()
# obj2.display()

print(obj1.instance_variable)
print(obj2.instance_variable)
print(obj1.static_variable)
print(obj2.static_variable)

obj1.static_variable = 4
# obj1.display()
# obj2.display()
print(obj1.instance_variable)
print(obj2.instance_variable)
print(obj1.static_variable)
print(obj2.static_variable)


MyClass.static_variable = 5
# obj1.display()
# obj2.display()
print(obj1.instance_variable)
print(obj2.instance_variable)
print(obj1.static_variable)
print(obj2.static_variable)


# In this example:

# static_variable is a static variable shared by all instances of MyClass.
# Each time a new instance is created, static_variable is incremented by 1.
# instance_variable is an instance variable unique to each instance.

# When you run this code, you will see that static_variable reflects the total number of instances created, while instance_variable holds the value specific to each instance.

# Feel free to experiment with this code to see how static variables behave in different scenarios! If you have any more questions or need further clarification, I'm here to help.