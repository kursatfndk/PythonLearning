#!/usr/bin/env python
# coding: utf-8

# # PYTHON PROGRAMLAMA DİLİ TEMELLERİ

# Best way to learn a language is to use it - Bir dili öğrenmenin en iyi yolu onu kullanmaktır...
# 1. Günlük kod yaz
# 2. İnteraktif çalış
# 3. 20-25 dk çalış ara ver.(örn. 2 saat kursa çalış. 2 saat kendin yaz Pekiştir.)
# 4. Hata yap ve çözüm bul. (hata yaptığında google ve çeşitli yerden araştır)
# 5. Çalışma arkadaşı bul.
# 6. Anladığınızı öğretmeye çalış.
# 7. Projeler yap.

# In[2]:


print("Kürşat Emre Fındık")


# In[3]:


print("Merhaba Dünya!")


# In[4]:


print "Yaz"


# In[5]:


print("Yaz")


# In[3]:


isim = input("İsminiz nedir?")
ikinci = input("İkinci ismin nedir?")
soy = input("Soyadınız nedir?")
print(isim+" "+ikinci+" "+soy)


# # DEĞİŞKENLER ve SABİTLER (VARİABLE and CONSTANTS)

# In[13]:


isim = "Kürşat"
soyisim = "Fındık"

print(isim)
print(soyisim)


# In[ ]:


PI = 3.14


# In[18]:


isim = "Ömer"


# In[19]:


print(isim)


# In[22]:


isim,soyisim = "Kürşat","Fındık"


# In[23]:


print(isim)


# In[24]:


isim,soyisim = soyisim,isim


# In[25]:


print(isim)


# In[26]:


print(soyisim)


# # değişkenlerde büyük küçük harf ve sayı kullanabilir. Özel karakter olmaz. İki kelimeliyse bitişik yada _ kullanmalı. Başlangıçta sayı kullanılmaz. Değişken isim atılmaz. Örn. Print
# 
# 

# In[ ]:


KullanıcıAdı =
Kullanıcı_Adı =


# In[4]:


1Kullanıcı_Adı =


# In[7]:


Print = "Ömer"
print(Print)


# ### Veri Tipleri(Data Types)

# -Numbers - sayılar
# -String -Karakter dizileri
# -Boolean - Doğru yanlış
# -List - Listeler
# -Tuple - Demetler
# -Dictionary - Sözcükler
# -Set - Kümeler

# ### Numbers (Sayılar)

# In[ ]:


Yas = 29


# In[ ]:





# In[8]:


5+15


# -İnteger - tam sayı  5
# -float -ondalık 5.56
# -long - uzun sayı 519654892L
# -complex - Karmaşık sayı 3.14j

# In[9]:


5+6.98


# In[12]:


4**2 #4ün üssü 


# In[13]:


40//6 # bölüyor noktasız kısmı alıyor


# In[15]:


round(4.56) #yuvarlama fonksiyonu round


# ### String (karakter dizileri)

# In[ ]:


'Kürşat'
"Kürşat"
"""Kürşat"""


# In[ ]:


isim = "Kürşat Fındık"


# In[16]:


isim[1]


# In[17]:


isim[0]


# In[18]:


isim[-1]


# In[19]:


isim[0:4]


# In[20]:


isim[0:8:2]


# In[21]:


isim


# In[25]:


'Türkiye'nin en büyük ili İstanbul' #Tırnaklar arası karmaşa oldu


# In[26]:


'Türkiye\'nin en büyük ili İstanbul' #\işareti python a aradığının bir sonraki karakterde olmadığını anlatıyor


# In[27]:


"Türkiye'nin en büyük ili İstanbul" #yada " çift tırnak kullanırsak da olur.


# In[31]:


print ('Türkiye\'nin en büyük\n ili\n İstanbul') #\n ifadesinden sonrasını alt satıra getirir.


# In[39]:


print ("Türkiye\t'nin en büyük\n ili\n İstanbul") #\t bir satır boşluk atar


# # Methodlar

# ### .upper() , .lower() , .capitalize() , .count("") , .find("") , .index("") , .lstrip() , .rstrip() , .strip() , .replace(" "," ")

# In[34]:


"Kürşat" +" Fındık"


# In[38]:


"Kürşat Fındık".upper #.upper ifadesi harfleri büyütür


# In[37]:


'KÜRŞAT FINDIK'.lower() # .lower yazarsak harfleri küçültür.


# In[43]:


"kürşat fındık".capitalize() #.capitalize yazarsak ilk harfi büyütür.


# In[52]:


ad = "kürşat fındık"


# In[54]:


yeni_ad = ad.upper()


# In[56]:


print(yeni_ad)


# In[57]:


ad


# In[58]:


yeni_ad


# In[76]:


ad.count("k") #.count kaç tane harf varsa söyler


# In[77]:


ad.find("fındık") #.find karakterin hangi sırada olduğunnu söyler


# In[78]:


ad.index("k") # .index ilk bulduğu sırayı söyler


# In[79]:


yeni = "      Kürşat Fındık       "


# In[80]:


yeni.lstrip() # .lstirp yazarsak soldaki boşluğu siler


# In[81]:


yeni.rstrip() # .rstrip yazarsak sağdaki boşluğun siler


# In[82]:


yeni.strip() # .strip yazarsak iki taraftaki boşluğu siler


# In[85]:


ad.replace("Fındık","Tek")


# In[90]:


isim = "kürşat"
soyisim = "Fındık"


# In[91]:


print("Benim ismim {} soyadım {} ".format(isim,soyisim))


# # Boolean Veri Tipi

# ### < , > , == , <= , >= , != , True False ifadelerini bulmak için kullanılır.

# In[13]:


5 > 4


# In[15]:


7 < 5


# In[16]:


5 == 5


# In[17]:


5 ==7


# In[18]:


7 >= 7


# In[19]:


7 >= 5


# In[20]:


7 >= 9


# In[23]:


6 != 6 # != eşit değilmidir sorusunu sorar. 


# In[24]:


6 != 5


# # Liste Veri Tipi (Lists)

# ### len (fonksiyonu) , .append() , .remove() , .pop() , .copy() , .extend() , .count() .index(), .insert(1,1) , .sort() , .reverse() , .clear()

# In[25]:


insan = ["Kürşat","fındık",23,"Python"]


# In[26]:


insan


# In[27]:


insan[1]


# In[28]:


insan[0]


# In[29]:


insan[3]


# In[30]:


insan[0:4]


# In[31]:


insan[0:4:2]


# In[1]:


isim = "Kürşat"


# In[32]:


isim[0] = "t"


# In[33]:


insan[0] 


# In[34]:


insan[0] = "ömer"


# In[35]:


insan


# In[37]:


insanlar = [("Kürşat","Fındık"),("Ömer","Çevikel"),("Ahmet","Gündoğdu")]


# In[38]:


insanlar


# In[39]:


insanlar[0]


# In[40]:


