class A:
    def method(self):
        print("class A print method")

    def __init__(self):
        self.method()


class B:
    # def method(self):
    #     print("class B print method")

    def __init__(self):
        self.method()


class C:
    def method(self):
        print("class C print method")

    def __init__(self):
        self.method()


class D(B, C):
    pass


d = D()
