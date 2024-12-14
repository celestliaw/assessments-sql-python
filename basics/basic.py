"""Python Basics: Lists, Dictionaries, & Booleans"""

#Data Objects
# 1. Lists
cities= ['Tokyo', 'LA','NY' , 'SF']
print(cities[1])

# 2. Dictionaries 
# characteristics; unordered
city_population = {
    'Tokyo': 13350000, # a key-value pair
    'Los Angeles': 18550000,
    'New York City': 8400000,
    'San Francisco': 1837442,
}
    #change value
city_population['San Francisco'] = 837442
print(city_population)

    #checkvalues; double equality checks value, one equality assigns value
print(city_population['Tokyo'] == 13350000) # Output: True
print(city_population['Tokyo'] != 50000) # Output: True



municipalities = {
    'New York City': [
        'Manhattan',
        'The Bronx',
        'Brooklyn',
        'Queens',
        'Staten Island'
    ],
    'Tokyo': [
        'Akihabara',
        'Harajuku',
        'Shimokitazawa',
        'Nakameguro',
        'Shibuya',
        'Ebisu/Daikanyama',
        'Shibuya District',
        'Aoyama',
        'Asakusa/Ueno',
        'Bunkyo District',
        'Ginza',
        'Ikebukuro',
        'Koto District',
        'Meguro District',
        'Minato District',
        'Roppongi',
        'Shinagawa District',
        'Shinjuku',
        'Shinjuku District',
        'Sumida District',
        'Tsukiji',
        'Tsukishima']
}

print(municipalities['Tokyo'])

type(municipalities['Tokyo'])  #OUTPUT: list