insanlar[0][1]


# In[41]:


insanlar[0][0]


# In[43]:


len(insanlar) #kaç elemandan oluştuğunu söyler


# In[44]:


len(insan)


# In[45]:


sayılar =[1,2,3,4,5,6,85,78,956,7852,8]


# In[46]:


len(sayılar)


# In[47]:


sayılar[-2]


# In[48]:


sayılar[0]


# In[49]:


sayılar[2:11:2]


# In[52]:


sayılar[2:] #yerleştirmelere göre : sadece iki nokta üst üste kullanarak sağındaki ve solundaki değerleri alır


# In[53]:


sayılar[:2]


# In[54]:


sayılar.append(3000) #.append() değeri listeye ekler


# In[55]:


sayılar


# In[56]:


sayılar.remove(5) #.remove değeri listeden kaldırır


# In[57]:


sayılar


# In[59]:


sayılar.pop() #.pop yazdırıldığında son elemanı verir. Listeden bu elemanı çıkarır. not: tekrardan shift+enter yaptığım için bir sonrakini de listeden çıkardı.


# In[60]:


sayılar


# In[61]:


sayılar.pop()


# In[62]:


sayılar


# In[63]:


sayılar.pop(4)


# In[65]:


sayılar


# In[66]:


sayılar.copy() # .copy listeyi kopyalar.


# In[67]:


yeni = sayılar.copy()


# In[68]:


yeni


# In[71]:


a = [1,2,3,4]
b = [5,6,7,8]


# In[72]:


a + b


# In[75]:


c = [1,2,3,4]
d = [5,6,7,8,9]


# In[76]:


c.extend(d) #.extend listeleri birleştirmek için kullanılır.


# In[77]:


c


# In[78]:


d = [5,6,7,8,9,10,10,10]


# In[79]:


d.count(10) # .count kaç tane geçtiğini belirtir.


# In[81]:


d.index(7) # .index kaçıncı sırada olduğunu söyler.


# In[84]:


d.insert(3,"min") # . insert listeye eklemek için kullanılır. kaçıncı elemana geçeceğini belirtmek ve ne geçmesi gerektiği belirtmek gerekir.


# In[85]:


d


# In[86]:


g = [9,5,7,8,3,28,36,15,99,87]


# In[87]:


g.sort() #sıralamak için kullanılır


# In[88]:


g


# In[89]:


g.sort(reverse = True)


# In[90]:


g


# In[94]:


isimler = [("Kürşat"),("Ahmet"),("Ömer"),("Faruk")]


# In[95]:


isimler.sort() #sort alfabeye göre yapar


# In[96]:


isimler


# In[97]:


isimler.reverse() #yazılan listeyi tersten yazar


# In[98]:


isimler


# In[99]:


isimler.sort(reverse=True) #alfabeye göre tersten sıralınış için


# In[100]:


isimler


# In[103]:


isimler.clear() #listenin içini siler


# In[104]:


isimler


# # Sözlükler (Dictinory)

# ### süslü parantez kullanılır.{} sözlük bölümüne liste değeri verilemez. .keys() .values() .items() .get() .update({}) .copy() .pop() .clear()

# In[3]:


kimlik = {"isim":"Kürşat",
          "soyisim":"Fındık",
          "tc_no":67578765682,
         "yer":"İstanbul"
}


# In[5]:


kimlik["yer"]


# In[6]:


kimlik["isim"]


# In[7]:


len(kimlik)


# In[8]:


kimlik


# In[9]:


kimlik["yıl"] = 2002


# In[10]:


kimlik


# In[12]:


kimlik.keys() #anahtar kelimeleri getiriri


# In[16]:


kimlik.values() #anahtar kelimenin içindeki kelimeyi getirir. değerleri verir


# In[17]:


kimlik.items() #keys  values şeklinde karşımıza getirir.


# In[19]:


kimlik.get("yer") #anahtarlara göre değeri getirir.


# In[21]:


kimlik.update({"anne_adı":"hatice"})


# In[22]:


kimlik


# In[23]:


kimlik.copy()


# # Demetler (Tuple)

# ### Demetler değiştirilemez. Listelerle neredeyse aynı. Listeler köşeli parantezken demetler yuvarlak parantez kullanır. Bütün indexleme işlemleri geçerlidir.

# In[30]:


zamirler = ("ben","sen","o","biz","siz","onlar")


# In[31]:


zamirler


# In[32]:


zamirler[0]


# In[33]:


zamirler[0] = "kem"


# In[34]:


len(zamirler)


# In[35]:


sayılar = (1,2,3,4,5,6,7)


# In[36]:


zamirler + sayılar


# In[37]:


sayılar.count(7)


# In[38]:


sayılar.index(4)


# In[44]:


t = (4)


# In[45]:


t


# In[46]:


t = (4,)


# In[47]:


t


# # Kümeler(Sets)

# #### kümelerde değişiklik yapılamaz.aynı eleman 1 kez geçer. .add() .discard() .remove() .update() .difference()

# In[2]:


sayı = {1,2,5,7,6,6,6,78,9,85,136}


# In[3]:


sayı


# In[4]:


sayı[2]


# In[5]:


sayı.add(100) #eklemek için kullanılır


# In[6]:


sayı


# In[7]:


sayı.discard(7) #silmek için kullanılır. içine elemena yazmasakta olur.


# In[8]:


sayı


# In[10]:


sayı.remove(5) #silmek için kullanılır içine eleman eklemek lazım


# In[11]:


sayı


# In[12]:


yeni = {11,31,41,51,61,10,9,85,165} #yeni sayılar eklendiğinde aynı eleman varsa kümelerde kesişim olduğunda yazdırırken aynı elemanlar 1 kez yazar.
sayı.update(yeni)


# In[13]:


sayı


# In[15]:


a = {1,2,3,4,5,6}
b = {4,5,6,7,8,9}


# In[16]:


a.difference(b) #a ve b kümesindeki farklılıkları bulmak için kullanılır.


# In[17]:


a.intersection(b) #iki kümenin kesişimini bulur


# In[18]:


a.union(b) #elemanları 1 kez kullanarak birleştirdi.


# In[19]:


len(a)


# ### Veri tipleri arasında dönüşümler

# In[20]:


a = 9


# In[21]:


type(a)


# In[23]:


a = 9.9


# In[24]:


type(a)


# In[25]:


str(a) #string yapar.


# In[26]:


b = "5.7"


# In[27]:


a + b


# In[31]:


d = float(b)


# In[32]:


a + d


# In[33]:


int(d)


# In[34]:


type(d)


# In[35]:


x = [3,6,8,9,4,3]


# In[36]:


tuple(x)


# In[37]:


set(x)


# In[38]:


dict(x = 7, y = 9)


# In[39]:


t = (5,6,7,8,9,3)


# In[40]:


y = list (t)


# In[41]:


y


# In[42]:


type(y)


# # Mantık Operatörleri

# In[48]:


5 < 10 and 3 < 8 


# In[50]:


5 > 10 and 3 > 8


# In[51]:


5 < 10 and 3 > 8


# In[52]:


5 < 10 or 3 < 8 


# In[53]:


5 > 10 or 3 < 8 


# In[54]:


not 5 > 3


# In[55]:


not 5 < 3


# ### Aitlik operatörleri

# In[56]:


b =[3,5,7,8]


# In[58]:


5 in b #in içerisinde varmı sorusu sorar


# In[59]:


6 in b


# In[60]:


6 not in b


# In[61]:


5 not in b


# ### Atama operatörleri

# In[62]:


b = 4


# In[63]:


b = b + 5


# In[64]:


b


# In[65]:


b += 5


# In[66]:


b


# In[67]:


b -= 5


# In[68]:


b


# In[69]:


b *= 5


# In[70]:


b


# In[71]:


b /= 5


# In[72]:


b


# In[73]:


b //= 3


# In[74]:


b


# In[75]:


b %= 2


# In[76]:


b


# # IF Koşul İfadesi 
# (Eğer Koşulu)
# : ifadesi ise demektir.

# In[1]:


if 5 > 3:
    print("Beş büyüktür üç")
else:
    print("Yanlış")


# In[2]:


if 5 > 6:
    print("Beş büyüktür üç")
else:
    print("Yanlış")


# In[4]:


kullanıcı_adı = "kürşatfındık"
sifre = "12345"
if kullanıcı_adı =="kürşatfındık":
    print("Kullanıcı adı doğru.")
else:
    print("Yanlış kullanıcı adı")


# In[5]:


kullanıcı_adı = "kürşatfındık1"
sifre = "12345"
if kullanıcı_adı =="kürşatfındık":
    print("Kullanıcı adı doğru.")
else:
    print("Yanlış kullanıcı adı")


# In[6]:


kullanıcı_adı = input("Kullanıcı adı giriniz")
if kullanıcı_adı =="kürşatfındık":
    print("Kullanıcı adı doğru.")
else:
    print("Yanlış kullanıcı adı")


# In[10]:


kullanıcı_adı = "kürşatfındık1"
sifre = "12345"

ad =  input("Kullanıcı adı giriniz")
sifre_gir =  input("Kullanıcı adı giriniz")

if kullanıcı_adı == ad:
    print("Hoşgeldiniz Kürşat Fındık")
else:
    print("Yanlış yada hatalı tuşlama yaptınız")

if sifre == sifre_gir:
    print("Şifre doğru")
else:
    print("Dalga mı geçiyosun birader")


# In[12]:


kullanıcı_adı = "kürşatfındık1"
sifre = "12345"

ad =  input("Kullanıcı adı giriniz")
sifre_gir =  input("Kullanıcı adı giriniz")

if kullanıcı_adı == ad and sifre == sifre_gir:
    print("Hoşgeldiniz Kürşat Fındık")
else:
    print("Yanlış yada hatalı tuşlama yaptınız")


# In[13]:


kullanıcı_adı = "kürşatfındık1"
sifre = "12345"

ad =  input("Kullanıcı adı giriniz")
sifre_gir =  input("Kullanıcı adı giriniz")

if kullanıcı_adı == ad and sifre == sifre_gir:
    print("Hoşgeldiniz Kürşat Fındık")
else:
    print("Yanlış yada hatalı tuşlama yaptınız")


# ### Elif ifadesi

# In[18]:


kullanıcı_adı = "kürşatfındık1"
sifre = "12345"

ad =  input("Kullanıcı adı giriniz")
sifre_gir =  input("Şifrenizi giriniz")

if kullanıcı_adı == ad and sifre == sifre_gir:
    print("Hoşgeldiniz Kürşat Fındık")
elif kullanıcı_adı != ad:
    print("kullanıcı adınız yanlış")
else:
    print("Şifreniz yanlış")


# In[17]:


kullanıcı_adı = "kürşatfındık1"
sifre = "12345"

ad =  input("Kullanıcı adı giriniz:")
sifre_gir =  input("Şifrenizi giriniz:")

if kullanıcı_adı == ad and sifre == sifre_gir:
    print("Hoşgeldiniz Kürşat Fındık")
elif kullanıcı_adı != ad:
    print("kullanıcı adınız yanlış")
else:
    print("Şifreniz yanlış")


# In[19]:


kullanıcı_adı = "kürşatfındık1"
sifre = "12345"

ad =  input("Kullanıcı adı giriniz:")
sifre_gir =  input("Şifrenizi giriniz:")

if kullanıcı_adı == ad and sifre == sifre_gir:
    print("Hoşgeldiniz Kürşat Fındık")
elif kullanıcı_adı != ad:
    print("kullanıcı adınız yanlış")
else:
    print("Şifreniz yanlış")


# In[23]:


ders_notu = int(input("Notunuzu Girin : "))
if ders_notu >= 90 and ders_notu <= 100:
    print("AA aldınız")
elif ders_notu >= 80 and ders_notu < 90:
    print("BB aldınız")
elif ders_notu >= 70 and ders_notu < 80:
    print("CC aldınız")
elif ders_notu >= 60 and ders_notu < 70:
    print("DD aldınız")
elif ders_notu >= 50 and ders_notu < 60:
    print("FF aldınız")
elif ders_notu < 50: 
    print("Dersten Kaldınız")
else:
    print("Geçerli bir değer girin")


# In[24]:


ders_notu = int(input("Notunuzu Girin : "))
if ders_notu >= 90 and ders_notu <= 100:
    print("AA aldınız")
elif ders_notu >= 80 and ders_notu < 90:
    print("BB aldınız")
elif ders_notu >= 70 and ders_notu < 80:
    print("CC aldınız")
elif ders_notu >= 60 and ders_notu < 70:
    print("DD aldınız")
elif ders_notu >= 50 and ders_notu < 60:
    print("FF aldınız")
elif ders_notu < 50: 
    print("Dersten Kaldınız")
else:
    print("Geçerli bir değer girin")


# In[25]:


ders_notu = int(input("Notunuzu Girin : "))
if ders_notu >= 90 and ders_notu <= 100:
    print("AA aldınız")
elif ders_notu >= 80 and ders_notu < 90:
    print("BB aldınız")
elif ders_notu >= 70 and ders_notu < 80:
    print("CC aldınız")
elif ders_notu >= 60 and ders_notu < 70:
    print("DD aldınız")
elif ders_notu >= 50 and ders_notu < 60:
    print("FF aldınız")
elif ders_notu < 50: 
    print("Dersten Kaldınız")
else:
    print("Geçerli bir değer girin")


# In[26]:


ders_notu = int(input("Notunuzu Girin : "))
if ders_notu >= 90 and ders_notu <= 100:
    print("AA aldınız")
elif ders_notu >= 80 and ders_notu < 90:
    print("BB aldınız")
elif ders_notu >= 70 and ders_notu < 80:
    print("CC aldınız")
