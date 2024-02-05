person = {
    "name":"Wangari",
    "country": "Kenya",
    "age":"30"
}

print(person)
print (len(person))
print(type(person))

#to access items from inside dictionary
x = person["name"]
print(x)

if "name" in person:
    print("yes, it's completed!")
    