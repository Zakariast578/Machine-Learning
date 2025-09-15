import numpy as np

#Assignment Link:
#https://g.co/gemini/share/efb851614d66


#A. Random integers#
print(f"Single random integer between 0 and 10: {np.random.randint(0, 10)}") #Single random integer between 0 and 10
print(f"Array of 5 random integers between 0 and 10: {np.random.randint(0, 10, size=5)}") #Array of 5 random integers between 0 and 10
print(f"3x4 array of random integers between 0 and 10: {np.random.randint(0, 10, size=(3, 4))}") #3x4 array of random integers between 0 and 10
print(f"Single random integer between 0 and 4: {np.random.randint(5)}")
print(f"Single random integer between 0 and 4: {np.random.randint(5)}")
print(f"Single random integer between 5 and 6: {np.random.randint(5, high=6)}")

random_arr = np.random.randint(-3, high=14,
                               size=(2, 2))
print(repr(random_arr))

#B. Utility functions#
print("Utility functions: ")
np.random.seed(1)
print(np.random.randint(10))
random_arr = np.random.randint(3, high=100,
                               size=(2, 2))
print(repr(random_arr))

# New seed
np.random.seed(2)
print(f"Single random integer between 0 and 10: {np.random.randint(10)}")
random_arr = np.random.randint(3, high=100,
                               size=(2, 2))
print(f"Random array with shape (2, 2): {repr(random_arr)}")

# Original seed
np.random.seed(1)
print(f"Single random integer between 0 and 10: {np.random.randint(10)}")
random_arr = np.random.randint(3, high=100,
                               size=(2, 2))
print(f"Random array with shape (2, 2): {repr(random_arr)}")

vec = np.array([1, 2, 3, 4, 5])
np.random.shuffle(vec)
print(repr(vec))
np.random.shuffle(vec)
print(repr(vec))

matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
np.random.shuffle(matrix)
print(repr(matrix))

#C. Distributions#
print("Distributions: ")
print(np.random.uniform())
print(np.random.uniform(low=-1.5, high=2.2))
print(repr(np.random.uniform(size=3)))
print(repr(np.random.uniform(low=-3.4, high=5.9,
                             size=(2, 2))))

print(np.random.normal())
print(np.random.normal(loc=1.0, scale=2.0))
print(repr(np.random.normal(loc=1.0, scale=2.0, size=3)))
print(repr(np.random.normal(loc=1.0, scale=2.0, size=(2, 2))))

#D. Custom sampling#
colors = ['red', 'blue', 'green']
print(np.random.choice(colors))
print(repr(np.random.choice(colors, size=2)))
print(repr(np.random.choice(colors, size=(2, 2),
                            p=[0.8, 0.19, 0.01])))