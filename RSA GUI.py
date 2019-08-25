import sys
import sympy
import random
from tkinter import * 
import tkinter.simpledialog
import tkinter.messagebox
from fractions import gcd


def isprime(n):
    if(sympy.isprime(n) == False):
        #print("Entered integer is not a prime")
        sys.exit()
    
def lcm(a,b):
    i = max(a,b)
    while i>0:
        if(i%a == 0) and (i%b == 0):
            return i
        else:
            i = i + 1    

root = Tk()
w = Label(root, text = "RSA Cryptosystem")
w.pack()

print ("CODE")
#primes = [i for i in range(200,500) if isprime(i)]
num1 = sympy.randprime(50, 100) 
num2 = sympy.randprime(20, 150) 

#print("Heya")
#num1 = int(raw_input("Enter first prime integer : "))
isprime(num1)
#num2 = int(raw_input("Enter second prime integer : "))
isprime(num2)
n = num1 * num2
elist = []
phi = (num1-1) * (num2-1)

i = 2
while i < phi:
    if(gcd(i,phi) == 1):
        elist.append(i)
    else:
        pass
    i= i+1

#print elist
#e = int(raw_input("Enter the value of e chosen : "))
e = elist[-1]
lamb = lcm(num1-1,num2-1)
d = 1
while d>0:
    k = (d*e)%lamb
    if(k == 1):
        #print("The value of d is : " + str(d))
        break
    else:
        d= d+1
        
#msg = raw_input("Enter the message for encryption : ")
msg = tkinter.simpledialog.askstring("Encryption", "Type your text for encryption : ")
codednum = []
for l in msg:
    coded = str(ord(l))
    codednum.append(coded)
    
encryptedlist = []
decryptedlist = []
encryptedtext = ""
decryptedtext = ""

#print "Encryption starts..."
for x in codednum:
    encryption = ((int(x)**e) % n)
    encryptedlist.append(encryption)
    encryptedtext = encryptedtext + chr(encryption)
    
int_elist = map(int,encryptedlist)
#print "Encryption done!"
#print int_elist
#print ("The encrypted text is : " + encryptedtext)
#output = "Your encrypted message is : %s" %(encryptedtext)
tkinter.messagebox.showinfo("ENCRYPTED TEXT", encryptedtext)

#choice = raw_input("Do you want to decrypt the message? Y or N  ")
choice = tkinter.simpledialog.askstring("Decryption","Do you want to decrypt the message? Y or N ")
if(choice == "y" or choice == "Y"):
    for x in int_elist:
        decryption = ((int(x)**d) % n)
        decryptedlist.append(decryption)
        decryptedtext = decryptedtext + chr(decryption)
    
    #int_dlist = map(int,decryptedlist)
    #print int_dlist
    #print ("The revealed text is : \n" + decryptedtext)
    tkinter.messagebox.showinfo("DECRYPTION TEXT", decryptedtext)    
else:
    #print ("Ok Bye!!!")
    tkinter.messagebox.showinfo("Exiting", "OK BYE BYE!")
