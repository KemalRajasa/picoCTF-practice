# 1. Why is it broken

```bash
hexdump -C file | head
```

```bash
00000000  5c 78 ff e0 00 10 4a 46  49 46 00 01 01 00 00 01  |\x....JFIF......|
00000010  00 01 00 00 ff db 00 43  00 08 06 06 07 06 05 08  |.......C........|
00000020  07 07 07 09 09 08 0a 0c  14 0d 0c 0b 0b 0c 19 12  |................|
```

the header had JFIF (which is the magic number for a JPEG file) but the first 2 bytes of the magic number were altered, fix magic number

```bash
hexeditor file
```

```bash
00000000  5c 78 ff e0 00 10 4a 46  49 46 00 01 01 00 00 01  |\x....JFIF......| # before
```

```bash
00000000  ff e0 00 10 4a 46  49 46 00 01 01 00 00 01 00 01  |....JFIF......| # after
```