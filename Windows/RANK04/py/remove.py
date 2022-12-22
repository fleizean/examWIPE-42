from genericpath import exists
from importlib.resources import path
import os
from colorama import Fore, init

# a.out ve a.exe // dosya yolları
amicroshell = "../microshell/"

# microshell #
microshell = "../microshell/microshell.c"
pshort_microshell = "../microshell.c"

#####################################################################################################################
## exam04REMOVE
def exam04remove():
    ex04mevcut = 0
    ex04remove = 0
    # 1.
    if os.path.exists(microshell):
        ex04remove += 1
        os.remove(microshell)
    else:
        ex04mevcut += 1
        print(pshort_microshell + " Dosyası mevcut değil.")
    print("\n\n------------------------------------------")
    print("Mevcut Olmayan Dosya Sayısı : " + str(ex04mevcut))
    print("Silinen Dosya Sayısı : " + str(ex04remove))

#################################################################################
## exam04CREATE
def exam04create():
    ex03mevcut = 0
    # 1.
    if os.path.exists(microshell):
        print(pshort_microshell + " Dosyası hali hazırda bulunuyor.")
    else:
        ex03mevcut += 1
        f = open(microshell, "w")
        open(microshell, "w")
    print("\n\n------------------------------------------")
    print("Mevcut Olan Dosya Sayısı : " + str(ex03mevcut))
    print("------------------------------------------")
####################################################################################
def aexeoutremove():
    aoutsayac = 0
    if os.path.exists(amicroshell + "a.out"):
        os.remove(amicroshell + "a.out")
        aoutsayac += 1
    print("\n\n------------------------------------------")
    print("Silinen Dosya Sayısı : " + str(aoutsayac))
    print("------------------------------------------")
####################################################################################
welcome = Fore.CYAN + """
----------- examWIPE -----------"""
welcome += """""" + Fore.LIGHTRED_EX + """
1- Exam04 Dosya Silme
2- Exam04 Dosya Oluşturma
3- a.out Dosyalarını Sil
4- Exit
"""
welcome += """""" + Fore.CYAN + """--------------------------------"""
####################################################################################
dosyasilme = Fore.CYAN + """
----------- examWIPE -----------"""
dosyasilme += """""" + Fore.LIGHTRED_EX + """
1- microshell'i sil
2- Exit
"""
dosyasilme += """""" + Fore.CYAN + """--------------------------------"""
#####################
dosyaolustur = Fore.CYAN + """
----------- examWIPE -----------"""
dosyaolustur += """""" + Fore.LIGHTRED_EX + """
1- microshell'i oluştur
2- Exit
"""
dosyaolustur += """""" + Fore.CYAN + """--------------------------------"""
#####################
while(1):
    print(welcome + Fore.WHITE)
    secim = input("Seçim Numaranızı Giriniz: ")
    if secim == "1":
        print(dosyasilme + Fore.WHITE)
        secim2 = input("Yeni Seçim Numaranızı Giriniz: ")
        if secim2 == "1":
            exam04remove()
        elif secim2 == "2":
            exit()
        else:
            print("Yanlış Seçim Numarası!")
    elif secim == "2":
        print(dosyaolustur + Fore.WHITE)
        secim3 = input("Yeni Seçim Numaranızı Giriniz: ")
        if secim3 == "1":
            exam04create()
        elif secim3 == "2":
            exit()
        else:
            print("Yanlış Seçim Numarası!")
    elif secim == "3":
        aexeoutremove()
    elif secim == "4":
        exit()
    else:
        print("Lütfen Doğru Seçim Yapınız!")
        exit()
