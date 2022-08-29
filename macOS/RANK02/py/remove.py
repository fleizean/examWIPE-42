from genericpath import exists
from importlib.resources import path
import os
from colorama import Fore, init

# a.out ve a.exe
# LEVEL 01 #
afirst_word = "level01/first_word/"
aputstr = "level01/ft_putstr/"
astrcpy = "level01/ft_strcpy/"
aswap = "level01/ft_swap/"
arepeat_alpha = "level01/repeat_alpha/"
arevprint = "level01/rev_print/"
arot_13 = "level01/rot_13/"
arotone = "level01/rotone/"
asaerch_and_replace = "level01/search_and_replace/"
aulstr = "level01/ulstr/"
# LEVEL 02 #
aalpha_mirror = "level02/alpha_mirror/"
ado_op = "level02/do_op/"
a_atoi = "level02/ft_atoi/"
astrcmp = "level02/ft_strcmp/"
astrdup = "level02/ft_strdup/"
astrrev = "level02/ft_strrev/"
ainter = "level02/inter/"
ais_power_of_2 = "level02/is_power_of_2/"
alast_word = "level02/last_word/"
amax = "level02/max/"
aprint_bits = "level02/print_bits/"
aswap_bits = "level02/swap_bits/"
areverse_bits = "level02/reverse_bits/"
aunion = "level02/union/"
awdmatch = "level02/wdmatch/"
# LEVEL 03 #
aadd_prime_sum = "level03/add_prime_sum/"
aepur_str = "level03/epur_str/"
aexpand_str = "level03/expand_str/"
aatoi_base = "level03/ft_atoi_base/"
alist_size = "level03/ft_list_size/"
arange = "level03/ft_range/"
arrange = "level03/ft_rrange/"
ahidenp = "level03/hidenp/"
aparamsum = "level03/paramsum/"
apgcd = "level03/pgcd/"
aprint_hex = "level03/print_hex/"
arstr_capitalizer = "level03/rstr_capitalizer/"
astr_capitalizer = "level03/str_capitalizer/"
atab_mult = "level03/tab_mult/"
# LEVEL 04 #
afprime = "level04/fprime/"
aitoa = "level04/ft_itoa/"
alist_foreach = "level04/ft_list_foreach/"
alist_remove_if = "level04/ft_list_remove_if/"
asplit = "level04/ft_split/"
arev_wstr = "level04/rev_wstr/"
arostring = "level04/rostring/"
asort_int_tab = "level04/sort_int_tab/"
asort_list = "level04/sort_list/"
###################################################################################################################
# LEVEL 01 #
first_word = "level01/first_word/first_word.c"
pshort_first_word = "first_word.c"
pft_first_word = "level01/first_word/first_word.c"
ft_putstr = "level01/ft_putstr/ft_putstr.c"
pshort_putstr = "ft_putstr.c"
pft_putstr = "level01/ft_putstr/ft_putstr.c"
ft_strcpy = "level01/ft_strcpy/ft_strcpy.c"
pshort_strcpy = "ft_strcpy.c"
pft_strcpy = "level01/ft_strcpy/ft_strcpy.c"
ft_swap = "level01/ft_swap/ft_swap.c"
pshort_swap = "ft_swap.c"
pft_swap = "level01/ft_swap/ft_swap.c"
repeat_alpha = "level01/repeat_alpha/repeat_alpha.c"
pshort_repeat_alpha = "repeat_alpha.c"
pft_repeat_alpha = "level01/repeat_alpha/repeat_alpha.c"
rev_print = "level01/rev_print/rev_print.c"
pshort_rev_print = "rev_print.c"
pft_rev_print = "level01/rev_print/rev_print.c"
rot_13 = "level01/rot_13/rot_13.c"
pshort_rot_13 = "rot_13.c"
pft_rot_13 = "level01/rot_13/rot_13.c"
rotone = "level01/rotone/rotone.c"
pshort_rotone = "rotone.c"
pft_rotone = "level01/rotone/rotone.c"
search_and_replace = "level01/search_and_replace/search_and_replace.c"
pshort_search_and_replace = "saerch_and_replace.c"
pft_search_and_replace = "level01/search_and_replace/search_and_replace.c"
ulstr = "level01/ulstr/ulstr.c"
pshort_ulstr = "ulstr.c"
pft_ulstr = "level01/ulstr/ulstr.c"
#####################################################################################################################

# LEVEL 02 #
alpha_mirror = "level02/alpha_mirror/alpha_mirror.c" 
pshort_alpha_mirror = "alpha_mirror.c"
pft_alpha_mirror = "level02/alpha_mirror/alpha_mirror.c"
do_op = "level02/do_op/do_op.c"
pshort_do_op = "do_op.c"
pft_do_op = "level02/do_op/do_op.c"
ft_atoi = "level02/ft_atoi/ft_atoi.c"
pshort_atoi = "ft_atoi.c"
pft_atoi = "level02/ft_atoi/ft_atoi.c"
ft_strcmp = "level02/ft_strcmp/ft_strcmp.c"
pshort_strcmp = "ft_strcmp.c"
pft_strcmp = "level02/ft_strcmp/ft_strcmp.c"
ft_strdup = "level02/ft_strdup/ft_strdup.c"
pshort_strdup = "ft_strdup.c"
pft_strdup = "level02/ft_strdup/ft_strdup.c"
ft_strrev = "level02/ft_strrev/ft_strrev.c"
pshort_strrev = "ft_strrev.c"
pft_strrev = "level02/ft_strrev/ft_strrev.c"
inter = "level02/inter/inter.c"
pshort_inter = "ft_inter.c"
pft_inter = "level02/inter/inter.c"
is_power_of_2 = "level02/is_power_of_2/is_power_of_2.c"
pshort_is_power_of_2 = "is_power_of_2.c"
pft_is_power_of_2 = "level02/is_power_of_2/is_power_of_2.c"
last_word = "level02/last_word/last_word.c"
pshort_last_word = "last_word.c"
pft_last_word = "level02/last_word/last_word.c"
max = "level02/max/max.c"
pshort_max = "max.c"
pft_max = "level02/max/max.c"
print_bits = "level02/print_bits/print_bits.c"
pshort_print_bits = "print_bits.c"
pft_print_bits = "level02/print_bits/print_bits.c"
reverse_bits = "level02/reverse_bits/reverse_bits.c"
pshort_reverse_bits = "reverse_bits.c"
pft_reverse_bits = "level02/reverse_bits/reverse_bits.c"
swap_bits = "level02/swap_bits/swap_bits.c"
pshort_swap_bits = "swap_bits.c"
pft_swap_bits = "level02/swap_bits/swap_bits.c"
union = "level02/union/union.c"
pshort_union = "union.c"
pft_union = "level02/union/union.c"
wdmatch = "level02/wdmatch/wdmatch.c"
pshort_wdmatch = "wdmatch.c"
pft_wdmatch = "level02/wdmatch/wdmatch.c"
#####################################################################################################################

