# Colors
purple=$'\033[1;34m'
reset=$'\033[0;39m'
red=$'\033[0;31m'
green=$'\033[0;32m'

# Comand
echo "Gerekli Modüller İndiriliyor";
pip3 install colorama
clear;
read -n1 -p "${purple}Gerekli modüller indirildi, RANK 04 examWIPE'ın başlatılmasını onaylamak için: [${green}y${purple}/${red}N${purple}]${reset} " input
if [ -n "$input" ] && [ "$input" = "y" ]; then
	echo;
	echo "İşlem başarıyla onaylandı, iyi çalışmalar dilerim. -eyagiz";
	sleep 3
	clear;
	python3 py/remove.py
	else
	echo "Yanlış seçenek seçildi.";
	fi
