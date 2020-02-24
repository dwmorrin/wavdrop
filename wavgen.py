""" generate .wav file containing test tone """
from array import array
from math import floor, pi, sin, asin, tan, atan
from struct import pack
import wave

max_value = 32760

def byte16(int):
    """ formats signed 16 bit int to 2x 8 bits """
    if int > max_value or int < -max_value:
        raise ValueError
    return pack("<h", int)

def scale(x, amplitude=0.5, master=0.8):
    return round(x * max_value * amplitude * master)

def saw(x):
    return (2/pi) * atan(tan(x))

def square(x):
    return -1 if sin(x) < 0 else 1

def tri(x):
    return (2/pi) * asin(sin(x))

"""
radians               1 second    frequency cycles    2pi radians
-------- = -------------------- x ---------------- x  -----------
sample      sample_rate samples             second        cycle

"""
def rads_per_sample(frequency, sample_rate):
    return frequency * 2 * pi / sample_rate

def write_samples(wav_write, sample_rate, frequency, duration, func=sin, fade_in_duration=0.01, fade_out_duration=0.01):
    n_samples = int(sample_rate * duration)
    n_fade_in_end = int(sample_rate * fade_in_duration)
    n_fade_out_samples = int(sample_rate * fade_out_duration)
    n_fade_out_start = n_samples - n_fade_out_samples
    
    angle_rate = rads_per_sample(frequency, sample_rate)
    amplitude = 0.0
    fade_in_inc = 1/float(n_fade_in_end)
    fade_out_dec = 1/float(n_fade_out_samples)
    for sample in range(n_samples):
        if sample <= n_fade_in_end:
            amplitude += fade_in_inc
        if sample >= n_fade_out_start:
            amplitude -= fade_out_dec
        wav_file.writeframesraw(byte16(scale(func(sample*angle_rate), amplitude)))

sample_rate = 44100 # Hz
wav_file = wave.open("tone.wav", "wb")
wav_file.setnchannels(1)
wav_file.setsampwidth(2)
wav_file.setframerate(sample_rate)
semitone_ratio = 2**(1/12)
skip = [1, 3, 6, 8, 10]
for x in range(2):
    f = 440
    func = sin
    #if x < 2:
    #    func = sin
    #elif x < 8:
    #    funx = tri
    #elif x < 12:
    #    func = saw
    #else:
    #    func = square
    for i in range(13):
        f *= semitone_ratio
        if i not in skip:
            write_samples(wav_file, sample_rate, f, 1, func)
wav_file.close()
