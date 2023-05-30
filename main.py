print("Grebnev PI-214")
array = [10,5,30,50,40]
array2 = []
for i in range(0,len(array)):
    if array[i] == max(array) or array[i] == min(array):
        array2.append(array[i] * 3)
    else:
        array2.append(array[i] * 2)
print(array2)
