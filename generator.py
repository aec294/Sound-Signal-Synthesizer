import time

import numpy as np
import pyaudio

p = pyaudio.PyAudio()

durations = {
    "s": 1/16,
    "e": 1/8,
    "q": 1/4,
    "h": 1/2,
    "w": 1
}

freqs = {
    "R": 0,
    "C": 16.3516015625,
    "C#": 17.32390625,
    "Db": 17.32390625,
    "D": 18.3540234375,
    "D#": 19.4454296875,
    "Eb": 19.4454296875,
    "E": 20.60171875,
    "F": 21.8267578125,
    "F#": 23.1246484375,
    "Gb": 23.1246484375,
    "G": 24.4997265625,
    "G#": 25.9565625,
    "Ab": 25.9565625,
    "A": 27.50,
    "A#": 29.135234375,
    "Bb": 29.135234375,
    "B": 30.8676953125
}

Keys = {
    'C': ['C', 'D', 'E' 'F', 'G', 'A', 'B'],

    'G': ['F#'],
    'Em': ['F#'],
    'D': ['F#', 'C#'],
    'Bm': ['F#', 'C#'],
    'A': ['F#', 'C#', 'G#'],
    'F#m': ['F#', 'C#', 'G#'],
    'E': ['F#', 'C#', 'G#', 'D#'],
    'C#m': ['F#', 'C#', 'G#', 'D#'],
    'B': ['F#', 'C#', 'G#', 'D#', 'A#'],
    'G#m': ['F#', 'C#', 'G#', 'D#', 'A#'],
    'F#': ['F#', 'C#', 'G#', 'D#', 'A#', 'E#'],
    'D#m': ['F#', 'C#', 'G#', 'D#', 'A#', 'E#'],
    'C#': ['F#', 'C#', 'G#', 'D#', 'A#', 'E#', 'B#'],
    'A#m': ['F#', 'C#', 'G#', 'D#', 'A#', 'E#', 'B#'],

    'F': ['Bb'],
    'Dm': ['Bb'],
    'Bb': ['Bb', 'Eb'],
    'Gm': ['Bb', 'Eb'],
    'Eb': ['Bb', 'Eb', 'Ab'],
    'Cm': ['Bb', 'Eb', 'Ab'],
    'Ab': ['Bb', 'Eb', 'Ab', 'Db'],
    'Fm': ['Bb', 'Eb', 'Ab', 'Db'],
    'Db': ['Bb', 'Eb', 'Ab', 'Db', 'Gb'],
    'Bbm': ['Bb', 'Eb', 'Ab', 'Db', 'Gb'],
    'Gb': ['Bb', 'Eb', 'Ab', 'Db', 'Gb', 'Cb'],
    'Ebm': ['Bb', 'Eb', 'Ab', 'Db', 'Gb', 'Cb'],
    'Cb': ['Bb', 'Eb', 'Ab', 'Db', 'Gb', 'Cb', 'Fb'],
    'Abm': ['Bb', 'Eb', 'Ab', 'Db', 'Gb', 'Cb', 'Fb'],
}

def play_seq(seq, duration, volume=1, sample_rate=44100):
    fs = []
    durs = []
    for i in range(len(seq)):
        notes = seq[i][:-1] if type(seq[i]) == list else [seq[i]]
        length = durations[seq[i][-1]] if type(seq[i]) == list else durations[seq[i].split("-")[1]]
        durs.append(duration*length)
        fs.append([])
        for note in notes:
            note = note.split("-")[0]
            if note == "R":
                fs[i].append(0)
            else:
                octave = int(note[-1])
                base = note[:-1]
                fs[i].append(freqs[base]*2**octave)

    # generate samples, note conversion to float32 array
    samples = []
    vol_scl = 1/len(fs)
    for i in range(len(fs)):
        samples.append([])
        samples[i] = (np.sin(2*np.pi*np.arange(sample_rate*durs[i])*fs[i][0]/sample_rate)).astype(np.float32)
        vol = volume - vol_scl * i
        for f in fs[i][1:]:
            samples[i] += (vol*np.sin(2*np.pi*np.arange(sample_rate*durs[i])*f/sample_rate)).astype(np.float32)
        samples[i] = (samples[i]).tobytes()

    # for paFloat32 sample values must be in range [-1.0, 1.0]
    stream = p.open(format=pyaudio.paFloat32,
                    channels=1,
                    rate=sample_rate,
                    output=True)

    # play. May repeat with different volume values (if done interactively)
    for i in range(len(samples)):
        start_time = time.time()
        stream.write(samples[i])
        print("Played sound for {:.2f} seconds".format(time.time() - start_time))

    stream.stop_stream()
    stream.close()

    p.terminate()

def generate_note(keys, octaves):
    return

def generate_seq(num_notes, keys, octaves):
    out = []
    for _ in num_notes:
        out.append(generate_note(keys, octaves))
    return out

N = 100
q = 180 #240 #180 #72
duration = 60/q*4  # in seconds, may be float

if __name__ == "__main__":
    sequence = generate_seq(N)
    play_seq(sequence, duration)
