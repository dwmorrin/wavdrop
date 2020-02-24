""" randomly zero out samples in a .wav file """
import argparse
import wave

parser = argparse.ArgumentParser(
        description="Randomly zero out samples in a .wav file")
parser.add_argument('-o', '--output', help="output filename",
        dest='filename', default="bad.wav", action='store')
parser.add_argument('input_file')
args = parser.parse_args()

# read input file
wav_read = wave.open(args.input_file, 'rb')
wav_params = wav_read.getparams()
data = bytearray(wav_read.readframes(wav_params.nframes))
wav_read.close()

# write output file
wav_write = wave.open(args.filename, 'wb')
wav_write.setparams(wav_params)
wav_write.writeframes(data)
wav_write.close()
