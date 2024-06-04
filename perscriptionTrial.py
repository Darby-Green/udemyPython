from perscriptionData import *
#avoid import * in future

trialPatents = ["Denise", "Eddie", "Frank", "Georgia", "Kenny"]


for i in trialPatents:
    prescription = patients[i]
    try:
        prescription.remove(warfarin) # This will make the code crash when it gets to Kenny
        prescription.add(edoxaban)
    except KeyError:
        print(f"Patient, {i}, not taking Warfarian."
              f" Please remove {i} from the trial!!")
    print(i, prescription)