elif ders_notu >= 60 and ders_notu < 70:
    print("DD aldınız")
elif ders_notu >= 50 and ders_notu < 60:
    print("FF aldınız")
elif ders_notu < 50: 
    print("Dersten Kaldınız")
else:
    print("Geçerli bir değer girin")


# In[27]:


ders_notu = int(input("Notunuzu Girin : "))
if ders_notu >= 90 and ders_notu <= 100:
    print("AA aldınız")
elif ders_notu >= 80 and ders_notu < 90:
    print("BB aldınız")
elif ders_notu >= 70 and ders_notu < 80:
    print("CC aldınız")
elif ders_notu >= 60 and ders_notu < 70:
    print("DD aldınız")
elif ders_notu >= 50 and ders_notu < 60:
    print("FF aldınız")
elif ders_notu >= 0 and ders_notu < 50:
    print("Dersten Kaldınız")
else:
    print("Geçerli bir değer girin")


# In[28]:


if 5 > 3 : print("5 büyüktür üç")


# In[29]:


print("5 büyüktür üç") if 5 > 3 else print("Yanlış")


# In[30]:


print("5 büyüktür üç") if 1 > 3 else print("Yanlış")


# In[33]:


sayı = int(input("Bir sayı giriniz : "))

if sayı >=0:
    if sayı == 0:
        print("sayı sıfırdır")
    else:
        print("sayı pozitiftir")
else:
    print("sayı negatiftir")


# In[35]:


if 3 >1:     #pass ifadesi sonradan doldurulacak kodlar için kullanılır. kodun yanlış çalışmasını engeller.
    pass     #pass kodu pasife alır.


# # Döngüler-For ve While

# In[ ]:


x = 3  #çalıştırdığımızda sonsuz sayıda x büyüktür 3 yazar çünkü while ile döngüye alır

while x > 3:
    print"(x büyüktür 3")


# In[5]:


x = 0

while x < 10:
    print("Bizim sayımız = ", x)
    x += 1


# In[6]:


x = 0

while x < 10:
    print("Bizim sayımız = ", x)
    x += 1

else:
    print("Sayımız 10 dan büyük")


# In[7]:


x = 0  #break döngüyü sonlandırmaya yarar. break kesmek anlamına gelir

while x < 10:
    print("Bizim sayımız = ", x)
    if x == 5:
        break
    x += 1

else:
    print("Sayımız 10 dan büyük")


# In[ ]:


x = 0  # Döngüyü sonlandırmaz hep başa döner

while x < 10:
    print("Bizim sayımız = ", x)
    if x == 5:
        continue
    x += 1

else:
    print("Sayımız 10 dan büyük")


# In[13]:


x = 0  

while x < 10:
    x += 1
    if x == 5:
        print("Bizim sayımız = ", x)
        continue
    x += 1

else:
    print("Sayımız 10 dan büyük")


# In[18]:


sayılar = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]


# In[19]:


1 in sayılar


# In[21]:


for sayı in sayılar:
    print("Sayımız =", sayı)
else:
    print("Döngü bitti")


# In[22]:


for sayı in sayılar:
    print("Sayımız =", sayı)
    if sayı == 10:
        break
else:
    print("Döngü bitti")


# In[31]:


for sayı in sayılar:
    if sayı == 10:
        continue
    print("Sayımız = ", sayı)
                
else:
    print("Döngü bitti")


# In[34]:


yeni = [1,2,3]


# In[35]:


for sayı in sayılar:
    for x in yeni:
        print(x)
else:
    print("Döngü bitti")


# In[38]:


for i in range(1,20):
    print(i)


# In[39]:


list(range(1,20))


# In[40]:


renkler = ["sarı","yeşil","siyah","mavi","kırmızı","siyah"]


# In[41]:


renkler[0]


# In[42]:


renkler[1]


# In[43]:


for renk in renkler:
    print(renk)


# In[45]:


gelirler = [2000,3000,4000,5000,6569,7000]


# In[46]:


for gelir in gelirler:
    print(gelir)


# In[47]:


for gelir in gelirler:
    print(gelir*2)


# # Fonksiyonlar (Functions)

# In[52]:


def kare_al(x): #x parametredir. def ile fonksiyona çevirebiliyoruz.
    print(x**2)


# In[53]:


kare_al(5) #5 burada argüman olmuş olur.


# In[54]:


kare_al(10)


# In[55]:


def alan(r,pi): 
    print(pi*r**2)


# In[56]:


alan(4)


# In[57]:


alan(4,3.14)


# In[58]:


alan(10,3.14)


# In[59]:


def alan(r,pi = 3.14): 
    print(pi*r**2)


# In[60]:


alan(6)


# In[61]:


print("Kürşat","Fındık")


# In[66]:


print("Kürşat","Fındık",sep="/",end=":jasndj")


# In[68]:


print("Kürşat","Fındık",sep="/",end="\n")


# In[10]:


def alan(r,pi = 3.14): #return ile fonksiyone değer atanır.
    return pi*r**2


# In[11]:


alan1 = alan(6)


# In[12]:


alan2 = alan(8)


# In[13]:


alan1 + alan2


# In[15]:


def asklmfklsmd(): #pass güncelleme yapacağımız kodu belirlememize yardımcı olur.
    pass #pass ifadesi yazdığımız kodu atlamamızı sağlar. ileride bu koda dönebiliriz.


# In[21]:


def cift_mi(x):
    if x % 2 ==0:
        print("Bu sayı çifttir")
    else:
        print("Bu sayı çift değildir")


# In[22]:


cift_mi(10)


# In[23]:


cift_mi(3)


# In[24]:


cift = cift_mi(10)


# In[25]:


type(cift)


# In[26]:


def cift_mi(x):
    if x % 2 ==0:
        return "Bu sayı çifttir"
    else:
        return "Bu sayı çift değildir"


# In[27]:


cift_mi(8)


# In[29]:


cift = cift_mi(8)


# In[30]:


type(cift)


# In[33]:


print()


# In[34]:


help(print)


# In[40]:


def kimlik(isim = "Boş",soyisim = "Boş",yaş = "Boş",kimlik = "Boş"):
    print("isim:",isim , "soyisim:",soyisim , "yaş:",yaş , "TC no:",kimlik)


# In[38]:


kimlik("Kürşat","Fındık",23,1548954541)


# In[39]:


kimlik("Kürşat","Fındık",23) #bu tarz sorunla karşılaşmamak için her değere defult parametre verebiliriz.
# = "Boş" gibi


# In[41]:


kimlik("Kürşat","Fındık",23)


# In[43]:


kimlik(isim = "Kürşat",yaş = 23,kimlik = 1548954541)


# # Python ile Nesne Tabanlı Programlama(Object Oriented Programing)

# özellikler (attributes) davranışlar (methods)
# - Nesne nedir?
# - Örnekle anlatım - Okul - Öğretmen, öğrenci, yönetim, hizmetliler ve veliler
# - class
#   

