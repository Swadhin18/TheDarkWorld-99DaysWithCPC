
name = "Swadhin Chacraborty" #from where to print
print(name[0:7]) #from the front
print(name[-11:]) # from the bac

a = name[0:7]
b = name[-11:]
sumName = a + " " + b
print(sumName)

age = 36 #formate string
txt = f"My name is {sumName}, I am {age} years old,"
print(txt)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])