# LEVEL 03 #
add_prime_sum = "level03/add_prime_sum/add_prime_sum.c"
pshort_add_prime_sum = "add_prime_sum.c"
pft_add_prime_sum = "level03/add_prime_sum/add_prime_sum.c"
epur_str = "level03/epur_str/epur_str.c"
pshort_epur_str = "epur_str.c"
pft_epur_str = "level03/epur_str/epur_str.c"
expand_str = "level03/expand_str/expand_str.c"
pshort_expand_str = "expand_str.c"
pft_expand_str = "level03/expand_str/expand_str.c"
ft_atoi_base = "level03/ft_atoi_base/ft_atoi_base.c"
pshort_atoi_base = "ft_atoi_base.c"
pft_atoi_base = "level03/ft_atoi_base/ft_atoi_base.c"
ft_list_size = "level03/ft_list_size/ft_list_size.c"
pshort_list_size = "ft_list_size.c"
pft_list_size = "level03/ft_list_size/ft_list_size.c"
ft_range = "level03/ft_range/ft_range.c"
pshort_range = "ft_range.c"
pft_range = "level03/ft_range/ft_range.c"
ft_rrange = "level03/ft_rrange/ft_rrange.c"
pshort_rrange = "ft_rrange.c"
pft_rrange = "level03/ft_rrange/ft_rrange.c"
hidenp = "level03/hidenp/hidenp.c"
pshort_hidenp = "hidenp.c"
pft_hidenp = "level03/hidenp/hidenp.c"
paramsum = "level03/paramsum/paramsum.c"
pshort_paramsum = "paramsum.c"
pft_paramsum = "level03/paramsum/paramsum.c"
pgcd = "level03/pgcd/pgcd.c"
pshort_pgcd = "pgcd.c"
pft_pgcd = "level03/pgcd/pgcd.c"
print_hex = "level03/print_hex/print_hex.c"
pshort_print_hex = "print_hex.c"
pft_print_hex = "level03/print_hex/print_hex.c"
rstr_capitalizer = "level03/rstr_capitalizer/rstr_capitalizer.c"
pshort_rstr_capitalizer = "rstr_capitalizer.c"
pft_rstr_capitalizer  = "level03/rstr_capitalizer/rstr_capitalizer.c"
str_capitalizer = "level03/str_capitalizer/str_capitalizer.c"
pshort_str_capitalizer = "str_capitalizer.c"
pft_str_capitalizer  = "level03/str_capitalizer/str_capitalizer.c"
tab_mult = "level03/tab_mult/tab_mult.c"
pshort_tab_mult = "tab_mult.c"
pft_tab_mult = "level03/tab_mult/tab_mult.c"
#####################################################################################################################

# LEVEL 04 #
fprime = "level04/fprime/fprime.c" 
pshort_fprime = "fprime.c"
pft_fprime = "level04/fprime/fprime.c"
ft_itoa = "level04/ft_itoa/ft_itoa.c"
pshort_itoa = "ft_itoa.c"
pft_itoa = "level04/ft_itoa/ft_itoa.c"
ft_list_foreach = "level04/ft_list_foreach/ft_list_foreach.c"
pshort_list_foreach = "ft_list_foreach.c"
pft_list_foreach = "level04/ft_list_foreach/ft_list_foreach.c"
ft_list_remove_if = "level04/ft_list_remove_if/ft_list_remove_if.c"
pshort_list_remove_if = "ft_list_remove_if.c"
pft_list_remove_if = "level04/ft_list_remove_if/ft_list_remove_if.c"
ft_split = "level04/ft_split/ft_split.c"
pshort_split = "ft_split.c"
pft_split = "level04/ft_split/ft_split.c"
rev_wstr = "level04/rev_wstr/rev_wstr.c"
pshort_rev_wstr = "rev_wstr.c"
pft_rev_wstr = "level04/rev_wstr/rev_wstr.c"
rostring = "level04/rostring/rostring.c"
pshort_rostring = "rostring.c"
pft_rostring = "level04/rostring/rostring.c"
sort_int_tab = "level04/sort_int_tab/sort_int_tab.c"
pshort_sort_int_tab = "sort_int_tab.c"
pft_sort_int_tab = "level04/sort_int_tab/sort_int_tab.c"
sort_list = "level04/sort_list/sort_list.c"
pshort_sort_list = "sort_list.c"
pft_sort_list = "level04/sort_list/sort_list.c"
#####################################################################################################################

# H FILES #

# level03
hlist_size = "level03/ft_list_size/ft_list.h"
hshort_list_size = "ft_list.h"
hft_list_size = "level03/ft_list_size/ft_list.h"
#####

# level04
hlist_foreach = "level04/ft_list_foreach/ft_list.h"
hshort_list_foreach = "ft_list.h"
hft_list_foreach = "level04/ft_list_foreach/ft_list.h"

hlist_remove_if = "level04/ft_list_remove_if/ft_list.h"
hshort_list_remove_if = "ft_list.h"
hft_list_remove_if = "level04/ft_list_remove_if/ft_list.h"

hlist_sort = "level04/sort_list/list.h"
hshort_sort_list = "list.h"
hft_sort_list = "level04/sort_list/list.h"
#####

#####################################################################################################################
## level01REMOVE
def level01remove():
    mevcutolmayan = 0
    silinendosya = 0
    # 1.
    if os.path.exists(pft_first_word):
        silinendosya += 1
        os.remove(pft_first_word)
    else:
        mevcutolmayan += 1
        print(pshort_first_word + " Dosyası mevcut değil.")
    # 2.
    if os.path.exists(pft_putstr):
        silinendosya += 1
        os.remove(pft_putstr)
    else:
        mevcutolmayan += 1
        print(pshort_putstr + " Dosyası mevcut değil.")
    # 3.
    if os.path.exists(pft_strcpy):
        silinendosya += 1
        os.remove(pft_strcpy)
    else:
        mevcutolmayan += 1
        print(pshort_strcpy + " Dosyası mevcut değil.")
    # 4.
    if os.path.exists(pft_swap):
        silinendosya += 1
        os.remove(pft_swap)
    else:
        mevcutolmayan += 1
        print(pshort_swap + " Dosyası mevcut değil.")
    # 5.
    if os.path.exists(pft_repeat_alpha):
        silinendosya += 1
        os.remove(pft_repeat_alpha)
    else:
        mevcutolmayan += 1
        print(pshort_repeat_alpha + " Dosyası mevcut değil.")
    # 6.
    if os.path.exists(pft_rev_print):
        silinendosya += 1
        os.remove(pft_rev_print)
    else:
        mevcutolmayan += 1
        print(pshort_rev_print + " Dosyası mevcut değil.")
    # 7.
    if os.path.exists(pft_rot_13):
        silinendosya += 1
        os.remove(pft_rot_13)
    else:
        mevcutolmayan += 1
        print(pshort_rot_13 + " Dosyası mevcut değil.")
    # 8.
    if os.path.exists(pft_rotone):
        silinendosya += 1
        os.remove(pft_rotone)
    else:
        mevcutolmayan += 1
        print(pshort_rotone + " Dosyası mevcut değil.")
    # 9.
    if os.path.exists(pft_search_and_replace):
        silinendosya += 1
        os.remove(pft_search_and_replace)
    else:
        mevcutolmayan += 1
        print(pshort_search_and_replace + " Dosyası mevcut değil.")
    # 10.
    if os.path.exists(pft_ulstr):
        silinendosya += 1
        os.remove(pft_ulstr)
    else:
        mevcutolmayan += 1
        print(pshort_ulstr + " Dosyası mevcut değil.")
    print("\n\nMevcut Olmayan Dosya Sayısı : " + str(mevcutolmayan))
    print("Silinen Dosya Sayısı : " + str(silinendosya))