# In[45]:


isim = "Kürşat" #string bir obje


# In[46]:


isim.upper() #bu tarz methodları var görmüştük.


# In[ ]:


bir_isim = "kürşat"
bir_soyisim = "fındık"
bir_yaş = 23
bir_not_ort = 90

iki_isim = "ömer"
iki_soyisim = "çevikel"
iki_yaş = 26
iki_not_ort = 80

üç_isim = "ahmet"
üç_soyisim = "gündoğdu"
üç_yaş = 32
üç_not_ort = 95

dört_isim = "mustafa"
dört_soyisim = "yılmaz"
dört_yaş = 23
dört_not_ort = 75


# In[47]:


class Öğrenci:
    isim = "kürşat"
    soyisim = "Fındık"
    yaş = 23
    not_ort = 90
    


# In[48]:


bir = Öğrenci()


# In[49]:


bir.isim


# In[50]:


bir.yaş


# In[51]:


iki = Öğrenci()


# In[52]:


iki.isim


# ### Initializer or Constructor

# Bizim sınıfımızın ana yapısını başlatan bir metot ==> __init__()
# self. İfdesi nesnenin anlamında kullanılır. Örn: nesnenin_isim == self.isim

# In[53]:


class Ogrenci:
    def __init__(self,isim,soyisim,yaş,not_ort):
        self.isim = isim
        self.soyisim = soyisim
        self.yaş = yaş
        self.not_ort = not_ort


# In[54]:


bir = Ogrenci("kürşat","fındık",23,90)


# In[55]:


bir.isim


# In[56]:


iki = Ogrenci("ali","yılmaz",20,80)


# In[57]:


iki.isim


# In[59]:


iki = Ogrenci("ali","yılmaz",20,80)
iki = Ogrenci("ali","yılmaz",20,80)
iki = Ogrenci("ali","yılmaz",20,80)
iki = Ogrenci("ali","yılmaz",20,80)
iki = Ogrenci("ali","yılmaz",20,80)
iki = Ogrenci("ali","yılmaz",20,80)
iki = Ogrenci("ali","yılmaz",20,80)


# In[60]:


class Ogrenci:
    def __init__(self,isim,soyisim,yaş,not_ort):
        self.isim = isim
        self.soyisim = soyisim
        self.yaş = yaş
        self.not_ort = not_ort

    def info(self):
        print("{} {} {} yaşında ve {} ortalamaya sahip bir öğrencidir".format(self.isim,self.soyisim,self.yaş,self.not_ort))


# In[61]:


bir = Ogrenci("ali","yılmaz",20,80)


# In[62]:


bir.isim


# In[64]:


bir.info()


# In[70]:


class Ogretmen:
    def __init__(self,isim,soyisim,yaş,maaş,uzmanlık):
        self.isim = isim
        self.soyisim = soyisim
        self.yaş = yaş
        self.maaş = maaş
        self.uzmanlık = uzmanlık

    def info(self):
        print("{} {} {} yaşında ve {} maaşı olan bir {} öğretmenidir".format(self.isim,self.soyisim,self.yaş,self.maaş,self.uzmanlık))

    def zam(self):
        return self.maaş * 1.3


# In[71]:


ali = Ogretmen("ali","yıldız",45,5000,"Fizik")


# In[72]:


ali.info()


# In[73]:


ali.zam()


# ## 1.Encapsulation-Kapsülleme(Erişimi Engelleme)

# -Set
# -get
# __:erişimi direk engellemek için.

# In[4]:


class Ogretmen:
    def __init__(self,isim,soyisim,yaş,maaş,uzmanlık):
        self.isim = isim
        self.soyisim = soyisim
        self.yaş = yaş
        self.__maaş = maaş #__ erişimi engeller
        self.uzmanlık = uzmanlık

    def info(self):
        print("{} {} {} yaşında ve {} maaşı olan bir {} öğretmenidir".format(self.isim,self.soyisim,self.yaş,self.maaş,self.uzmanlık))

    def zam(self):
        return self.maaş * 1.3


# In[5]:


ali = Ogretmen("ali","yıldız",45,5000,"Fizik")


# In[6]:


ali.maaş


# In[7]:


class Ogretmen:
    def __init__(self,isim,soyisim,yaş,maaş,uzmanlık):
        self.isim = isim
        self.soyisim = soyisim
        self.yaş = yaş
        self.__maaş = maaş #__ erişimi engeller
        self.uzmanlık = uzmanlık

    def info(self):
        print("{} {} {} yaşında ve {} maaşı olan bir {} öğretmenidir".format(self.isim,self.soyisim,self.yaş,self.maaş,self.uzmanlık))

    def zam(self):
        return self.maaş * 1.3

    def getMaaş(self):
        return self.__maaş
    def setMaaş(self,yeni_maaş):
        self.__maaş = yeni_maaş


# In[8]:


ali = Ogretmen("ali","yıldız",45,5000,"Fizik")


# In[10]:


ali.getMaaş() #. kısmına gelince taba bastığımızda get maaşı seçebiliriz.


# In[11]:


ali.setMaaş(10000)


# In[12]:


ali.getMaaş()


# In[13]:


class Ogretmen:
    def __init__(self,isim,soyisim,yaş,maaş,uzmanlık):
        self.isim = isim
        self.soyisim = soyisim
        self.yaş = yaş
        self.__maaş = maaş #__ erişimi engeller
        self.uzmanlık = uzmanlık

    def info(self):
        print("{} {} {} yaşında ve {} maaşı olan bir {} öğretmenidir".format(self.isim,self.soyisim,self.yaş,self.maaş,self.uzmanlık))

    def __zam(self):
        return self.__maaş * 1.3

    def getMaaş(self):
        return self.__maaş
    def setMaaş(self,yeni_maaş):
        self.__maaş = yeni_maaş


# In[14]:


ali = Ogretmen("ali","yıldız",45,5000,"Fizik")


# In[ ]:


ali.__zam


# ## 2.Inheritance-Kalıtım

# -Aynı özellik ve metodlar tekrar etmemek için bir ana sınıf oluşturuyoruz. alt sınıftan bazı özellik ve metodları miras alıyor
# -İsterseniz alt sınıfa istediğiniz özelliği ve metodu ekleyebilirsiniz.
# -Super() .__init__() ile ana sınıfın özelliklerini alabiliyoruz. Alt sınıfta tekrar tanımlamaya gerek kalmıyor

# In[16]:


class Okul:
    def __init__(self,isim,soyisim,yaş):
        self.isim = isim
        self.soyisim = soyisim
        self.yaş = yaş
        print("Okul sınıfı çalıştı")


# In[17]:


ahmet = Okul("Ahmet","Sağlam",45)


# In[18]:


ahmet.isim


# In[23]:


