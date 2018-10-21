# Introduce Python : Pythonic way, Guide of life to become the pythonist

## Prasyarat
  * Installed Python 3.* above (my recomendations 3.7), you can download [here](https://www.python.org/downloads/)

  * Text editor or IDE, everything you like it. an example vim, micro, nano, visual studio code, pycharm, Netbeans etc. (maybe i use jupyter notebook XD)

  * a cup of coffe and enjoy :D
  
  
  ### Preambule
  * sedikit perkenalan dengan python yang merupakan bahasa pemgrograman tingkat tinggi untuk general purpose dengan beberapa paradigma seperti functional, object oriented, imperative , procedural dsb, dan juga dengan beberapa disiplin penulisan seperti strong type, dan dynamic type, untuk lebih jelasnya bisa dicari di google yaa
  
  * Yunindyo Prabowo, [21.10.18 19:33]
seperti yang dijelaskan di tema , yaitu pythonic way , ada beberapa hal yg sebenernya bisa dianggap melenceng jauh dari bahasa python itu sendiri, mungkin sebagian temen-temen ada yang pernah menggunakan, sedang menggunakan, pertama kali penggunakan atau bahkan bahasa sekian yg dikuasi. beberapa kasus ini terutama yang masalah terakhir, yaitu python bahasa ke sekian yang dikuasi biasanya masih terbawa paradigma atau styling bahasa sebelumnya, saya bahkan bisa menebak hampir 80% temen2 disini pernah atau bahkan sampai saat ini masih menggunakan php

* Yunindyo Prabowo, [21.10.18 19:33]
nah setelah mencoba python biasanya styling phpnya masih terbawa sampai di python, sehingga banyak fitur2 python yg gak terpakai dan useless kalau boleh dibilang demikian

* Yunindyo Prabowo, [21.10.18 19:34]
case ini gak cuma php aja, bahkan hampir di semua case karena migrasi bahasa lain ke python

* nah pada malam ini saya mencoba untuk menjelaskan beberapa materi terutama dibagian struktur data , mengapa? karena struktur data itu bagian terpenting dalam program secara keseluruhan, dengan pendekatan pythonic way diharapkan temen2 bisa membedakan bagaimana bahasa satu dengan bahasa lainnya

* python tidak mengenal yg namanya semicolon atau ; , di python setiap line atau perintah dibedakan menggunakan identasi, 1 identasi dengan ukuran 4 spasi 

### basics syntax
```python
print ("hello world")

"""
Static Type an Example:
in c -- int angka=10;
"""
# variable
angka = 3 #dynamic type
kata = "aku"
print(angka, kata)

# assigment variable
c = angka
print(c)

#Error
d = angka + kata
print(d)
```
 #### variable
 * oke kita next, yaitu variable, dalam bahasa python variable di ketik langsung pada source tanpa mendefinisikan tipe datanya, berbeda dengan c atau java yang harus didefiniskan terlebih dahulu, ini merupakan salah satu perbedaan antara dynamic type (python) dan static type (java)

### Fungsi
Yunindyo Prabowo, [21.10.18 20:22]
seperti bahasa pemrograman pada umumnya, di python juga dikenal yang namanya function atau method, terdiri dari dua bagian utama, kepala fungsi dan badan fungsi yang dibedakan dengan identasi, bukan kurung kurawal atau kurung2 lainnya seperti bahasa pemgrograman c atau java atau php, formatnya, 


def namafungsi():
       badanfungsi
       
       
sekarang buat file baru namanya method.py
isikan dengan, 
```python
def hello():
    print("Hello world form method")
```

cara pemanggilannya yaitu dengan mengetik nama fungsinya se-garis lurus dengan statement def, ingat kembali bahwa python menggunakan identasi untuk membedakan nama fungsi dengan badan fungsi dan command pemanggilannya 
```python
def hello():
       print("Hello world from method")

# Pemanggilan fungsi

hello()
```

### module / package
didalam python juga mengenal istilah modul, atau package, ada yg bawaan ada juga yg kita define sendiri, untuk yg bawaan misalnya math, Collection, timeit, dsb sedangkan untuk yg define sendiri nanti saya jelaskan abis ini, caranya dengan 
```python
from somemodule import somefunction
```
method 1, pangkat dengan module bawaan python yang bernama math dan fungsi yg namanya pow atau power
di import dengan syntax berikut
buat file baru kasih nama fungsi2.py lalu paste code berikut. 
```python
from math import pow
def pangkat(x,y):
       return pow(x,y)

# pemanggilan method
print(pangkat(2,3))
```

```python
'''Menghasilkan hasil sisi miring dari rumus pythagoras dari 2 inputan sisi lainnya'''
def sisi_miring(sisi_tidur, sisi_tegak):
    simir= sqrt(pangkat(sisi_tidur,2) + pangkat(sisi_tegak,2))
    print(f"sisi tidur: {sisi_tidur}, sisi tegak: {sisi_tegak} dan sisi miring: {simir}")

#sisi_miring(3,4) -> sisi tidur: 3, sisi tegak: 4 dan sisi miring: 5.0

```

### Mutable & Imutable
> ### imutable
    * int, float, decimal, complex, bool, string, tuple, range, frozenset, bytes
> ### mutable
    * list, dict, set, bytearray, user-defined classes

### Mutable vs Immutable
> * Immutable tidak sama dengan konstanta
> * Immutable berarti nilai yang tersimpan tidak bisa dirubah
> * Sedangkan isi dari variabel bisa tetap berubah

### How to work
* Immutable
> Ketika kita melakukan manipulasi pada variable yang menyimpan nilai immutable maka,
> python akan membuatkan slot memory baru dan mereferensikannya terhadap alamat baru tersebut
> passing variable as referance

* Mutable
> Python akan langsung merubah nilai dari alamat memory variable mutable

```python
from ctypes import *

def bad_changer(nilai, best_mark):
    nilai = best_mark
    
def good_changer(nilai, best_mark):
    nilai[0] = best_mark


print("bad changer")
nilai_mhs1 = 80
print (f"alamat memory pada value sebelum dirubah {hex(id(nilai_mhs1))} dengan nilai {nilai_mhs1}")
bad_changer(nilai_mhs1, 90)
print (f"alamat memory pada value sesudah dirubah {hex(id(nilai_mhs1))} dengan nilai {nilai_mhs1}")


print("\ngood changer")
nilai_mhs2 = [80]
print (f"alamat memory pada list sebelum dirubah {hex(id(nilai_mhs2))} dengan nilai {nilai_mhs2}")
print (f"alamat memory pada value list sesudah {hex(id(nilai_mhs2[0]))} dengan nilai {nilai_mhs2[0]}")

good_changer(nilai_mhs2, 90)
print (f"alamat memory pada list sesudah dirubah {hex(id(nilai_mhs2))} dengan nilai {nilai_mhs2}")
print (f"alamat memory pada value list sesudah dirubah {hex(id(nilai_mhs2[0]))} dengan nilai {nilai_mhs2[0]}")
```

### performance concate string
```python
import timeit
def concateplus(times):
    teks = ''
    for time in range(times):
        teks += "Yunindyo Prabowo "
    return teks
def concatejoin(times):
    temp = []
    for time in range(times):
        temp.append("Yunindyo Prabowo ")
    return ''.join(temp)

print(concatejoin(10))
print(concateplus(10))

print(timeit.Timer("concateplus(100)", "from __main__ import concateplus").timeit())
print(timeit.Timer("concatejoin(100)", "from __main__ import concatejoin").timeit())
```
### list comprehension
#### cara lama
```python
new_list = []
for data in range(1, 11):
    #data*=2
    new_list.append(data)
    
print(new_list)
```

#### pythonic way list compre
```python
new_list1 = [data for data in range(1, 11)]
print (new_list1)

new_list2 = [data for data in range(1, 11) if data % 2 == 0]
print(new_list2)
```