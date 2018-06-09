#dictionary {"key":value} - paris "jason kind"

#information of profile
information = {"name":"csk", "age":27,"city":"bangalore", "are":"jp nagar"}
print(information)
#accessing a single value from the dictionary
print(information["name"])
print(information["age"])
print(information["are"])

#function in a dictionary
print(dir(information))

#assignemt
#['clear','copy','fromkeys','get']
#items , keys, pop , 'popitem'
#set default, 'update'

print(information.items())
print(information.keys())
print(information.values())

for value,key in information.items():
    print(value,key)


