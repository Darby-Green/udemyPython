import hashlib

publishedHash = '4f1d9991f5acc0ca119f9d443620b77f9d6b33703e51011c16baf57afb285fc6'

filename = 'colorama-0.4.6-py2.py3-none-any.whl'

with open(filename, 'rb') as downloadedFile:
    contents = downloadedFile.read()

fileHash = hashlib.sha256(contents).hexdigest()
print(fileHash)

if fileHash == publishedHash:
    print(f'{filename} is the correct file')
else:
    print(f'{filename} has been corrupted or tampered with!!!')