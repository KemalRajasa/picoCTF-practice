chr(0x33) + chr(0x39) + chr(0x63) + chr(0x65)

format 0x,, mengindikasi jika angka tersebut adalah hexadecimal, convert tiap karakter menjadi decimal
0x33 --> 51 
0x39  --> 57
0x63 --> 99  
0x65 --> 101 

dilihat dari file python terdapat fungsi chr() untuk merubah karakter menjadi ASCII

chr(51) --> 3
chr(57) -> 9
chr(99) --> c
chr(101) --> e

pw: 39ce

##FLAG
picoCTF{tr45h_51ng1ng_502ec42e}