#################################################################################
## LEVEL02REMOVE
def level02remove():
    mevcutolmayan = 0
    silinendosya = 0
    # 1.
    if os.path.exists(pft_alpha_mirror):
        silinendosya += 1
        os.remove(pft_alpha_mirror)
    else:
        mevcutolmayan += 1
        print(pshort_alpha_mirror + " Dosyası mevcut değil.")
    # 2.
    if os.path.exists(pft_do_op):
        silinendosya += 1
        os.remove(pft_do_op)
    else:
        mevcutolmayan += 1
        print(pshort_do_op + " Dosyası mevcut değil.")
    # 3.
    if os.path.exists(pft_atoi):
        silinendosya += 1
        os.remove(pft_atoi)
    else:
        mevcutolmayan += 1
        print(pshort_atoi + " Dosyası mevcut değil.")
    # 4.
    if os.path.exists(pft_strcmp):
        silinendosya += 1
        os.remove(pft_strcmp)
    else:
        mevcutolmayan += 1
        print(pshort_strcmp + " Dosyası mevcut değil.")
    # 5.
    if os.path.exists(pft_strdup):
        silinendosya += 1
        os.remove(pft_strdup)
    else:
        mevcutolmayan += 1
        print(pshort_strdup + " Dosyası mevcut değil.")
    # 6.
    if os.path.exists(pft_strrev):
        silinendosya += 1
        os.remove(pft_strrev)
    else:
        mevcutolmayan += 1
        print(pshort_strrev + " Dosyası mevcut değil.")
    # 7.
    if os.path.exists(pft_inter):
        silinendosya += 1
        os.remove(pft_inter)
    else:
        mevcutolmayan += 1
        print(pshort_inter + " Dosyası mevcut değil.")
    # 8.
    if os.path.exists(pft_is_power_of_2):
        silinendosya += 1
        os.remove(pft_is_power_of_2)
    else:
        mevcutolmayan += 1
        print(pshort_is_power_of_2 + " Dosyası mevcut değil.")
    # 9.
    if os.path.exists(pft_last_word):
        silinendosya += 1
        os.remove(pft_last_word)
    else:
        mevcutolmayan += 1
        print(pshort_last_word + " Dosyası mevcut değil.")
    # 10.
    if os.path.exists(pft_max):
        silinendosya += 1
        os.remove(pft_max)
    else:
        mevcutolmayan += 1
        print(pshort_max + " Dosyası mevcut değil.")
    # 11.
    if os.path.exists(pft_print_bits):
        silinendosya += 1
        os.remove(pft_print_bits)
    else:
        mevcutolmayan += 1
        print(pshort_print_bits + " Dosyası mevcut değil.")
    # 12.
    if os.path.exists(pft_swap_bits):
        silinendosya += 1
        os.remove(pft_swap_bits)
    else:
        mevcutolmayan += 1
        print(pshort_swap_bits + " Dosyası mevcut değil.")
    # 13.
    if os.path.exists(pft_reverse_bits):
        silinendosya += 1
        os.remove(pft_reverse_bits)
    else:
        mevcutolmayan += 1
        print(pshort_reverse_bits + " Dosyası mevcut değil.")
    # 14.
    if os.path.exists(pft_union):
        silinendosya += 1
        os.remove(pft_union)
    else:
        mevcutolmayan += 1
        print(pshort_union + " Dosyası mevcut değil.")
    # 15.
    if os.path.exists(pft_wdmatch):
        silinendosya += 1
        os.remove(pft_wdmatch)
    else:
        mevcutolmayan += 1
        print(pshort_wdmatch + " Dosyası mevcut değil.")
    print("\n\nMevcut Olmayan Dosya Sayısı : " + str(mevcutolmayan))
    print("Silinen Dosya Sayısı : " + str(silinendosya))
