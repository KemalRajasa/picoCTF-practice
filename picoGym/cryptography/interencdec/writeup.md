
input 1:

```
echo "YidkM0JxZGtwQlRYdHFhR3g2YUhsZmF6TnFlVGwzWVROclgya3lNRFJvYTJvMmZRPT0nCg==" | base64 --
decode
```
output 1:

```
b'd3BqdkpBTXtqaGx6aHlfazNqeTl3YTNrX2kyMDRoa2o2fQ=='
```

looks like its still in base64 format, decode it once more

input 2 :
```
echo "b'd3BqdkpBTXtqaGx6aHlfazNqeTl3YTNrX2kyMDRoa2o2fQ=='" | base64 --decode
```

output 2:
`base64: invalid input`


input 3:

in this attempt remove the `b''`

`echo "d3BqdkpBTXtqaGx6aHlfazNqeTl3YTNrX2kyMDRoa2o2fQ==" | base64 --decode`

output 3:

`wpjvJAM{jhlzhy_k3jy9wa3k_i204hkj6}`

this is already looks like a plain text, next try caesar cipher shift after many attempts
right shift 7 will return the flag
