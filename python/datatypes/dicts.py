# Create a dictionary
my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# Access keys, values, and items
print("Keys:", my_dict.keys())       # dict_keys(['name', 'age', 'city'])
print("Values:", my_dict.values())   # dict_values(['Alice', 30, 'New York'])
print("Items:", my_dict.items())     # dict_items([('name', 'Alice'), ('age', 30), ('city', 'New York')])

# Update a value
my_dict["age"] = 31
print("Updated age:", my_dict["age"]) # Updated age: 31

# Add a new key-value pair
my_dict["job"] = "Engineer"
print("Added job:", my_dict["job"])   # Added job: Engineer

# Delete a key using del
del my_dict["city"]
print("After deleting city:", my_dict)

# Delete and return a value using pop
age_value = my_dict.pop("age")
print("Popped age:", age_value)
print("After popping age:", my_dict)

# Remove and return the last inserted item using popitem
last_item = my_dict.popitem()
print("Popped last item:", last_item)
print("After popitem:", my_dict)

# Clear all items
my_dict.clear()
print("After clear:", my_dict)
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

dict1.update(dict2)

print(dict1)
person = {'name': 'Alice', 'age': 30}

# Existing key
print(person.get('name'))  # Output: Alice

# Key not present, returns None by default
print(person.get('job'))   # Output: None

# Key not present, returns specified default value
print(person.get('job', 'Unemployed'))  # Output: Unemployed
