# 6.857 testcode

a = 'a2 6c 49 3f 20 81 c2 e4 da 16 c9'
b = 'b1 71 4b 28 27 94 ce fd da 17 c0'

unia = ''
for let in a:
	unia += str(ord(let))
unib = ''	
for let in b:
	unib += str(ord(let))

# print unia
# print unib


def sxor(s1,s2, needtosplit=True):    
    # convert strings to a list of character pair tuples
    # go through each tuple, converting them to ASCII code (ord)
    # perform exclusive or on the ASCII code
    # then convert the result back to ASCII (chr)
    # merge the resulting array of characters as a string
    if needtosplit:
        split1 = s1.split(" ")
        split2 = s2.split(" ")

    assert len(split1) == len(split2)

    master = []
    for i in xrange(len(split1)):
    	hex1 = int(split1[i],16)
    	# we know that hex1 XOR k must be in range 41-5A, 61-7A
    	hex2 = int(split2[i],16)
    	# print hex1,hex2, hex1 ^ hex2,"\t", format(hex1 ^ hex2,"#010b") #, chr(hex1 ^ hex2)
        master.append(hex1 ^ hex2)
    	# print format(hex1 ^ hex2,"#010b")
    return master

master = sxor(a,b)
print master


def letterxor(s1):
	print 'input', s1, format(s1,'#010b')
	for i in xrange(ord('a'),ord('z')+1):
		print i, chr(i), s1 ^ i, chr(s1 ^ i)

# letterxor(29)

# all 11 letter words
results = []
with open('11 letter.txt') as inputfile:
    for line in inputfile:
        temp = line.strip().split(' ')
        for word in temp:
            results.append(word)

def check(s1,s2, master):
    assert len(s1) == len(s2)

    for i in xrange(len(s1)):
        h1 = ord(s1[i])
        h2 = ord(s2[i])
        if h1 ^ h2 != master[i]:
            return False
    return True

# brute force compare all strings
for i in xrange(len(results)):
    for j in xrange(i,len(results)):
        test = check(results[i],results[j], master)
        if test:
            print results[i],results[j], test
    if i % 100 == 0:
        print i
