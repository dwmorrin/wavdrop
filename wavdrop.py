#!/usr/bin/env python3
""" randomly zero out samples in a .wav file """
from random import choice, sample
import argparse
import wave

parser = argparse.ArgumentParser(
        description="Randomly zero out samples in a .wav file")
parser.add_argument('-o', '--output', help="output filename",
        dest='filename', default="bad.wav")
parser.add_argument('-n', '--drops', help="number of dropped samples",
        dest='ndrops', type=int, default=10)
parser.add_argument('-s', '--stereo', help="apply drops to stereo channels separately",
        action='store_true')
parser.add_argument('-w', '--width', help="width of dropped samples",
        dest='drop_width', type=int, default=3)
parser.add_argument('input_file')
args = parser.parse_args()

# read input file
wav_read = wave.open(args.input_file, 'rb')
wav_params = wav_read.getparams()
data = bytearray(wav_read.readframes(wav_params.nframes))
wav_read.close()

# pick random times to drop samples, print times to stdout, and apply to data
def time_of_sample(sample_rate, sample):
    return float(sample)/float(sample_rate)

drops = sample(range(wav_params.nframes - args.drop_width), args.ndrops)
drops.sort()
print("Dropping at the following times [seconds]:")
FRAME_SIZE = wav_params.nchannels * wav_params.sampwidth
dropped_channel = ""
for n in drops:
    start_index = FRAME_SIZE * n
    if args.stereo:
        dropped_channel = choice(['L', 'R'])
    for i in range(args.drop_width):
        for j in range(wav_params.nchannels):
            if args.stereo and dropped_channel == 'L' and j == 1:
                continue
            if args.stereo and dropped_channel == 'R' and j == 0:
                continue
            for k in range(wav_params.sampwidth):
                data[start_index + i*FRAME_SIZE + j*wav_params.sampwidth + k] = 0
    print("\t{}{:7.3f} s".format(dropped_channel, time_of_sample(wav_params.framerate, n)))

# write output file
wav_write = wave.open(args.filename, 'wb')
wav_write.setparams(wav_params)
wav_write.writeframes(data)
wav_write.close()
