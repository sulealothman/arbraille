# arbraille
Arabic braille translator package


## Requirement :

- Install argparse lib, "pip3 install argparse" -> for linux & macos | "pip install argparse" for windows


## Examples :

- Convert from alphabet to braille

```
import braille

txt = "السلام عليكم و رحمة الله و بركاته"
br = braille.AlphabetToBraille()
output = br.convert(txt)
print(output)
```

- Convert Files on command line ( from alphabet arabic to braille )

```
python3 braille.py -f input.txt -o output.txt -t ar2br
```


- Convert Files on command line ( from braille to alphabet arabic )

```
python3 braille.py -f input.txt -o output.txt -t br2ar
```


## Supports

- all letters from أ - ي

- all numbers from 0 - 9
