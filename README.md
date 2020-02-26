# wavdrop

Corrupt .wav files for the purpose of ear training.
```
usage: wavdrop.py [-h] [-o FILENAME] [-n NDROPS] [-w DROP_WIDTH] input_file

Randomly zero out samples in a .wav file

positional arguments:
  input_file

optional arguments:
  -h, --help            show this help message and exit
  -o FILENAME, --output FILENAME
                        output filename
  -n NDROPS, --drops NDROPS
                        number of dropped samples
  -w DROP_WIDTH, --width DROP_WIDTH
                        width of dropped samples
```

## wavgen

To generate .wav files for testing, see [wavgen](https://github.com/dwmorrin/wavgen)
