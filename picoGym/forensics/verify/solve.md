# Find a file with same sha265sum value

```bash
find . -type f -exec sha256sum {} + | grep "fba9f49bf22aa7188a155768ab0dfdc1f9b86c47976cd0f7c9003af2e20598f7"

# find .: Mencari di direktori saat ini (.).

# -type f: Hanya mencari file (mengabaikan folder).

# -exec md5sum {} +: Menjalankan perintah md5sum pada file yang ditemukan. Tanda + di akhir membuat perintah ini sangat efisien karena dia akan memproses banyak file sekaligus dalam satu command (batch), bukan satu per satu.

# | grep "...": Memfilter output hanya untuk hash yang cocok.
```

```bash
ctf-player@pico-chall$ ls
checksum.txt  decrypt.sh  files
ctf-player@pico-chall$ cat checksum.txt
fba9f49bf22aa7188a155768ab0dfdc1f9b86c47976cd0f7c9003af2e20598f7
ctf-player@pico-chall$ find . -type f -exec sha256sum {} + | grep "fba9f49bf22aa7188a155768ab0dfdc1f9b86c47976cd0f7c9003af2e20598f7"
fba9f49bf22aa7188a155768ab0dfdc1f9b86c47976cd0f7c9003af2e20598f7  ./files/87590c24
ctf-player@pico-chall$ bash decrypt.sh files/87590c24 
picoCTF{trust_REDACTED_REDACTED_REDACTED}
ctf-player@pico-chall$ 
```