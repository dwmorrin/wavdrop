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

wavgen makes .wav files for testing wavdrop.
```
usage: wavgen.py [-h] [-d DURATION] [-f FREQUENCY] [-o FILENAME]
                 [-r SAMPLE_RATE] [-w WAVEFORM] [-t TYPE]

Generate .wav file using direct digital synthesis

optional arguments:
  -h, --help            show this help message and exit
  -d DURATION, --duration DURATION
                        duration of tone
  -f FREQUENCY, --frequency FREQUENCY
                        audio frequency
  -o FILENAME, --output FILENAME
                        output filename
  -r SAMPLE_RATE, --rate SAMPLE_RATE
                        sample rate
  -w WAVEFORM, --waveform WAVEFORM
                        sin|tri|saw|square
  -t TYPE, --type TYPE  tone|constant|scale|slope
```
