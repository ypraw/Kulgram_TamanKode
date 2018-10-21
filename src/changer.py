from ctypes import *


def bad_changer(nilai, best_mark):
    nilai = best_mark


def good_changer(nilai, best_mark):
    nilai[0] = best_mark


print("bad changer")
nilai_mhs1 = 80
print(f"alamat memory pada value sebelum dirubah {hex(id(nilai_mhs1))} dengan nilai {nilai_mhs1}")
bad_changer(nilai_mhs1, 90)
print(f"alamat memory pada value sesudah dirubah {hex(id(nilai_mhs1))} dengan nilai {nilai_mhs1}")

print("\ngood changer")
nilai_mhs2 = [80]
print(f"alamat memory pada list sebelum dirubah {hex(id(nilai_mhs2))} dengan nilai {nilai_mhs2}")
print(f"alamat memory pada value list sesudah {hex(id(nilai_mhs2[0]))} dengan nilai {nilai_mhs2[0]}")

good_changer(nilai_mhs2, 90)
print(f"alamat memory pada list sesudah dirubah {hex(id(nilai_mhs2))} dengan nilai {nilai_mhs2}")
print(f"alamat memory pada value list sesudah dirubah {hex(id(nilai_mhs2[0]))} dengan nilai {nilai_mhs2[0]}")
print(nilai_mhs2[0])