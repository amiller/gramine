These are python demos to work with the spicy printfs.

## Example program

scripts/userstest.py

This initializes a file, then picks a random location to access

## Running the program
Assuming you've already set up gramine on an SGX machine:

```
SGX=1 make
```

I found this useful for quick development:


## Building and printing MRENCLAVE

```
docker build -t gramine .
docker run --rm gramine
```