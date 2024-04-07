vehicles = {
    'dream' : 'Honda 250T',
    'roadster' : 'BMW R1100',
    'er5' : 'Kawasaki ER5',
    'can-am' : 'Bombardier Can-Am 250',
    'virago' : 'Yamaha XV250',
    'tenere' : 'Yamaha XT650',
    'jimny' : 'Suzuki Jimny 1.5',
    'fiesta' : 'Ford Fiesta Ghia 1.4'
}

vehicles["Starfighter"] = "X-Wing"
vehicles["Learjet"] = "Bombardier Learjet 75"
vehicles['toy'] = 'Glider'

#upgrade virago
vehicles['virago'] = "Yamaha XV535"

del vehicles["Starfighter"]
result = vehicles.pop('f1', "That does not exist")
print(result)
print()
# for key in vehicles:
#     print(key, vehicles[key], sep=", ")

for key ,value in vehicles.items():
    print(key, value, sep=', ')