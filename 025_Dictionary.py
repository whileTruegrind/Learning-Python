# Dictionaries:
    ## Dictionaries are used to store data values in key:value pairs
    ## A dictionary is a collection which is ordered*, changeable and do not allow duplicates
        ### *Dictionaries are written with curly brackets, and have keys and values
    ## As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered

capitals = {"India":"New Delhi", 
            "China":"Beijing",
            "Russia":"Moscow",
            "Pakistan":"Islamabad"}

print(capitals.get("India"))
print(capitals.get("Japan")) # Returns "None"

capitals.update({"Germany":"Berlin"})
print(capitals)

capitals.update({"India":"Mumbai"})
print(capitals)

capitals.pop("China")
print(capitals)

capitals.popitem()
print(capitals)

print(capitals.keys())
print(capitals.values())
print(capitals.items())

capitals.clear()
print(capitals)