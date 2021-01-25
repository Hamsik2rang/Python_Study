class Test:
    instance_count = 0

    def __init__(self, first, second):
        self.variable_1 = first
        self.variable_2 = second
        Test.instance_count += 1

    def print_attribute(self):
        print(self.variable_1)
        print(self.variable_2)

    def get_instance_count(self):
        return self.instance_count


Test.name = "MyTest"
test1 = Test(2, 3)
test1.name = "test1"
test1.print_attribute()
print(test1.get_instance_count())

test2 = Test(5, 6)
test2.name = "test2"
test2.print_attribute()
print(test2.get_instance_count())

print("\n")
print(f"Test.name is {Test.name}")
print(f"test1.name is test1.name")
print(f"test2.name is test2.name")
