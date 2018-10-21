from math import pow,sqrt
def pangkat(x,y):
       return pow(x,y)

def pangkat1 (x,y):
    #return print (f"pangkat {x} dari {y} adalah {pow(x,y)}")
    print (f" {x} pangkat {y} adalah {int(pow(x,y))}")

'''Menghasilkan hasil sisi miring dari rumus pythagoras dari 2 inputan sisi lainnya'''
def sisi_miring(sisi_tidur, sisi_tegak):
    simir= sqrt(pangkat(sisi_tidur,2) + pangkat(sisi_tegak,2))
    print(f"sisi tidur: {sisi_tidur}, sisi tegak: {sisi_tegak} dan sisi miring: {simir}")

# pemanggilan method
print(pangkat(2,3))

pangkat1(5,2)

sisi_miring(3,4)