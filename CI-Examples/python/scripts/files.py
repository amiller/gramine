import random

with open("/output/output.dat","wb") as f:

    n = random.randint(0,2**15)
    f.seek(n)
    f.write(b"hello world")

with open("/output/output.dat","rb") as f:
    n = random.randint(0,2**15)
    f.seek(n)
    s = f.read(11)

print("wrote a message to a random location in the encrypted file")
print(s)
