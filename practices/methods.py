"""Python Methods, Functions, & Libraries"""
import numpy

# 1. Methods; A method is an action that you can take on an object

# Let's use a dictionary you created in the previous lesson:
city_population = {
  'Tokyo': 13350000, # a key-value pair
  'Los Angeles': 18550000,
  'New York City': 8400000,
  'San Francisco': 1837442,
}

print(city_population.keys())
print(city_population.values())
# city_population.values()


# 2. Functions; 
# They're very similar to methods in that they perform an action, 
# but unlike methods, functions are not tied to specific objects.
"""Functions typically go in front of an object name (with the object wrapped in parentheses),
 whereas a method is appended to the end of an object name. For example, compare throw_rock(window) 
 with window.open()."""

# Libraries
# A library is a bundle of code made to help you accomplish routine tasks more quickly.
#You need to import a library in order to access the things in it (like its objects and methods)
import numpy
population_values = city_population.values()
population_values
numpy.mean(population_values)