class Ogretmen(Okul):
    def __init__(self,isim,soyisim,yaş):
        super().__init__(isim,soyisim,yaş)
        print("Öğretmen sınıfı çalıştı")
    def info(self):
        print("{} {} {} yaşında olan bir öğretmenidir".format(self.isim,self.soyisim,self.yaş,))
        


# In[24]:


semih = Ogretmen("Semih","Saygın",56)


# In[25]:


semih.info()


# In[30]:


class Ogretmen(Okul):
    def __init__(self,isim,soyisim,yaş,maaş,uzmanlık):
        super().__init__(isim,soyisim,yaş)
        self.maaş = maaş
        self.uzmanlık = uzmanlık
        print("Öğretmen sınıfı çalıştı")
    def info(self):
        print("{} {} {} yaşında {} TL maaşı olan bir {}  öğretmenidir".format(self.isim,self.soyisim,self.yaş,self.maaş,self.uzmanlık))

    def zam(self):
        return self.maaş * 1.5


# In[31]:


semih = Ogretmen("Semih","Saygın",56,10000,"Fizik")


# In[32]:


semih.info()


# In[33]:


semih.zam()


# In[34]:


class Ogrenci(Okul):
    def __init__(self,isim,soyisim,yaş,not_ort):
        super().__init__(isim,soyisim,yaş)
        self.not_ort = not_ort
        print("öğrenci sınıfı çalıştı")
    def info(self):
        print("{} {} {} yaşında {} ortalaması olan bir öğrencidir".format(self.isim,self.soyisim,self.yaş,self.not_ort))


# In[35]:


ayşe = Ogrenci("ayşe","kılınç",18,95)


# In[36]:


ayşe.info()


# ## 3.Abstract Class (Soyut Sınıflar)

# In[7]:


from abc import ABC,absrtactmethod

class Hayvan(ABC):
    @absrtactmethod
    def yürü(self):
        print("hayvan yürüyor")
    @absrtactmethod
    def koş(self):
        print("hayvan koşuyor")


# In[8]:


aslan = Hayvan()


# In[4]:


aslan.yürü()


# In[9]:


from abc import ABC,absrtactmethod

class Hayvan(ABC):
    @absrtactmethod
    def yürü(self):
        print("hayvan yürüyor")
    @absrtactmethod
    def koş(self):
        print("hayvan koşuyor")

class Aslan(Hayvan):
    def yürü(self):
        print("aslan yürüyor")
    def koş(self):
        print("aslan koşuyor")


# ### Polymorphism -Çok Şekillilik

# In[32]:


class Okul:
    def __init__(self,isim,soyisim,yaş,maaş):
        self.isim = isim
        self.soyisim = soyisim
        self.yaş = yaş
        self.maaş =maaş
        print("Okul sınıfı çalıştı")

    def info(self):
        print("{} {} {} yaşında {} Tl maaşı olan bir okul elemanıdır".format(self.isim,self.soyisim.self.yaş,self.maaş))

    def zam(self):
        return self.maaş * 1.2
class Ogretmen(Okul):
    def __init__(self,isim,soyisim,yaş,maaş,uzmanlık):
        super().__init__(isim,soyisim,yaş,maaş)
        self.maaş = maaş
        self.uzmanlık = uzmanlık
        print("Öğretmen sınıfı çalıştı")
    def info(self):
        print("{} {} {} yaşında {} TL maaşı olan bir {}  öğretmenidir".format(self.isim,self.soyisim,self.yaş,self.maaş,self.uzmanlık))

    def zam(self):
        return self.maaş * 1.5

class Yonetim(Okul):
    def __init__(self,isim,soyisim,yaş,maaş,birim):
        super().__init__(isim,soyisim,yaş,maaş)
        self.maaş = maaş
        self.birim = birim
        print("Yönetim sınıfı çalıştı")
    def info(self):
        print("{} {} {} yaşında {} TL maaşı olan ve {}  olarak görev yapan yönetim elemanıdır".format(self.isim,self.soyisim,self.yaş,self.maaş,self.birim))

    def zam(self):
        return self.maaş * 2

class Hizmetli(Okul):
    def __init__(self,isim,soyisim,yaş,maaş):
        super().__init__(isim,soyisim,yaş,maaş)
        self.maaş = maaş
        print("Hizmetli sınıfı çalıştı")
    def info(self):
        print("{} {} {} yaşında {} TL maaşı olan bir hizmetlidir".format(self.isim,self.soyisim,self.yaş,self.maaş))

    def zam(self):
        return self.maaş * 3


# In[33]:


ahmet = Okul("ahmet","korkmaz",45,5000)


# In[34]:


ali = Ogretmen("ali","cesur",28,5000,"fizikçi")


# In[41]:


Kemal = Yonetim("kemal","büyük",48,5000,"Müdür")


# In[42]:


Osman = Hizmetli("osman","zengin",28,5000)


# In[43]:


ahmet.zam()


# In[44]:


ali.zam()


# In[46]:


Kemal.zam()


# In[47]:


Osman.zam()


# # *args and *kwargs

# *args and *kwargs allow you to pass multiple arguments or keyword arguments to a function

# ## Arbitrary Arguments, *args

# In[1]:


def topla(x,y):
    print(x + y)


# In[2]:


topla(4,9)


# In[3]:


def topla(x,y,z):
    print(x + y + z)


# In[4]:


topla(4,9,5)


# In[5]:


def topla(*args):
    print(args)


# In[6]:


topla(6,7,3,9)


# In[16]:


def topla(*args):   #önemli olan yıldız. *args yerine *numaralar da yazabilirim mesela
    toplam = 0
    for i in args:
        toplam = toplam + i
    print(toplam)


# In[17]:


topla(6,7,3,9)


# In[18]:


topla(6,7,3,9,10,47,85,95)


# In[21]:


def isim(*args):
    print("{} {} {} Python öğrencisi".format(args[0],args[1],args[2]))


# In[22]:


isim("Kürşat","Emre","Fındık")


# ## Arbitary Keyword Arguments,**Kwargs

# In[23]:


def kimlik(**kwargs):
    print("kwargs:",kwargs)


# In[24]:


kimlik(isim = "Kürşat",soyisim = "Fındık")


# In[25]:


def kimlik(**kwargs):
    for key in kwargs.keys():
        print("anahtarlar : ",key)


# In[26]:


kimlik(isim = "Kürşat",soyisim = "Fındık")


# In[27]:


def kimlik(**kwargs):
    for key,value in kwargs.items():
        print("anahtarlar : ",key , "değerler :" , value)


# In[28]:


kimlik(isim = "Kürşat",soyisim = "Fındık")


# In[29]:


def kimlik(**kwargs):
    for key,value in kwargs.items():
        print(" {} = {} " .format(key,value))


# In[30]:


kimlik(isim = "Kürşat",soyisim = "Fındık",yaş = 23, tc = 35489512541, email = "anonim@gmail.com")


# # Python Global and Local Variables

# ## Global Variables

# Python'da fonksiyonun dışında veya global kapsamda bildirilen bir değişken global bir değişken olarak bilinir. Bu, global değişkene fonksiyonun içinde veya dışında erişilebileceği anlamına gelir.

