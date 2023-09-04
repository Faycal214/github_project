import random
import string

def get_password(lenght,number=True,special_char=True):
    caractere=string.ascii_letters
    chiffre=string.digits
    special=string.punctuation
    
    password=caractere
    if(number):
        password += chiffre
    if(special_char):
        password += special
    
    pswd=""
    for i in range(1,lenght+1):
        pswd +=random.choice(password)
        
    print("le mot de passe generer est :",pswd)
    
taille=int(input("donner la taille de mot de passe :"))

ch1=str(input("est ce qu'elle va contenir de chiffre(oui/no) :"))
if(ch1=="oui"):
    chiffre=True
else :
    chiffre=False

ch2=str(input("est ce qu'elle va contenir de caractere speciale (oui/no) :"))
if(ch2=="oui"):
    special=True
else :
    special=False

get_password(taille,chiffre,special)

