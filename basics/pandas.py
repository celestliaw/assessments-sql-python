"""Pandas"""

# .sample(n=) method
# lets you get a random set of rows of a DataFrame

# .sort_values()
#data.sort_values(by='arr_delay', ascending=False)[:10]

#Lambda

"""def is_delayed(x):
    return x > 0
data['delayed'] = data['arr_delay'].apply(is_delayed)
OR
data['delayed'] = data['arr_delay'].apply(lambda x: x > 0)

"""
""".apply() method is going through every record one-by-one in the data['arr_delay'] series, 
where x is each record. Just as the def function does above, the lambda function 
checks if the value of each arr_delay record is greater than zero, then returns True or False."""