# In[31]:


x = 10

print(x)


# ## Local Variables

# fonksiyonun gövdesinde veya yerel kapsamda tanımlanan değişkene yerel değişken (Local Variables) denir.

# In[32]:


def fonksiyon():
    x = 5
    print(x)


# In[33]:


fonksiyon()


# # Lambda Function

# - Lambda fonksiyonu küçük anonim bir fonksiyondur.
# - Lambda fonksiyonu herhangi sayıda argüman alabilir, ancak yalnızca bir ifadeye sahip olabilir.
# - Bu fonksiyonu bir kez kullandığınızda lambdayı kullanın.

# In[1]:


def kare(x):
    return x**2


# In[2]:


kare(8)


# In[4]:


x = lambda x:x**2


# In[5]:


x(10)


# In[8]:


x = [1,2,3,4,5,6,7,8,9,10] #filter() fonksiyonunu kullandık

list(filter(lambda x:(x%2==0) ,x))


# In[11]:


x = [1,2,3,4,5,6,7,8,9,10] #map() fonksiyonunu kullandık
list(map(lambda x:x**2 ,x))


# # Some Built-in Functions (Gömülü fonksiyonlar)

# abs() bir sayının mutlak değerini döndürür.

# In[12]:


abs(-7.5)


# bin) bir sayının ikili versiyonunu döndürür

# In[13]:


bin(4)


# enumerate() bir koleksiyon (örneğin bir tuple) alır ve onu bir numaralandırma nesnesi olarak döndürür.

# In[16]:


renkler =["sarı","beyaz","kırmızı","yeşil","siyah"]


# In[17]:


x = enumerate(renkler)


# In[18]:


list(x)


# In[19]:


for index,renk in enumerate(renkler):
    print(index,renk)


# - max() bir yenileyicideki en büyük fonksiyonu döndürür.
# - max() fonksiyonu en yüksek değere sahip öğeyi veya yinelemeli bir öğedeki en yüksek değere sahip öğeyi döndürür.
# değerler dizelerse alfabetik bir karşılaştırma yapılır.

# In[20]:


x =[2,3,7,12,35]


# In[21]:


max(x)


# In[22]:


y = ["c","s","h","v","l"]


# In[23]:


max(y)


# min() bir yinelemedeki en küçük ögeyi döndürür.
# 

# In[ ]:


x =[2,3,7,12,35]


# In[24]:


min(x)


# In[ ]:


y = ["c","s","h","v","l"]


# In[25]:


min(y)


# pow() x'in y kuvvetine göre değerini döndürür.Örn: 2 üssü 5 =32

# In[26]:


pow(2,5)


# In[28]:


pow(5,4,10) #5 in 4. kuvvetini aldı 10a böldü


# reversed() tersine çevrilmiş bir yineleyici döndürür.

# In[29]:


x = [2,3,7,12,35,5]


# In[30]:


y = reversed(x)


# In[31]:


list(y)


# round() bir sayıyı yuvarlar

# In[34]:


round(3.56874)


# In[36]:


round(3.56874,4) #virgülden sonra hangi değeri yazarsak o kısmın sonrasını yuvarlar.


# sorted() sıralanmış bir listeyi döndürür. dizeler alfabetik sayılar sayısal olarak sıralanır

# In[39]:


x = [2,3,7,12,35,5]


# In[41]:


sorted(x)


# In[42]:


sorted(x, reverse = True)


#  sum() bir yenleyicinin öğelerini toplar

# In[43]:


x = [2,3,7,12,35,5]


# In[44]:


sum(x)


# zip() iki veya daha fazla yineleyici döndürür

# In[ ]:


x = [2,3,5,7,12]
renkler =["sarı","beyaz","kırmızı","yeşil","siyah"]


# In[46]:


list(zip(x,renkler))


# # Modüller-Paketler ve kütüphaneler

# In[1]:


import math


# In[2]:


math.factorial(5)


# In[3]:


math.factorial(8)


# In[4]:


math.sqrt(5)


# In[5]:


math.pow(3,4)


# In[6]:


math.pi


# In[3]:


import math as mt #indirilen dosyayı çağırırken ismini 
#değiştirmek için as kullanılabilir.


# In[2]:


mt.pi


# In[3]:


from math import factorial #math modülünden sadece 1 
#fonksiyonu almak için kullanılır.*kullanırsak hepsini alır


# In[4]:


factorial(4)


# ### DateTime Modülü

# datetime,date ve time sınıflarıdır.

# In[5]:


import datetime


# In[6]:


datetime.datetime.now() #yıl ay gün saat dakika saniye mikrosaniye sırasıyladır.


# In[7]:


datetime.datetime.today()


# In[8]:


simdi = datetime.datetime.now()


# In[12]:


simdi.strftime("%d/%m/%Y %H:%M:%S")


# In[13]:


simdi.strftime("%d/%B/%Y %H:%M:%S")


# In[14]:


dir(datetime)


# In[1]:


from datetime import date


# In[2]:


date.today()


# In[3]:


bugün = date.today()


# In[4]:


bugün.day


# In[5]:


bugün.month


# In[6]:


bugün.year


# In[7]:


yeni = date(2018,6,23)


# In[8]:


yeni


# In[1]:


from datetime import time


# In[2]:


zaman = time(10,23,45,245)


# In[3]:


zaman.hour


# In[4]:


zaman.minute


# In[5]:


zaman.second


# In[6]:


zaman.microsecond


# In[7]:


print(zaman)


# In[8]:


zaman1 = date(2020,5,22)


# In[9]:


from datetime import date


# In[10]:


zaman1 = date(2020,5,22)


# In[11]:


zaman2 = date(2017,4,21)


# In[12]:


zaman1 - zaman2


# In[13]:


zaman3 = date(2025,6,12)


# In[14]:


zaman4 = date(2002,5,11)


# In[15]:


zaman3 - zaman4


# In[18]:


8433/365.25


# In[19]:


import time


# In[20]:


time.localtime()


# In[21]:


time.strftime("%d/%B/%Y %H:%M:%S")


# In[22]:


time.strftime("%H:%M:%S")


# In[23]:


time.strftime("%H:%M:%S")


# In[24]:


while True:
    zaman = time.strftime("%H:%M:%S")
    print(zaman)
    time.sleep(1)


# In[4]:


import HesapMakinesi #HesapMakinesi adında modül oluşturup buradaki fonksiyonları çağırdık.


# In[5]:


hesap = HesapMakinesi


# In[6]:


hesap.topla(5,6,7,8,89)


# import Anapaket.altpaket.modul

# # Hatalar ve İstisnalar

# try ve except, finnaly ve raise

# In[7]:


def topla(x,y):
print(x + y)


# In[8]:


if 5 > 1
    print("5 büyüktür 1")


# In[9]:


x = 5
y = "10"
x + y


# In[10]:


