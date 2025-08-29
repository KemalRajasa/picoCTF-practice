└─# ls -la
total 24
drwxr-xr-x  2 root    root    4096 Aug 29 22:37 .
drwxr-xr-x 28 root    root    4096 Aug 29 22:35 ..
-rwxrwxrwx  1 rjskali rjskali  785 Aug 29 22:35 ltdis.sh
-rw-r--r--  1 root    root       0 Aug 29 22:39 .ltdis.x86_64.txt
-rwxrwxrwx  1 rjskali rjskali 8376 Aug 29 22:36 static

└─# bash ltdis.sh static
Attempting disassembly of static ...
Disassembly successful! Available at: static.ltdis.x86_64.txt
Ripping strings from binary with file offsets...
Any strings found in static have been written to static.ltdis.strings.txt with file offset

└─# grep "pico" static.ltdis.strings.txt 
   1020 picoCTF{d15a5m_t34s3r_6f8c8200}
