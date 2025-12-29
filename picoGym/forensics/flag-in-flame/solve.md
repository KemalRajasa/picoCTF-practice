# 1. Decode log

```bash
base64 -d logs.txt > decoded_logs
```

# 2. File has a magic number of a PNG file

```bash
cat decoded_logs | hexdump -C
```

# 3. Change file extension to PNG

# 4. Flag in hex format