z + y


# In[11]:


x = int(input("bir sayı giriniz:"))
y = int(input("ikinci sayı giriniz:"))

x + y


# In[12]:


x = int(input("bir sayı giriniz:"))
y = int(input("ikinci sayı giriniz:"))

x / y


# In[15]:


try:
    x = int(input("bir sayı giriniz:"))
    y = int(input("ikinci sayı giriniz :"))
    x + y

except:
    print("hata oluştu")


# In[5]:


try:
    x = int(input("bir sayı giriniz:"))
    y = int(input("ikinci sayı giriniz :"))
    x / y

except ValueError:
    print("Lütfen bir sayı giriniz")
except TypeError:
    print("Verilerin Tipinde bir hata var")
except ZeroDivisionError:
    print("Sıfırdan farklı bir değer giriniz")


# In[6]:


try:
    x = int(input("bir sayı giriniz:"))
    y = int(input("ikinci sayı giriniz :"))
    print(x / y)

except ValueError:
    print("Lütfen bir sayı giriniz")
except TypeError:
    print("Verilerin Tipinde bir hata var")
except ZeroDivisionError:
    print("Sıfırdan farklı bir değer giriniz")
else:
    print("problem yok")


# In[7]:


try:
    x = int(input("bir sayı giriniz:"))
    y = int(input("ikinci sayı giriniz :"))
    print(x + y)

except:
    print("hata oluştu")
finally:
    print("ne olursa olsun çalışacak")


# In[8]:


try:
    x = int(input("bir sayı giriniz:"))
    y = int(input("ikinci sayı giriniz :"))
    print(x + y)

except:
    print("hata oluştu")
finally:
    print("ne olursa olsun çalışacak")


# In[10]:


x = int(input("bir sayı giriniz:"))

if x == 0:
    raise Exception("Lütfen 0 dan farklı bir değer giriniz")
else:
    print(x)


# In[13]:


class SıfırHatası(Exception):
    pass


# In[14]:


x = int(input("bir sayı giriniz:"))

if x == 0:
    raise SıfırHatası("Lütfen 0 dan farklı bir değer giriniz")
else:
    print(x)


# # Dosya İşlemleri

# open(), close(), read(), readlines(), with open()...as file,write()
# - seek() #istediğimiz karakter sayısına gider.
# - tell()  #kaçıncı karakterde olduğunu öğrenebilirsin
# - ayrıca hem okuma hemde yazma yapmak istiyorsak "+" işaretini kullanabiliriz.
# - "r+"hem okuma hem yazma(dosyanın var olması gerekir)
# - "w+"hem okuma hem yazma(dosya varsa siler)
# - "a+"eğer çağrılan dosya varsa en sondan ekler.yoksa yazma ve okuma yapacak yeni dosya oluşturur.
# - "x+"hem okuma hem yazma(dosya yoksa hata verir)

# In[7]:


dosya = open("dosya.txt",mode = "w",encoding = "utf-8")


# In[8]:


dosya.write("Merhaba, ben Kürşat Emre Fındık Python derslerimin sonuna yaklaştım İlerideki hedeflerimde kendimi geliştirip developer olmak")


# In[9]:


dosya.close()


# In[10]:


dosya = open("dosya.txt",mode = "a",encoding = "utf-8")


# In[11]:


dosya.write(" Pythonu çok seviyorum.")


# In[12]:


dosya.close()


# In[13]:


dosya = open("dosya.txt",mode = "x",encoding = "utf-8")


# In[14]:


dosya = open("dosya.txt",mode = "r",encoding = "utf-8")


# In[15]:


dosya.read()


# In[16]:


dosya.close()


# In[17]:


dosya = open("dosya.txt",mode = "r",encoding = "utf-8")


# In[18]:


for i in dosya:
    print(i)


# In[19]:


dosya.close()


# In[20]:


dosya = open("dosya.txt",mode = "r",encoding = "utf-8")


# In[21]:


dosya.readline()


# In[22]:


dosya.readline()


# In[23]:


dosya.readline()


# In[24]:


dosya.readline()


# In[25]:


dosya.readline()


# In[26]:


dosya.close()


# In[27]:


dosya = open("dosya.txt",mode = "r",encoding = "utf-8")


# In[28]:


dosya.readlines()


# In[30]:


liste = dosya.readlines()


# In[33]:


dosya.close()


# In[34]:


with open("cv.txt","w",encoding = "utf-8") as cv:
    cv.write("Merhaba, ben Kürşat Emre Fındık.")
    cv.write("Python derslerimin sonuna yaklaştım.")
    cv.write("İlerideki hedeflerimde kendimi geliştirip developer olmak.")


# In[35]:


with open("cv.txt","r",encoding = "utf-8") as cv:
    cv.seek(25)
    print(cv.read(37))
    print(cv.tell())


# In[36]:


with open("cv.txt","r+",encoding = "utf-8") as cv: #hem okuma hem yazma için r+
    print(cv.read(50))
    cv.write("hedeflerimde kendimi geliştirip developer olmak.")


# In[37]:


cv.close()


# # Iterator

# İterasyon: Bir objedeki elemanları sıralı şekilde ziyaret etme işlemi olarak tanımlayabiliriz.

# In[38]:


x = "Kürşat"


# In[40]:


for i in x:
    print(i)


# In[41]:


y = [1,2,3,4,8,9]


# In[42]:


for i in y:
    print(i)


# In[43]:


iterasyon = iter(x)


# In[44]:


next(iterasyon)


# In[45]:


next(iterasyon)


# In[46]:


next(iterasyon)


# In[47]:


next(iterasyon)


# In[48]:


next(iterasyon)


# In[49]:


next(iterasyon)


# In[50]:


next(iterasyon)


# In[51]:


iterasyon = iter(x)
while True:
    try:
        eleman = next(iterasyon)
        print(eleman)
    except StopIteration:
        break


# kendi iteratörlerimizi de yapabiliriz. __iter__() ve__next__()

# In[54]:


class Sayılar:
    def __iter__(self):
        self.sayı = 0
        return self

    def __next__(self):
        x = self.sayı
        self.sayı += 5
        return x

besartan = Sayılar()
iterasyon = iter(besartan)

print(next(iterasyon))
print(next(iterasyon))
print(next(iterasyon))
print(next(iterasyon))
print(next(iterasyon))


# # Generator(Üreteçler)

# Generatorlar iterable objeler oluşturmak için kullanılırlar. Bellekte yer tutmadıkları için son derece kullanışlıdırlar. 
# return yerine yield anahtar kelimesini kullanacağız

# In[59]:


def cift(sayı):
    cift_sayılar = []
    for i in range(sayı):
        cift_sayılar.append(i*2)
    return cift_sayılar
        


# In[60]:


cift(20)


# In[62]:


def cift(sayı):
    for i in range(sayı):
        yield i*2


# In[63]:


cift(20)


# In[64]:


for i in cift(1000):
    print(i)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




