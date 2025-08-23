tools used:
hash-identifier
hashcat
bvi

first of all identify where is the hashed string located
by reading the hash.bin file using bvi
found a character 1B 18 E1 31 6F 92 18 CC 5B 05 3E 1C EA 28 E0 2E 

second, use hash-identifier to decrypt the string but identfier cant detect current format with space as separator
1B18E1316F9218CC5B053E1CEA28E02E 
hash-identifier identified that its a md5 hash then store it in hash.txt

third step is to decrypt the hashed string with the possible password list in level3.py
since its identified that its a md5 "-m 0" is used for the hashcat argument
hashcat -m 0 hash.txt level3.py

then

hashcat -m 0 hash.txt level3.py --show

password will be shown and the correct password is "865e"
