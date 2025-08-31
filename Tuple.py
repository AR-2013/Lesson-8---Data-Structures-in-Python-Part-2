my_tuple = ()
print(my_tuple)

my_tuple = (1, 2, 3)
print(my_tuple)

my_tuple = (8, "Hello", 13.2)
print(my_tuple)

my_tuple = ("puppy", [2, 8, 13], (1, 2, 3))
print(my_tuple)

my_tuple = ('h', 'a', 'p', 'p', 'y')
print(my_tuple[0])
print(my_tuple[3])

n_tuple = ("puppy", [2, 8, 13], (1, 2, 3))

print(n_tuple[0][3])
print(n_tuple[1][1])

print("Sliced :",my_tuple[1:4])

for letter in(my_tuple):
    print("Hello", letter)