#################################################################################
## level03REMOVE
def level03remove():
    mevcutolmayan = 0
    silinendosya = 0
    # 1.
    if os.path.exists(pft_add_prime_sum):
        silinendosya += 1
        os.remove(pft_add_prime_sum)
    else:
        mevcutolmayan += 1
        print(pshort_add_prime_sum + " Dosyası mevcut değil.")
    # 2.
    if os.path.exists(pft_epur_str):
        silinendosya += 1
        os.remove(pft_epur_str)
    else:
        mevcutolmayan += 1
        print(pshort_epur_str + " Dosyası mevcut değil.")
    # 3.
    if os.path.exists(pft_expand_str):
        silinendosya += 1
        os.remove(pft_expand_str)
    else:
        mevcutolmayan += 1
        print(pshort_expand_str + " Dosyası mevcut değil.")
    # 4.
    if os.path.exists(pft_atoi_base):
        silinendosya += 1
        os.remove(pft_atoi_base)
    else:
        mevcutolmayan += 1
        print(pshort_atoi_base + " Dosyası mevcut değil.")
    # 5.
    if os.path.exists(pft_list_size):
        silinendosya += 1
        os.remove(pft_list_size)
    else:
        mevcutolmayan += 1
        print(pshort_list_size + " Dosyası mevcut değil.")
    # 5. H FILE
    if os.path.exists(hft_list_size):
        silinendosya += 1
        os.remove(hft_list_size)
    else:
        mevcutolmayan += 1
        print(hshort_list_size + " Dosyası mevcut değil.")
    # 6.
    if os.path.exists(pft_range):
        silinendosya += 1
        os.remove(pft_range)
    else:
        mevcutolmayan += 1
        print(pshort_range + " Dosyası mevcut değil.")
    # 7.
    if os.path.exists(pft_rrange):
        silinendosya += 1
        os.remove(pft_rrange)
    else:
        mevcutolmayan += 1
        print(pshort_rrange + " Dosyası mevcut değil.")
    # 8.
    if os.path.exists(pft_hidenp):
        silinendosya += 1
        os.remove(pft_hidenp)
    else:
        mevcutolmayan += 1
        print(pshort_hidenp + " Dosyası mevcut değil.")
    # 9.
    if os.path.exists(pft_paramsum):
        silinendosya += 1
        os.remove(pft_paramsum)
    else:
        mevcutolmayan += 1
        print(pshort_paramsum + " Dosyası mevcut değil.")
    # 10.
    if os.path.exists(pft_pgcd):
        silinendosya += 1
        os.remove(pft_pgcd)
    else:
        mevcutolmayan += 1
        print(pshort_pgcd + " Dosyası mevcut değil.")
    # 11.
    if os.path.exists(pft_print_hex):
        silinendosya += 1
        os.remove(pft_print_hex)
    else:
        mevcutolmayan += 1
        print(pshort_print_hex + " Dosyası mevcut değil.")
    # 12.
    if os.path.exists(pft_rstr_capitalizer):
        silinendosya += 1
        os.remove(pft_rstr_capitalizer)
    else:
        mevcutolmayan += 1
        print(pshort_rstr_capitalizer + " Dosyası mevcut değil.")
    # 13.
    if os.path.exists(pft_str_capitalizer):
        silinendosya += 1
        os.remove(pft_str_capitalizer)
    else:
        mevcutolmayan += 1
        print(pshort_str_capitalizer + " Dosyası mevcut değil.")
    # 14.
    if os.path.exists(pft_tab_mult):
        silinendosya += 1
        os.remove(pft_tab_mult)
    else:
        mevcutolmayan += 1
        print(pshort_tab_mult + " Dosyası mevcut değil.")
    print("\n\nMevcut Olmayan Dosya Sayısı : " + str(mevcutolmayan))
    print("Silinen Dosya Sayısı : " + str(silinendosya))
#################################################################################
## level04REMOVE
def level04remove():
    mevcutolmayan = 0
    silinendosya = 0
    # 1.
    if os.path.exists(pft_fprime):
        silinendosya += 1
        os.remove(pft_fprime)
    else:
        mevcutolmayan += 1
        print(pshort_fprime + " Dosyası mevcut değil.")
    # 2.
    if os.path.exists(pft_itoa):
        silinendosya += 1
        os.remove(pft_itoa)
    else:
        mevcutolmayan += 1
        print(pshort_itoa + " Dosyası mevcut değil.")
    # 3.
    if os.path.exists(pft_list_foreach):
        silinendosya += 1
        os.remove(pft_list_foreach)
    else:
        mevcutolmayan += 1
        print(pshort_list_foreach + " Dosyası mevcut değil.")
    # 3. H FILE
    if os.path.exists(hft_list_foreach):
        silinendosya += 1
        os.remove(hft_list_foreach)
    else:
        mevcutolmayan += 1
        print(hshort_list_foreach + " Dosyası mevcut değil.")
    # 4.
    if os.path.exists(pft_list_remove_if):
        silinendosya += 1
        os.remove(pft_list_remove_if)
    else:
        mevcutolmayan += 1
        print(pshort_list_remove_if + " Dosyası mevcut değil.")
    # 4. H FILE
    if os.path.exists(hft_list_remove_if):
        silinendosya += 1
        os.remove(hft_list_remove_if)
    else:
        mevcutolmayan += 1
        print(hshort_list_remove_if + " Dosyası mevcut değil.")
    # 5.
    if os.path.exists(pft_split):
        silinendosya += 1
        os.remove(pft_split)
    else:
        mevcutolmayan += 1
        print(pshort_split + " Dosyası mevcut değil.")
    # 6.
    if os.path.exists(pft_rev_wstr):
        silinendosya += 1
        os.remove(pft_rev_wstr)
    else:
        mevcutolmayan += 1
        print(pshort_rev_wstr + " Dosyası mevcut değil.")
    # 7.
    if os.path.exists(pft_rostring):
        silinendosya += 1
        os.remove(pft_rostring)
    else:
        mevcutolmayan += 1
        print(pshort_rostring + " Dosyası mevcut değil.")
    # 8.
    if os.path.exists(pft_sort_int_tab):
        silinendosya += 1
        os.remove(pft_sort_int_tab)
    else:
        mevcutolmayan += 1
        print(pshort_sort_int_tab + " Dosyası mevcut değil.")
    # 9.
    if os.path.exists(pft_sort_list):
        silinendosya += 1
        os.remove(pft_sort_list)
    else:
        mevcutolmayan += 1
        print(pshort_sort_list + " Dosyası mevcut değil.")
    # 9. H FILE
    if os.path.exists(hft_sort_list):
        silinendosya += 1
        os.remove(hft_sort_list)
    else:
        mevcutolmayan += 1
        print(hshort_sort_list + " Dosyası mevcut değil.")
    print("\n\nMevcut Olmayan Dosya Sayısı : " + str(mevcutolmayan))
    print("Silinen Dosya Sayısı : " + str(silinendosya))
#################################################################################
## level01CREATE
def level01create():
    mevcutolmayan = 0
    # 1.
    if os.path.exists(pft_first_word):
        print(pshort_first_word + " Dosyası hali hazırda bulunuyor.")
    else:
        mevcutolmayan += 1
        f = open(pft_first_word, "w")
        open(first_word, "w")
    # 2.
    if os.path.exists(pft_putstr):
        print(pshort_putstr + " Dosyası hali hazırda bulunuyor.")
    else:
        mevcutolmayan += 1
        f = open(pft_putstr, "w")
        open(ft_putstr, "w")
    # 3.
    if os.path.exists(pft_strcpy):
        print(pshort_strcpy + " Dosyası hali hazırda bulunuyor.")
    else:
        mevcutolmayan += 1
        f = open(pft_putstr, "w")
        open(ft_strcpy, "w")
    # 4.
    if os.path.exists(pft_swap):
        print(pshort_swap + " Dosyası hali hazırda bulunuyor.")
    else:
        mevcutolmayan += 1
        f = open(pft_swap, "w")
        open(ft_swap, "w")
    # 5.
    if os.path.exists(pft_repeat_alpha):
        print(pshort_repeat_alpha + " Dosyası hali hazırda bulunuyor.")
    else:
        mevcutolmayan += 1
        f = open(pft_repeat_alpha, "w")
        open(repeat_alpha, "w")
    # 6.
    if os.path.exists(pft_rev_print):
        print(pshort_rev_print + " Dosyası hali hazırda bulunuyor.")
    else:
        mevcutolmayan += 1
        f = open(pft_rev_print, "w")
        open(rev_print, "w")
    # 7.
    if os.path.exists(pft_rot_13):
        print(pshort_rot_13 + " Dosyası hali hazırda bulunuyor.")
    else:
        mevcutolmayan += 1
        f = open(pft_rot_13, "w")
        open(rot_13, "w")
    # 8.
    if os.path.exists(pft_rotone):
        print(pshort_rotone + " Dosyası hali hazırda bulunuyor.")
    else:
        mevcutolmayan += 1
        f = open(pft_rotone, "w")
        open(rotone, "w")
    # 9.
    if os.path.exists(pft_search_and_replace):
        print(pshort_search_and_replace + " Dosyası hali hazırda bulunuyor.")
    else:
        mevcutolmayan += 1
        f = open(pft_search_and_replace, "w")
        open(search_and_replace, "w")
    # 10.
    if os.path.exists(pft_ulstr):  
        print(pshort_ulstr + " Dosyası hali hazırda bulunuyor.")
    else:
        mevcutolmayan += 1
        f = open(pft_ulstr, "w")
        open(ulstr, "w")
    print("\n\nMevcut Olan Dosya Sayısı : " + str(mevcutolmayan))
