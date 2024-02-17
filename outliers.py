# data = [4,5,104,105,110,120,130,130,150,160,170,183,185,187,188,191,350,
# 360]
# data = [4,5,104,105,110,120,130,130,150,160,170,183,185,187,188,191]
# data = [104,105,110,120,130,130,150,160,170,183,185,187,188,191,350,360]
# data = [104,105,110,120,130,130,150,160,170,183,185,187,188,191]
# data = [1000,1900,1911,1920,3450,2020]
data = []

min_val = 100
max_value = 200

# process low values in list
stop = 0
for index, value in enumerate(data):
    if value >= min_val:
        stop = index
        break
print(stop) #for debugging
del data[:stop]
print(data)

# process high values in list
start = 0
for i in range(len(data) - 1,-1,-1):
    if data[i] <= max_value:
        # we have the index of the last item we want to keep
        # set 'start' to the position of the first item we want to delete
        # which is 1 after 'i'
        start = i+1
        break
print(start) # debugging
del data[start:]
print(data)