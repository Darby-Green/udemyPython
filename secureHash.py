import hashlib

# print(sorted(hashlib.algorithms_guaranteed))
# print(sorted(hashlib.algorithms_available))


pythonProgram = """for i in range(10)
print(i)
"""

print(pythonProgram)

# for b in pythonProgram.encode('utf8'):
#     print(b, chr(b))

ogHash = hashlib.sha256(pythonProgram.encode('utf8'))

print(f"SHA256: {ogHash.hexdigest()}")
print()

pythonProgram += "print('change code')"
print(pythonProgram)

newhash = hashlib.sha256(pythonProgram.encode('utf8'))
print(f"Sha256: {newhash.hexdigest()}")

if newhash.hexdigest() == ogHash.hexdigest():
    print("The file has not been modified!")
else:
    print("Warning, this file has been modified!")