# class Cat:
#     def __init__(self, name):
#         self.name = name

#     def __str__(self):
#         return f'Cat: {self.name}'

# fluffy = Cat('Fluffy')

# print(fluffy)




# class Foo:
#     def __init__(self, number):
#         self.number = number

#     def __str__(self):
#         return f'Foo: {self.number}'
    
#     def __add__(self, other):
#         result = self.number + other.number
#         return Foo(result)

#     def __sub__(self, other):
#         result = self.number - other.number
#         return Foo(result)




# class Foo(int):
#     def __init__(self, number):
#         self.number = number




# a = Foo(1)
# b = Foo(2)

# c = a - b

# print(c)



class Fraction:
    def __init__(self, numer, denom):
        self.numer = numer
        self.denom = denom

    def __str__(self):
        return f'{self.numer}/{self.denom}'
    
    def get_numerator(self):
        return self.numer

    def get_denominator(self):
        return self.denom

    def __add__(self, other):
        denom_sum = self.denom * other.denom
        numer_sum = (self.numer * other.denom) + (other.numer * self.denom)
        return Fraction(numer_sum, denom_sum)

    def __sub__(self, other):
        denom_sum = self.denom * other.denom
        numer_sum = (self.numer * other.denom) - (other.numer * self.denom)
        return Fraction(numer_sum, denom_sum)

    def convert(self):
        divided_nums = self.numer / self.denom
        return divided_nums




onehalf = Fraction(1, 2)
twothird = Fraction(2, 3)
sum_ = onehalf + twothird
subtr = onehalf - twothird
print(sum_)
print(subtr)
print(type(sum_))
print(type(subtr))