####################################################################################
## LEVEL02CREATE
def level02create():
    mevcutolmayan = 0
    # 1.
    if os.path.exists(pft_alpha_mirror):
        print(pshort_alpha_mirror + " Dosyası hali hazırda bulunuyor.")
    else:
        mevcutolmayan += 1
        f = open(pft_alpha_mirror, "w")
        open(alpha_mirror, "w")
    # 2.
    if os.path.exists(pft_do_op):
        print(pshort_do_op + " Dosyası hali hazırda bulunuyor.")
    else:
        mevcutolmayan += 1
        f = open(pft_do_op, "w")
        open(do_op, "w")
    # 3.
    if os.path.exists(pft_atoi):
        print(pshort_atoi + " Dosyası hali hazırda bulunuyor.")
    else:
        mevcutolmayan += 1
        f = open(pft_atoi, "w")
        open(ft_atoi, "w")
    # 4.
    if os.path.exists(pft_strcmp):
        print(pshort_strcmp + " Dosyası hali hazırda bulunuyor.")
    else:
        mevcutolmayan += 1
        f = open(pft_strcmp, "w")
        open(ft_strcmp, "w")
    # 5.
    if os.path.exists(pft_strdup):
        print(pshort_strdup + " Dosyası hali hazırda bulunuyor.")
    else:
        mevcutolmayan += 1
        f = open(pft_strdup, "w")
        open(ft_strdup, "w")
    # 6.
    if os.path.exists(pft_strrev):
        print(pshort_strrev + " Dosyası hali hazırda bulunuyor.")
    else:
        mevcutolmayan += 1
        f = open(pft_strrev, "w")
        open(ft_strrev, "w")
    # 7.
    if os.path.exists(pft_inter):
        print(pshort_inter + " Dosyası hali hazırda bulunuyor.")
    else:
        mevcutolmayan += 1
        f = open(pft_inter, "w")
        open(inter, "w")
    # 8.
    if os.path.exists(pft_is_power_of_2):
        print(pshort_is_power_of_2 + " Dosyası hali hazırda bulunuyor.")
    else:
        mevcutolmayan += 1
        f = open(pft_is_power_of_2, "w")
        open(is_power_of_2, "w")
    # 9.
    if os.path.exists(pft_last_word):
        print(pshort_last_word + " Dosyası hali hazırda bulunuyor.")
    else:
        mevcutolmayan += 1
        f = open(pft_last_word, "w")
        open(last_word, "w")
    # 10.
    if os.path.exists(pft_max):  
        print(pshort_max + " Dosyası hali hazırda bulunuyor.")
    else:
        mevcutolmayan += 1
        f = open(pft_max, "w")
        open(max, "w")
    # 11.
    if os.path.exists(pft_print_bits):  
        print(pshort_print_bits + " Dosyası hali hazırda bulunuyor.")
    else:
        mevcutolmayan += 1
        f = open(pft_print_bits, "w")
        open(print_bits, "w")
    # 12.
    if os.path.exists(pft_reverse_bits):  
        print(pshort_reverse_bits + " Dosyası hali hazırda bulunuyor.")
    else:
        mevcutolmayan += 1
        f = open(pft_reverse_bits, "w")
        open(reverse_bits, "w")
    # 13.
    if os.path.exists(pft_swap_bits):  
        print(pshort_swap_bits + " Dosyası hali hazırda bulunuyor.")
    else:
        mevcutolmayan += 1
        f = open(pft_swap_bits, "w")
        open(swap_bits, "w")
    # 14.
    if os.path.exists(pft_union):  
        print(pshort_union + " Dosyası hali hazırda bulunuyor.")
    else:
        mevcutolmayan += 1
        f = open(pft_union, "w")
        open(union, "w")
    # 15.
    if os.path.exists(pft_wdmatch):  
        print(pshort_wdmatch + " Dosyası hali hazırda bulunuyor.")
    else:
        mevcutolmayan += 1
        f = open(pft_wdmatch, "w")
        open(wdmatch, "w")
    print("\n\nMevcut Olan Dosya Sayısı : " + str(mevcutolmayan))
