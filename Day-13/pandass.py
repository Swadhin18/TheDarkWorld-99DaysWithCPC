import pandas as pd

mydataset = {
    "routine": ['LEG', 'CHEST','ARM'],
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}


index = [1,2,3] 
myvar = pd.DataFrame(mydataset,index)
a = ["x", "y", "z"]

val = pd.Series(a, index )

print(myvar, "\n")
print(val)
