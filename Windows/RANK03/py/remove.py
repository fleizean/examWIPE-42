from genericpath import exists
from importlib.resources import path
import os
from colorama import Fore, init

# a.out ve a.exe // dosya yolları
anext_line = "../get_next_line/"
aprintf = "../printf/"

# NEXTLINE #
get_next_line = "../get_next_line/get_next_line.c"
pshort_next_line = "get_next_line.c"
h_next_line = "../get_next_line/get_next_line.h"
pshorth_next_line = "get_next_line.h"

# PRINTF #
ft_printf = "../printf/ft_printf.c"
pshort_printf = "ft_printf.c"
#####################################################################################################################
## ../level01REMOVE
def exam03remove():
    ex03mevcut = 0
    ex03remove = 0
    # 1.
    if os.path.exists(get_next_line):
        ex03remove += 1
        os.remove(get_next_line)
    else:
        ex03mevcut += 1
        print(pshort_next_line + " Dosyası mevcut değil.")
    # 2.
    if os.path.exists(h_next_line):
        ex03remove += 1
        os.remove(h_next_line)
    else:
        ex03mevcut += 1
        print(pshorth_next_line + " Dosyası mevcut değil.")
    # 3.
    if os.path.exists(ft_printf):
        ex03remove += 1
        os.remove(ft_printf)
    else:
        ex03mevcut += 1
        print(pshort_printf + " Dosyası mevcut değil.")
    print("\n\n------------------------------------------")
    print("Mevcut Olmayan Dosya Sayısı : " + str(ex03mevcut))
    print("Silinen Dosya Sayısı : " + str(ex03remove))

#################################################################################
## ../level01CREATE
def exam03create():
    ex03mevcut = 0
    # 1.
    if os.path.exists(get_next_line):
        print(pshort_next_line + " Dosyası hali hazırda bulunuyor.")
    else:
        ex03mevcut += 1
        f = open(get_next_line, "w")
        open(get_next_line, "w")
    # 2.
    if os.path.exists(ft_printf):
        print(pshort_printf + " Dosyası hali hazırda bulunuyor.")
    else:
        ex03mevcut += 1
        f = open(ft_printf, "w")
        open(ft_printf, "w")
    # 3.
    if os.path.exists(h_next_line):
        print(pshorth_next_line + " Dosyası hali hazırda bulunuyor.")
    else:
        ex03mevcut += 1
        f = open(h_next_line, "w")
        open(h_next_line, "w")
    print("\n\n------------------------------------------")
    print("Mevcut Olan Dosya Sayısı : " + str(ex03mevcut))
    print("------------------------------------------")
####################################################################################
def aexeoutremove():
    aoutsayac = 0
    if os.path.exists(anext_line + "a.out"):
        os.remove(anext_line + "a.out")
        aoutsayac += 1
    if os.path.exists(aprintf + "a.out"):
        os.remove(aprintf + "a.out")
        aoutsayac += 1
    if os.path.exists(anext_line + "a.exe"):
        os.remove(anext_line + "a.exe")
        aoutsayac += 1
    if os.path.exists(aprintf + "a.exe"):
        os.remove(aprintf + "a.exe")
        aoutsayac += 1
    print("\n\n------------------------------------------")
    print("Silinen Dosya Sayısı : " + str(aoutsayac))
    print("------------------------------------------")
####################################################################################
welcome = Fore.CYAN + """
----------- examWIPE -----------"""
welcome += """""" + Fore.LIGHTRED_EX + """
1- Exam03 Dosya Silme
2- Exam03 Dosya Oluşturma
3- a.out Dosyalarını Sil
4- Exit
"""
welcome += """""" + Fore.CYAN + """--------------------------------"""
####################################################################################
dosyasilme = Fore.CYAN + """
----------- examWIPE -----------"""
dosyasilme += """""" + Fore.LIGHTRED_EX + """
1- get_next_line // printf sil
2- Exit
"""
dosyasilme += """""" + Fore.CYAN + """--------------------------------"""
#####################
dosyaolustur = Fore.CYAN + """
----------- examWIPE -----------"""
dosyaolustur += """""" + Fore.LIGHTRED_EX + """
1- get_next_line // printf oluştur
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
            exam03remove()
        elif secim2 == "2":
            exit()
        else:
            print("Yanlış Seçim Numarası!")
    elif secim == "2":
        print(dosyaolustur + Fore.WHITE)
        secim3 = input("Yeni Seçim Numaranızı Giriniz: ")
        if secim3 == "1":
            exam03create()
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
