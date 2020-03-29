# Ödev Çözüm  (20.Ders)

liste = [121,4,43,432,52,5,33,523]

mini = 10
maxi = 0

for i in liste:
    
    if i > maxi :
        
        maxi = i
        
    if i < mini:
        
        mini = i
        
print("Maximum değer : ",maxi)    
print("Minimum değer : ",mini)

# enumerate (21.Ders)
 
liste = [1,2,3,4,56,67]

for i in liste :
    
    print(i)



for i,j in enumerate(liste):
    
    print("index : ",i,"değer :",j)
    
    

sozluk = {"elma " : "kırmızı" , "üzüm" : "yeşil"}

sozluk.items()

for m,n in sozluk.items():
    
    print("key:", m, "value:", n)
    
    
# while()  (22.Ders)

i = 0

while(i<5):
    
    print(i)
    
    i += 1
    
    
m = 0

while (m!=20):
    
    print(m)
    m += 5
    
    
liste = [1,2,3,4,5]
uzunluk = len(liste)
i = 0
toplam = 0

while(i<uzunluk):
    
    toplam += liste[i]
    i += 1
    
print(toplam)   



# range  (23.Ders)

range(10)
print(*range(10))

print(*range(3,12,2))

liste = list(range(10))

for i in range(10):
    
    print(i)
    
print("#"*30)

for i in range(5,30,3):
    print(i)
    
    
    
liste2 = ["ali","veli","ahmet","ömer"]

for i in range(len(liste2)):
    
    print(i,liste2[i])
    
print(*range(4))    

    
print(*range(2,3))   


# break & continue  (24.Ders)


i = 0

while(i<10):
    
    print(i)
    i += 1
        
    
i = 0

while(i<10):
    
    print(i)
    i += 1
    
    if i == 6:
        break
    
    
    
i = 0

while(i<10):
    
    print(i)
    
    if i == 6:
        break
    
    
    i += 1
    
liste = [1,2,3,4,5,6,7,8]

for i in liste :
    
    print(i)  
    
    if i % 5 == 0:
        break
    
while True:
    
    kullanici_adi = input("Kullanıcı adi giriniz : ")
    
    if len(kullanici_adi) < 3 :
        
        print("yanlış giriş yaptınız..")
        break
    print("Hoş geldiniz {}".format(kullanici_adi))
    
#
    
liste2 = [1,2,3,4,5,6,7]

for i in liste :
    
    if i == 4 or i == 7:
        
        continue
    
    
    print(i)
    
    
i = 0

while(i<10):
    
    if i == 4 :
        continue
    
    print(i)
    i += 1
    
    
    
i = 0

while(i<10):
    
    if i == 4 :
        i += 1
        continue
    
    print(i)
    i += 1    

    
    

    
    
    




    
    
    

    
        
    
    
    

    
        
    
    
    







    
    
    
       



  






















   
    
    