import one

print ("** This is where the import happen **")
one.f()
print(one.mult(12,34))

if __name__ == '__main__':
    print("we are in main of two.py")
else:
    print("two.py is being imported")