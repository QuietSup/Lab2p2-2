class Rectangle:
    def __init__(self):
        self.length = 1
        self.width = 1

    def set(self, width, length):
        if width <= 0 or width >= 20:
            self.width = "Width is out of range (0; 20)"
        else:
            if isinstance(width, float):
                self.width = width
            else:
                self.width = "Width is not float"
        if length <= 0 or length >= 20:
            self.length = "Length is out of range (0; 20)"
        else:
            if isinstance(length, float):
                self.length = length
            else:
                self.length = "Length is not float"

    def get_width(self):
        return self.width

    def get_length(self):
        return self.length

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


a = Rectangle()
a.set(1.0, 6.0)
print("width:", a.get_width())
print("length:", a.get_length())

try:
    print("area:", a.area())
    print("perimeter:", a.perimeter())
except:
    print("Wrong data")