####################################################################################
## level03CREATE
def level03create():
    mevcutolmayan = 0
    # 1.
    if os.path.exists(pft_add_prime_sum):
        print(pshort_add_prime_sum + " Dosyası hali hazırda bulunuyor.")
    else:
        mevcutolmayan += 1
        f = open(pft_add_prime_sum, "w")
        open(add_prime_sum, "w")
    # 2.
    if os.path.exists(pft_epur_str):
        print(pshort_epur_str + " Dosyası hali hazırda bulunuyor.")
    else:
        mevcutolmayan += 1
        f = open(pft_epur_str, "w")
        open(epur_str, "w")
    # 3.
    if os.path.exists(pft_expand_str):
        print(pshort_expand_str + " Dosyası hali hazırda bulunuyor.")
    else:
        mevcutolmayan += 1
        f = open(pft_expand_str, "w")
        open(expand_str, "w")
    # 4.
    if os.path.exists(pft_atoi_base):
        print(pshort_atoi_base + " Dosyası hali hazırda bulunuyor.")
    else:
        mevcutolmayan += 1
        f = open(pft_atoi_base, "w")
        open(ft_atoi_base, "w")
    # 5.
    if os.path.exists(pft_list_size):
        print(pshort_list_size + " Dosyası hali hazırda bulunuyor.")
    else:
        mevcutolmayan += 1
        f = open(pft_list_size, "w")
        open(ft_list_size, "w")
    # 5. H FILE
    if os.path.exists(hft_list_size):
        print(hshort_list_size + " Dosyası hali hazırda bulunuyor.")
    else:
        mevcutolmayan += 1
        f = open(hft_list_size, "w")
        open(hlist_size, "w")
    # 6.
    if os.path.exists(pft_range):
        print(pshort_range + " Dosyası hali hazırda bulunuyor.")
    else:
        mevcutolmayan += 1
        f = open(pft_range, "w")
        open(ft_range, "w")
    # 7.
    if os.path.exists(pft_rrange):
        print(pshort_rrange + " Dosyası hali hazırda bulunuyor.")
    else:
        mevcutolmayan += 1
        f = open(pft_rrange, "w")
        open(ft_rrange, "w")
    # 8.
    if os.path.exists(pft_hidenp):
        print(pshort_hidenp + " Dosyası hali hazırda bulunuyor.")
    else:
        mevcutolmayan += 1
        f = open(pft_hidenp, "w")
        open(hidenp, "w")
    # 9.
    if os.path.exists(pft_paramsum):
        print(pshort_paramsum + " Dosyası hali hazırda bulunuyor.")
    else:
        mevcutolmayan += 1
        f = open(pft_paramsum, "w")
        open(paramsum, "w")
    # 10.
    if os.path.exists(pft_pgcd):  
        print(pshort_pgcd + " Dosyası hali hazırda bulunuyor.")
    else:
        mevcutolmayan += 1
        f = open(pft_pgcd, "w")
        open(pgcd, "w")
    # 11.
    if os.path.exists(pft_print_hex):  
        print(pshort_print_hex + " Dosyası hali hazırda bulunuyor.")
    else:
        mevcutolmayan += 1
        f = open(pft_print_hex, "w")
        open(print_hex, "w")
    # 12.
    if os.path.exists(pft_rstr_capitalizer):  
        print(pshort_rstr_capitalizer + " Dosyası hali hazırda bulunuyor.")
    else:
        mevcutolmayan += 1
        f = open(pft_rstr_capitalizer, "w")
        open(rstr_capitalizer, "w")
    # 13.
    if os.path.exists(pft_str_capitalizer):  
        print(pshort_str_capitalizer + " Dosyası hali hazırda bulunuyor.")
    else:
        mevcutolmayan += 1
        f = open(pft_str_capitalizer, "w")
        open(str_capitalizer, "w")
    # 14.
    if os.path.exists(pft_tab_mult):  
        print(pshort_tab_mult + " Dosyası hali hazırda bulunuyor.")
    else:
        mevcutolmayan += 1
        f = open(pft_tab_mult, "w")
        open(tab_mult, "w")
    print("\n\nMevcut Olan Dosya Sayısı : " + str(mevcutolmayan))
####################################################################################
## .level04CREATE
def level04create():
    mevcutolmayan = 0
    # 1.
    if os.path.exists(pft_fprime):
        print(pshort_fprime + " Dosyası hali hazırda bulunuyor.")
    else:
        mevcutolmayan += 1
        f = open(pft_fprime, "w")
        open(fprime, "w")
    # 2.
    if os.path.exists(pft_itoa):
        print(pshort_itoa + " Dosyası hali hazırda bulunuyor.")
    else:
        mevcutolmayan += 1
        f = open(pft_itoa, "w")
        open(ft_itoa, "w")
    # 3.
    if os.path.exists(pft_list_foreach):
        print(pshort_list_foreach + " Dosyası hali hazırda bulunuyor.")
    else:
        mevcutolmayan += 1
        f = open(pft_list_foreach, "w")
        open(ft_list_foreach, "w")
    # 3. H FILE
    if os.path.exists(hft_list_foreach):
        print(hshort_list_foreach + " Dosyası hali hazırda bulunuyor.")
    else:
        mevcutolmayan += 1
        f = open(hft_list_foreach, "w")
        open(hlist_foreach, "w")
    # 4.
    if os.path.exists(pft_list_remove_if):
        print(pshort_list_remove_if + " Dosyası hali hazırda bulunuyor.")
    else:
        mevcutolmayan += 1
        f = open(pft_list_remove_if, "w")
        open(ft_list_remove_if, "w")
    # 4. H FILE
    if os.path.exists(hft_list_remove_if):
        print(hshort_list_remove_if + " Dosyası hali hazırda bulunuyor.")
    else:
        mevcutolmayan += 1
        f = open(hft_list_remove_if, "w")
        open(hlist_remove_if, "w")
    # 5.
    if os.path.exists(pft_split):
        print(pshort_split + " Dosyası hali hazırda bulunuyor.")
    else:
        mevcutolmayan += 1
        f = open(pft_split, "w")
        open(ft_split, "w")
    # 6.
    if os.path.exists(pft_rev_wstr):
        print(pshort_rev_wstr + " Dosyası hali hazırda bulunuyor.")
    else:
        mevcutolmayan += 1
        f = open(pft_rev_wstr, "w")
        open(rev_wstr, "w")
    # 7.
    if os.path.exists(pft_rostring):
        print(pshort_rostring + " Dosyası hali hazırda bulunuyor.")
    else:
        mevcutolmayan += 1
        f = open(pft_rostring, "w")
        open(rostring, "w")
    # 8.
    if os.path.exists(pft_sort_int_tab):
        print(pshort_sort_int_tab + " Dosyası hali hazırda bulunuyor.")
    else:
        mevcutolmayan += 1
        f = open(pft_sort_int_tab, "w")
        open(sort_int_tab, "w")
    # 9.
    if os.path.exists(pft_sort_list):
        print(pshort_sort_list + " Dosyası hali hazırda bulunuyor.")
    else:
        mevcutolmayan += 1
        f = open(pft_sort_list, "w")
        open(sort_list, "w")
    # 9. H FILE
    if os.path.exists(hft_sort_list):
        print(hshort_sort_list + " Dosyası hali hazırda bulunuyor.")
    else:
        mevcutolmayan += 1
        f = open(hft_sort_list, "w")
        open(hlist_sort, "w")
    print("\n\nMevcut Olan Dosya Sayısı : " + str(mevcutolmayan))
