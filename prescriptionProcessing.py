from perscriptionData import patients

trailPatients = {"Denise", "Eddie", "Frank", "Georgia", "Kenny"}

while trailPatients:
    patient = trailPatients.pop()
    print(patient, end=" : ")
    prescription = patients[patient]
    print(prescription)

# we don't care what order this code gets done in, just that it gets done