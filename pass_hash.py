import hashlib
def encrypt(a):
    result = ""
    s = 6
    for i in range(len(a)):
        char = a[i]
        if char.isupper():
            result += chr((ord(char)+ 3 -65) %26 +65)
        elif char.islower():
            result += chr((ord(char)+ 6 -97) %26 +97)
        elif char.isdigit():
            x = int(char)
            y = x + 7
            result += str(y)
        else:
            result += char
    return result
def hashfunc(mystring):
    salt = 'aQz@94$'
    mystring = mystring + salt
    #print(mystring)
    hash_obj = hashlib.blake2s(mystring.encode())
    a = hash_obj.hexdigest()
    #print(a)
    a = a[::-1]
    #print(a)
    a = encrypt(a)
    #print(a)
    a = a[::-1]
    #print(a)
    hash_obj1 = hashlib.sha1(a.encode())
    b = hash_obj1.hexdigest()
    print(b)
    hash_obj2 = hashlib.md5(b.encode())
    b = hash_obj2.hexdigest()
    return b
hashfunc(password)