####################################################################################
def aexeoutremove():
    silinen = 0
    # level01 A.OUT
    if os.path.exists(afirst_word + "a.out"):
        os.remove(afirst_word + "a.out")
        silinen += 1
    if os.path.exists(aputstr + "a.out"):
        os.remove(aputstr + "a.out")
        silinen += 1
    if os.path.exists(astrcpy + "a.out"):
        os.remove(astrcpy + "a.out")
        silinen += 1
    if os.path.exists(aswap + "a.out"):
        os.remove(aswap + "a.out")
        silinen += 1
    if os.path.exists(arepeat_alpha + "a.out"):
        os.remove(arepeat_alpha + "a.out")
        silinen += 1
    if os.path.exists(arevprint + "a.out"):
        os.remove(arevprint + "a.out")
        silinen += 1
    if os.path.exists(arot_13 + "a.out"):
        os.remove(arot_13 + "a.out")
        silinen += 1
    if os.path.exists(arotone + "a.out"):
        os.remove(arotone + "a.out")
        silinen += 1
    if os.path.exists(asaerch_and_replace + "a.out"):
        os.remove(asaerch_and_replace + "a.out")
        silinen += 1
    if os.path.exists(aulstr + "a.out"):
        os.remove(aulstr + "a.out")
        silinen += 1
    # LEVEL02 A.OUT
    if os.path.exists(aalpha_mirror + "a.out"):
        os.remove(aalpha_mirror + "a.out")
        silinen += 1
    if os.path.exists(ado_op + "a.out"):
        os.remove(ado_op + "a.out")
        silinen += 1
    if os.path.exists(a_atoi + "a.out"):
        os.remove(a_atoi + "a.out")
        silinen += 1
    if os.path.exists(astrcmp + "a.out"):
        os.remove(astrcmp + "a.out")
        silinen += 1
    if os.path.exists(astrdup + "a.out"):
        os.remove(astrdup + "a.out")
        silinen += 1
    if os.path.exists(astrrev + "a.out"):
        os.remove(astrrev + "a.out")
        silinen += 1
    if os.path.exists(ainter + "a.out"):
        os.remove(ainter + "a.out")
        silinen += 1
    if os.path.exists(ais_power_of_2 + "a.out"):
        os.remove(ais_power_of_2 + "a.out")
        silinen += 1
    if os.path.exists(alast_word + "a.out"):
        os.remove(alast_word + "a.out")
        silinen += 1
    if os.path.exists(amax + "a.out"):
        os.remove(amax + "a.out")
        silinen += 1
    if os.path.exists(aprint_bits + "a.out"):
        os.remove(aprint_bits + "a.out")
        silinen += 1
    if os.path.exists(areverse_bits + "a.out"):
        os.remove(areverse_bits + "a.out")
        silinen += 1
    if os.path.exists(aswap_bits + "a.out"):
        os.remove(aswap_bits + "a.out")
        silinen += 1
    if os.path.exists(aunion + "a.out"):
        os.remove(aunion + "a.out")
        silinen += 1
    if os.path.exists(awdmatch + "a.out"):
        os.remove(awdmatch + "a.out")
        silinen += 1
    # level03 A.OUT
    if os.path.exists(aadd_prime_sum + "a.out"):
        os.remove(aadd_prime_sum + "a.out")
        silinen += 1
    if os.path.exists(aepur_str + "a.out"):
        os.remove(aepur_str + "a.out")
        silinen += 1
    if os.path.exists(aexpand_str + "a.out"):
        os.remove(aexpand_str + "a.out")
        silinen += 1
    if os.path.exists(aatoi_base + "a.out"):
        os.remove(aatoi_base + "a.out")
        silinen += 1
    if os.path.exists(alist_size + "a.out"):
        os.remove(alist_size + "a.out")
        silinen += 1
    if os.path.exists(arange + "a.out"):
        os.remove(arange + "a.out")
        silinen += 1
    if os.path.exists(arrange + "a.out"):
        os.remove(arrange + "a.out")
        silinen += 1
    if os.path.exists(ahidenp + "a.out"):
        os.remove(ahidenp + "a.out")
        silinen += 1
    if os.path.exists(aparamsum + "a.out"):
        os.remove(aparamsum + "a.out")
        silinen += 1
    if os.path.exists(apgcd + "a.out"):
        os.remove(apgcd + "a.out")
        silinen += 1
    if os.path.exists(aprint_hex + "a.out"):
        os.remove(aprint_hex + "a.out")
        silinen += 1
    if os.path.exists(arstr_capitalizer + "a.out"):
        os.remove(arstr_capitalizer + "a.out")
        silinen += 1
    if os.path.exists(astr_capitalizer + "a.out"):
        os.remove(astr_capitalizer + "a.out")
        silinen += 1
    if os.path.exists(atab_mult + "a.out"):
        os.remove(atab_mult + "a.out")
        silinen += 1
    # level04 A.OUT
    if os.path.exists(afprime + "a.out"):
        os.remove(afprime + "a.out")
        silinen += 1
    if os.path.exists(aitoa + "a.out"):
        os.remove(aitoa + "a.out")
        silinen += 1
    if os.path.exists(alist_foreach + "a.out"):
        os.remove(alist_foreach + "a.out")
        silinen += 1
    if os.path.exists(alist_remove_if + "a.out"):
        os.remove(alist_remove_if + "a.out")
        silinen += 1
    if os.path.exists(asplit + "a.out"):
        os.remove(asplit + "a.out")
        silinen += 1
    if os.path.exists(arev_wstr + "a.out"):
        os.remove(arev_wstr + "a.out")
        silinen += 1
    if os.path.exists(arostring + "a.out"):
        os.remove(arostring + "a.out")
        silinen += 1
    if os.path.exists(asort_int_tab + "a.out"):
        os.remove(asort_int_tab + "a.out")
        silinen += 1
    if os.path.exists(asort_list + "a.out"):
        os.remove(asort_list + "a.out")
        silinen += 1
    # level01 A.EXE
    if os.path.exists(afirst_word + "a.exe"):
        os.remove(afirst_word + "a.exe")
        silinen += 1
    if os.path.exists(aputstr + "a.exe"):
        os.remove(aputstr + "a.exe")
        silinen += 1
    if os.path.exists(astrcpy + "a.exe"):
        os.remove(astrcpy + "a.exe")
        silinen += 1
    if os.path.exists(aswap + "a.exe"):
        os.remove(aswap + "a.exe")
        silinen += 1
    if os.path.exists(arepeat_alpha + "a.exe"):
        os.remove(arepeat_alpha + "a.exe")
        silinen += 1
    if os.path.exists(arevprint + "a.exe"):
        os.remove(arevprint + "a.exe")
        silinen += 1
    if os.path.exists(arot_13 + "a.exe"):
        os.remove(arot_13 + "a.exe")
        silinen += 1
    if os.path.exists(arotone + "a.exe"):
        os.remove(arotone + "a.exe")
        silinen += 1
    if os.path.exists(asaerch_and_replace + "a.exe"):
        os.remove(asaerch_and_replace + "a.exe")
        silinen += 1
    if os.path.exists(aulstr + "a.exe"):
        os.remove(aulstr + "a.exe")
        silinen += 1
    # LEVEL02 A.EXE
    if os.path.exists(aalpha_mirror + "a.exe"):
        os.remove(aalpha_mirror + "a.exe")
        silinen += 1
    if os.path.exists(ado_op + "a.exe"):
        os.remove(ado_op + "a.exe")
        silinen += 1
    if os.path.exists(a_atoi + "a.exe"):
        os.remove(a_atoi + "a.exe")
        silinen += 1
    if os.path.exists(astrcmp + "a.exe"):
        os.remove(astrcmp + "a.exe")
        silinen += 1
    if os.path.exists(astrdup + "a.exe"):
        os.remove(astrdup + "a.exe")
        silinen += 1
    if os.path.exists(astrrev + "a.exe"):
        os.remove(astrrev + "a.exe")
        silinen += 1
    if os.path.exists(ainter + "a.exe"):
        os.remove(ainter + "a.exe")
        silinen += 1
    if os.path.exists(ais_power_of_2 + "a.exe"):
        os.remove(ais_power_of_2 + "a.exe")
        silinen += 1
    if os.path.exists(alast_word + "a.exe"):
        os.remove(alast_word + "a.exe")
        silinen += 1
    if os.path.exists(amax + "a.exe"):
        os.remove(amax + "a.exe")
        silinen += 1
    if os.path.exists(aprint_bits + "a.exe"):
        os.remove(aprint_bits + "a.exe")
        silinen += 1
    if os.path.exists(areverse_bits + "a.exe"):
        os.remove(areverse_bits + "a.exe")
        silinen += 1
    if os.path.exists(aswap_bits + "a.exe"):
        os.remove(aswap_bits + "a.exe")
        silinen += 1
    if os.path.exists(aunion + "a.exe"):
        os.remove(aunion + "a.exe")
        silinen += 1
    if os.path.exists(awdmatch + "a.exe"):
        os.remove(awdmatch + "a.exe")
        silinen += 1
    # level03 A.EXE
    if os.path.exists(aadd_prime_sum + "a.exe"):
        os.remove(aadd_prime_sum + "a.exe")
        silinen += 1
    if os.path.exists(aepur_str + "a.exe"):
        os.remove(aepur_str + "a.exe")
        silinen += 1
    if os.path.exists(aexpand_str + "a.exe"):
        os.remove(aexpand_str + "a.exe")
        silinen += 1
    if os.path.exists(aatoi_base + "a.exe"):
        os.remove(aatoi_base + "a.exe")
        silinen += 1
    if os.path.exists(alist_size + "a.exe"):
        os.remove(alist_size + "a.exe")
        silinen += 1
    if os.path.exists(arange + "a.exe"):
        os.remove(arange + "a.exe")
        silinen += 1
    if os.path.exists(arrange + "a.exe"):
        os.remove(arrange + "a.exe")
        silinen += 1
    if os.path.exists(ahidenp + "a.exe"):
        os.remove(ahidenp + "a.exe")
        silinen += 1
    if os.path.exists(aparamsum + "a.exe"):
        os.remove(aparamsum + "a.exe")
        silinen += 1
    if os.path.exists(apgcd + "a.exe"):
        os.remove(apgcd + "a.exe")
        silinen += 1
    if os.path.exists(aprint_hex + "a.exe"):
        os.remove(aprint_hex + "a.exe")
        silinen += 1
    if os.path.exists(arstr_capitalizer + "a.exe"):
        os.remove(arstr_capitalizer + "a.exe")
        silinen += 1
    if os.path.exists(astr_capitalizer + "a.exe"):
        os.remove(astr_capitalizer + "a.exe")
        silinen += 1
    if os.path.exists(atab_mult + "a.exe"):
        os.remove(atab_mult + "a.exe")
        silinen += 1
    # level04 A.EXE
    if os.path.exists(afprime + "a.exe"):
        os.remove(afprime + "a.exe")
        silinen += 1
    if os.path.exists(aitoa + "a.exe"):
        os.remove(aitoa + "a.exe")
        silinen += 1
    if os.path.exists(alist_foreach + "a.exe"):
        os.remove(alist_foreach + "a.exe")
        silinen += 1
    if os.path.exists(alist_remove_if + "a.exe"):
        os.remove(alist_remove_if + "a.exe")
        silinen += 1
    if os.path.exists(asplit + "a.exe"):
        os.remove(asplit + "a.exe")
        silinen += 1
    if os.path.exists(arev_wstr + "a.exe"):
        os.remove(arev_wstr + "a.exe")
        silinen += 1
    if os.path.exists(arostring + "a.exe"):
        os.remove(arostring + "a.exe")
        silinen += 1
    if os.path.exists(asort_int_tab + "a.exe"):
        os.remove(asort_int_tab + "a.exe")
        silinen += 1
    if os.path.exists(asort_list + "a.exe"):
        os.remove(asort_list + "a.exe")
        silinen += 1
    print("\n\nSilinen Dosya Sayısı : " + str(silinen))
