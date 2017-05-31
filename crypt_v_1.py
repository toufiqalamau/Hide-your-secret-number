alpha=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def crypt():
    code=int(raw_input('Please type the number you want to hide. \n\'0\' at the beginning of your number will be discarded: '))
    key=int(raw_input('type a prime number of your choice: '))
    mod=int(code%key)
    quotient=int(code//key)
    intlist=map(int, str(mod))
    intlist2= map(int, str(quotient))
    lttrlist=[alpha[i] for i in intlist]
    lttrlist2=[alpha[i] for i in intlist2]
    secret1=''.join(lttrlist)
    secret2=''.join(lttrlist2)
    print 'this is your secret 1: ',secret1,'. this is your secret 2: ',secret2,'. The prime you chose: ',key,'.'
    print 'Please keep these numbers and prime you chose for future use. If asked provide them accordningly.'
    return secret1,secret2

def decrypt():
    key=int(raw_input('Please type in the prime number you have used to hide your number: '))
    secret1=raw_input('Pleae, type in the secret 1 here: ')
    secret2=raw_input('Please, type in the secret 2 here: ')
    lttrlist=map(str, str(secret1))
    lttrlist2=map(str, str(secret2))
    intlist=[alpha.index(i) for i in lttrlist]
    intlist2=[alpha.index(i) for i in lttrlist2]
    m=''.join(map(str, intlist))
    mod=int(m)
    q=''.join(map(str, intlist2))
    quotient=int(q)
    code=(key*quotient)+mod
    print 'This is the number you hid: ',code,'.'
    return code
while True:
    try:
        q1=[1,2]
        q=int(raw_input('Please select what you want the program to do?\n1. Hide number.\n2. Show the numebr.\nYour choice: '))
        for i in q1:
            if q==i:
                if i==1:
                    crypt()
                elif i==2:
                    decrypt()
      
    except ValueError:
        print 'nope. wrong answer. Type 1 or 2.'
        
