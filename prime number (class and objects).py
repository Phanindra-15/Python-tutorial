class First:
    def __init__(self):
        self.num = int(input("Enter a number:"))


class Test(First):
    def check(self):
        i = 2
        p = 1
        while i <= self.num / 2:
            if self.num % i == 0:
                p = 0
                break
            i = i + 1

        if p == 1:
            print("Number is prime:", self.num)
        else:
            print("Number is not prime:", self.num)


obj = Test()
obj.check()
