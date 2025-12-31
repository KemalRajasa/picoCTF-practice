# 1. Examine metadata

```bash
exiftool flag.png
```
Found an interesting column in the output:

```bash
Warning                         : [minor] Trailer data after PNG IEND chunk
```

Stating that after the IEND chunk (supposed to be the end of PNG file) there is some extra data.

# 2. Read raw binary content

```bash
hexdump -C flag.png > raw.txt
```

inside raw.txt we can see the extra data (that ive extracted to raw-extra.txt), im assuming that there is a file within a file (polyglot)

# 3. Extract the hidden file using binwalk

```bash
binwalk -e flag.png
```
flag could be found in _flag.png.extracted/secret/flag.png file.