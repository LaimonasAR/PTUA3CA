# my_dictionary = {}
# my_dictionary["name"] = "Laimonas"

# # print(my_dictionary["name"])

# my_dictionary = {"name" : "Tom"}

# # print(my_dictionary["name"])
# print(my_dictionary)
# print(my_dictionary.get('name'))


countries_capitals = {
    'Lithuania': {
        'capital': 'Vilnius',
        'population': 3000000,
        'rich': 'poor'
        },
    'Poland': {
        'capital': 'Warsaw',
        'population': 10000000,
        'rich': 'medium'
        },
    'Latvia': {
        'capital': 'Riga',
        'population': 2000000,
        'rich': 'poor'

        },
    
}
print(countries_capitals['Latvia']["population"])



new_country = {'Spain':{'capital': 'Madrid', 'population': '5000000', "rich": "rich"}}
countries_capitals.update(new_country)

for country, info in countries_capitals.items():
    print("\nCountry:", country)
    for key in info:
        print(key + ':',info[key])

# print(countries_capitals.items())
# print(list(countries_capitals.items()))
# print(countries_capitals['Poland'].keys())
# print(countries_capitals['Latvia'].values())
# print(countries_capitals['Lithuania'].items())