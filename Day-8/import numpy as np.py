import numpy as np
data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
print("Original 1D Array:")
print(data)

reshaped_data = data.reshape(3, 4)
print("\nReshaped to 3x4 Array:")
print(reshaped_data)


#Creating another 3d
new_data = np.array([[13, 14, 15, 16],
                     [17, 18, 19, 20],
                     [21, 22, 23, 24]])
stacked_data = np.vstack((reshaped_data, new_data))
print("\nVertically Stacked Array:")
print(stacked_data)

second_row = stacked_data[1, :]
print("\nSecond Row:")
print(second_row)

element_3_2 = stacked_data[2, 1]
print("\nElement in 3rd row, 2nd column:")
print(element_3_2)

last_two_columns = stacked_data[:, -2:]
print("\nLast Two Columns:")
print(last_two_columns)