####################################################################################
welcome = Fore.CYAN + """
----------- examWIPE -----------"""
welcome += """""" + Fore.LIGHTRED_EX + """
1- Exam Dosya Silme
2- Exam Dosya Oluşturma
3- a.out Dosyalarını Sil
4- Exit
"""
welcome += """""" + Fore.CYAN + """--------------------------------"""
####################################################################################
dosyasilme = Fore.CYAN + """
----------- examWIPE -----------"""
dosyasilme += """""" + Fore.LIGHTRED_EX + """
1- level01'ı Sil
2- level02'ı Sil
3- level03'ı Sil
4- level04'ı Sil
5- Hepsini Sil
6- Exit
"""
dosyasilme += """""" + Fore.CYAN + """--------------------------------"""
#####################
dosyaolustur = Fore.CYAN + """
----------- examWIPE -----------"""
dosyaolustur += """""" + Fore.LIGHTRED_EX + """
1- level01'ı oluştur
2- level02'ı oluştur
3- level03'ı oluştur
4- level04'ı oluştur
5- Hepsini oluştur
6- Exit
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
            level01remove()
        elif secim2 == "2":
            level02remove()
        elif secim2 == "3":
            level03remove()
        elif secim2 == "4":
            level04remove()
        elif secim2 == "5":
            level01remove()
            level02remove()
            level03remove()
            level04remove()
        elif secim2 == "6":
            exit()
    elif secim == "2":
        print(dosyaolustur + Fore.WHITE)
        secim3 = input("Yeni Seçim Numaranızı Giriniz: ")
        if secim3 == "1":
            level01create()
        elif secim3 == "2":
            level02create()
        elif secim3 == "3":
            level03create()
        elif secim3 == "4":
            level04create()
        elif secim3 == "5":
            level01create()
            level02create()
            level03create()
            level04create()
        elif secim3 == "6":
            exit()
    elif secim == "3":
        aexeoutremove()
    elif secim == "4":
        exit()
    else:
        print("Lütfen Doğru Seçim Yapınız!")
        exit()
