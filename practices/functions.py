### assigning values to an existing column will overwrite that column"""

# data['new'] = 'overwritten'

"""control statements"""

"""if 'Opera Mini' in mobile:
    print 'great success.'"""

"""operas = ['The Marriage of Figaro', 'The Magic Flute', 'La traviata']
if 'The Marriage of Figaro' in mobile:
print 'grave success.'
elif 'The Marriage of Figaro' in operas:
print 'that is a gravely beautiful piece.'
else:
print 'that is immobile.'"""


### Defining Functions
#functions should only do one logical thing


# Parameter
# parameter is a very important part of the function. 
# Think of it as a temporary variable name you use when you define the function, but that gets replaced when you run the function.
"""def is_in_mobile(platform): #define the "is_in_mobile" function, which accepts an argument called "platform"
    if platform in mobile:
        print 'great success.'"""
"""is_in_mobile('BlackBerry')"""

# Return statements
"""A return statement is different from a print statement, because when it executes, 
return makes the value available to store as a variable or to use in another function. 
print simply makes the value appear on the screen."""
#The real use of return as opposed to print is the fact that you can assign the value to a variable name

#Apply functions to dataframes
#.apply() method 
"""data['platform'].apply(filter_desktop_mobile)"""

#selecting multiple columns
"""data[['platform','platform_type']][14:18] # rows with different values to make sure it worked
"""

# groupby()
"""group_by_carrier = data.groupby(['unique_carrier','delayed'])
count_delays_by_carrier = group_by_carrier.size().unstack() """

# plot chart
"""count_delays_by_carrier.plot(kind='barh', stacked=True, figsize=[16,6], colormap='winter')"""

#pivot_table()
"""flights_by_carrier = data.pivot_table(index='flight_date', columns='unique_carrier', values='flight_num', aggfunc='count')
"""


