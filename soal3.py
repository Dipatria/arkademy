import re

input1 = input("Masukkan kalimat:") 
input2 = input("Pencarian kata/frasa:")

if (len(input2) < len(input1)):
    jumlah = len(re.findall('(?={0})'.format(input2), input1))
    input1_reverse = input1[::-1]
    jumlah += len(re.findall('(?={0})'.format(input2), input1_reverse))
    print('ditemukan', jumlah, 'kali')
else:
    print("Kata/frasa yang dicari terlalu panjang")