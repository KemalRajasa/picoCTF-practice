HASH CRACKING

identify the hashed character : bvi level4.hash.bin

store the hashed character in hash.txt

identify hash type using : hash-identifier [hashed character]

result is md5 hash


store the password list to a new txt.file using grep:
grep "pos_pw_list" level4.py | sed 's/.*\[//; s/]//; s/,/\n/g; s/"//g; s/ //g' > wordlist.txt

use hashcat to automate loop through the wordlist:
hashcat -m 0 hashcat.txt wordlist.txt

hashcat -m 0 hashcat.txt wordlist.txt --show
