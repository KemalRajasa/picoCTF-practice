# general rot13 solution
Gunakan 'tr' untuk melakukan substitusi ROT13
'A-Za-z' adalah set karakter input
'N-ZA-Mn-za-m' adalah set karakter output yang sesuai

# script
# Gunakan 'tr' untuk melakukan substitusi ROT13
# 'A-Za-z' adalah set karakter input
rot13_text=$(tr 'A-Za-z' 'N-ZA-Mn-za-m' <<< "$input_text")
