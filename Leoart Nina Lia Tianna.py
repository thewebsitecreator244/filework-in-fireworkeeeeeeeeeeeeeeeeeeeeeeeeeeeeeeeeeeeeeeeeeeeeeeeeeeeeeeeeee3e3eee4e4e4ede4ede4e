with open("C:\\Users\Prêt\OneDrive\Bureau\Leoart Nina Lia Tianna.txt","r",) as age:
    text = age.read()
alsotext = text.split()
textagain = alsotext[1::2]
for index in range(len(textagain)):
    textagain[index] = int(textagain[index]) + 1
print(textagain)
