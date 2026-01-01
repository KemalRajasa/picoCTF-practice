

# 1. Examine filetype

```bash
file mystery

# Output:
mystery: data
```
```bash
exiftool mystery

# Output:
ExifTool Version Number         : 13.25
File Name                       : mystery
Directory                       : .
File Size                       : 203 kB
File Modification Date/Time     : 2025:11:15 02:58:37+07:00
File Access Date/Time           : 2025:12:31 23:20:30+07:00
File Inode Change Date/Time     : 2025:12:31 23:20:30+07:00
File Permissions                : -rw-r--r--
Error                           : Unknown file type
```

```bash
hexdump -C mystery > raw.txt

# after examining the end of file, it has an IEND chunk which is the end of a PNG file
# but it the first 8 bit magic number / file signature is incorrect
tail raw.txt
```

# 2. Fix header / file signature

Using ghex i edited the file signature from :

```bash
└─$ head -n 1 raw.txt
00000000  89 65 4e 34 0d 0a b0 aa  00 00 00 0d 43 22 44 52  |.eN4........C"DR|
```
to :

```bash
└─$ head -n 1 raw.txt
00000000  89 50 4e 47 0d 0a 1a 0a  00 00 00 0d 49 48 44 52  |.PNG........IHDR|
```
then store the image as `mystery.png`

examine the new file using `pngcheck`

```bash
└─$ pngcheck -c -v mystery.png

File: mystery.png (202940 bytes)
  chunk IHDR at offset 0x0000c, length 13
    1642 x 1095 image, 24-bit RGB, non-interlaced
  chunk sRGB at offset 0x00025, length 1
    rendering intent = perceptual
  chunk gAMA at offset 0x00032, length 4: 0.45455
  chunk pHYs at offset 0x00042, length 9: 2852132389x5669 pixels/meter
  CRC error in chunk pHYs (computed 38d82c82, expected 495224f0)
ERRORS DETECTED in mystery-docum.png
```
notice the CRC error in the pHYs chunk. 

```bash
  CRC error in chunk pHYs (computed 38d82c82, expected 495224f0)
```

# 3. Fix CRC error

using ghex i edited the CRC error in the pHYs chunk from :

```bash
# CRC chunk as stated in the error from pngcheck earlier was `49 52 24 f0`

00000040  00 09 70 48 59 73 aa 00  16 25 00 00 16 25 01 49  |..pHYs...%...%.I|
00000050  52 24 f0 aa aa ff a5 ab  44 45 54 78 5e ec bd 3f  |R$......DETx^..?|
```

change it to :

```bash

00000040  00 09 70 48 59 73 aa 00  16 25 00 00 16 25 01 38  |..pHYs...%...%.8|
00000050  d8 2c 82 aa aa ff a5 ab  44 45 54 78 5e ec bd 3f  |.,......DETx^..?|
```

save the edited file then recheck the png using `pngcheck`

```bash
└─$ pngcheck -c -v mystery.png 

File: mystery-docum.png (202940 bytes)
  chunk IHDR at offset 0x0000c, length 13
    1642 x 1095 image, 24-bit RGB, non-interlaced
  chunk sRGB at offset 0x00025, length 1
    rendering intent = perceptual
  chunk gAMA at offset 0x00032, length 4: 0.45455
  chunk pHYs at offset 0x00042, length 9: 2852132389x5669 pixels/meter
:  invalid chunk length (too large)
ERRORS DETECTED in mystery-docum.png
```

now CRC chunk is solved, remaining issue is the pHYs chunk has an invalid length, it has more than 2 billion pixels/meter.

# 4. Fix pHYs chunk

```bash

00000040  00 09 70 48 59 73 aa 00  16 25 00 00 16 25 01 38  |..pHYs...%...%.8|
```

the next 8 bits after `09 70 48 59` is the content of the pHYs chunk which detailed below:

| Name | Length | Current Value |
| --- | --- | --- |
| Pixels per unit, X axis | 4 bytes (PNG unsigned integer) | aa 00 16 25 |
| Pixels per unit, Y axis | 4 bytes (PNG unsigned integer) | 00 00 16 25 |
| Unit specifier | 1 byte | 01 |

the AA bit is the most significant bit of the X axis. In hexadecimal AA means 170 and because its the msb it will be 170 * 2^24 = 2852132389 pixels per meter that explain the error from pngcheck. 

change the AA bit to 00 to fix the error.

```bash
00000040  00 09 70 48 59 00 00  16 25 00 00 16 25 01 38  |..pHYs...%...%.8|
```

save the edited file then recheck the png using `pngcheck`

```bash
pngcheck mystery.png

File: mystery.png (202940 bytes)
  chunk IHDR at offset 0x0000c, length 13
    1642 x 1095 image, 24-bit RGB, non-interlaced
  chunk sRGB at offset 0x00025, length 1
    rendering intent = perceptual
  chunk gAMA at offset 0x00032, length 4: 0.45455
  chunk pHYs at offset 0x00042, length 9: 5669x5669 pixels/meter (144 dpi)
ERRORS DETECTED in mystery.png
```

now solve the remaining issue

# 5. Fix IDAT chunk name

notice after the `pHYs` and `CRC` chunk, there is no IDAT chunk. An `IDAT` chunk but a chunk named `.DET`

```bash
00000040  00 09 70 48 59 73 aa 00  16 25 00 00 16 25 01 38  |..pHYs...%...%.8|
00000050  d8 2c 82 aa aa ff a5 ab  44 45 54 78 5e ec bd 3f  |.,......DETx^..?|
```

change the `DET` which is `44 45 54` to  `49 44 41 54`

```bash
00000040  00 09 70 48 59 73 00 00  16 25 00 00 16 25 01 49  |..pHYs...%...%.I|
00000050  52 24 f0 00 00 ff a5 49  44 41 54 78 5e ec bd 3f  |R$.....IDATx^..?|
```

save the edited file.

# 6. Fix more IDAT issue

using binwalk with -R option to find all IDAT c
>-R, --raw=str Scan target file(s) for the specified sequence of bytes

```bash
binwalk -R "IDAT" mystery.png
```

output:

```bash
DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
87            0x57            Raw signature (IDAT)
65544         0x10008         Raw signature (IDAT)
131080        0x20008         Raw signature (IDAT)
196616        0x30008         Raw signature (IDAT)
```

remember the byte that the fifth step in this writeup worked on to fixed the IDAT chunk, its the same as the IDAT mentioned in the binwalk output for the 87th byte.

```bash
00000050  52 24 f0 aa aa ff a5 49  44 41 54 78 5e ec bd 3f  |R$.....IDATx^..?|
```

so the 4 byte before the 87th byte (which is the I from IDAT `49`) is the length of the IDAT chunk. 

```bash
# length
AA AA FF A5
```

Notice the length of the IDAT chunk contains `AA AA` which is 2852132389 in decimal. its the same length error from the earlier pHYs chunk error.

now to make it a reasonable size change the AA to 00 so the length became `00 00 FF A5` which is 65.445 bytes in decimal

```bash
00000050  52 24 f0 00 00 ff a5 49  44 41 54 78 5e ec bd 3f  |R$.....IDATx^..?|
```

# 7. Validate

```bash
pngcheck mystery.png

OK: mystery.png (1642x1095, 24-bit RGB, non-interlaced, 96.3%).
```
