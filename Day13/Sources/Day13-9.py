# Class Attribute, Static Method, and Class Method

class Friend:
    # Class attribute
    # It is shared by all instances what be made from 'Friend' class.
    friend_members = []

    def __init__(self,name):
        self.name = name
        Friend.friend_members.append(self.name)

    def print_name(self):
        print(self.name)

    # Static Method
    # For define static method, use decorator '@staticmethod' avobe the code defining the function.
    # Static method can't access instance variables. so it's used when you want to define 'Pure function' in class.
    @staticmethod
    def bark():
        print("힝구")

    @classmethod
    def print_all_friends(cls):
        print(cls.friend_members)

    @classmethod
    def create_instance(cls, name):
        instance = cls(name)
        return instance

hamsik = Friend("Hamsik")
kkomi = Friend("Kkomi")

hamsik.print_name()
kkomi.print_name()

print(hamsik.friend_members)
print(kkomi.friend_members)
print(Friend.friend_members)


hamsik.bark()
kkomi.bark()
Friend.bark()


Friend.print_all_friends()

haeyong = Friend.create_instance("Haeyong")

print(haeyong.friend_members)
haeyong.print_name()
haeyong.bark()
Friend.print_all_friends()


# +a. if you want to check whether some object is instance of certain class, use 'isinstance' function.
if isinstance(haeyong, Friend):
    print("Haeyong is instance of Friend class.")
else:
    print("Haeyong isn't instance of Friend class.")
