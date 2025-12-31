# 1. Clue gathering:

```
This file contains more than it seems.
```

# 2. Examine raw file

```bash
hexdump -C garden.jpg > raw.txt
```

# 3. Extract flag

after analyzing the raw.txt file, we can see that the flag is after the image raw hex values (search for "FF D9" which is the end of the image).
