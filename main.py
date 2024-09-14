import time
import numpy as np
import pyaudio
import argparse

p = pyaudio.PyAudio()

# mario
bigram_spd = {"E5-e": {"": 9, "\\s": 1, "E5-e": 1, "R-e": 1, "C4-e": 4, "G3-e": 2}, "\\s": {"": 1}, "R-e": {"": 20, "E5-e": 4, "C5-q": 4, "G4-q": 2, "E4-q": 2, "G5-e": 2, "B4-q": 2, "Eb5-q": 2, "D5-q": 2}, "C5-e": {"": 11, "R-e": 1, "E5-q": 2, "A5-e": 8}, "E5-q": {"": 5, "C5-e": 1, "G4-e": 2, "R-e": 2}, "G5-q": {"": 1, "E5-q": 1}, "R-q": {"": 2, "G5-q": 1, "G4-q": 1}, "G4-q": {"": 3, "R-q": 1, "R-e": 2}, "C5-q": {"": 4, "R-q": 1, "R-e": 3}, "E4-q": {"": 2, "R-e": 2}, "A4-q": {"": 4, "R-e": 2, "Bb4-e": 2}, "B4-q": {"": 4, "A4-q": 2, "D5-e": 2}, "Bb4-e": {"": 2, "B4-q": 2}, "G4-e": {"": 2, "A4-q": 2}, "G5-e": {"": 10, "E5-q": 2, "F5-e": 2, "C3-q": 6}, "A5-q": {"": 2, "G5-e": 2}, "F5-e": {"": 8, "A5-q": 2, "F#5-e": 6}, "D5-e": {"": 6, "C5-e": 6}, "C3-q": {"": 10, "R-e": 1, "D5-e": 4, "G3-q": 4, "C3-q": 1}, "F#5-e": {"": 6, "G5-e": 6}, "D#5-e": {"": 6, "F5-e": 6}, "C4-e": {"": 8, "D#5-e": 4, "C5-e": 4}, "F3-e": {"": 4, "E5-e": 4}, "G#5-e": {"": 4, "F3-e": 4}, "A5-e": {"": 8, "G#5-e": 4, "C4-e": 4}, "G3-e": {"": 4, "D#5-e": 2, "R-e": 2}, "C6-q": {"": 4, "R-e": 2, "C6-e": 2}, "C6-e": {"": 2, "C6-q": 2}, "G3-q": {"": 4, "C6-q": 2, "G3-e": 2}, "Eb5-q": {"": 2, "C3-q": 2}, "D5-q": {"": 2, "R-e": 2}, "\\e": {"": 0, "C3-q": 1}}

# mario + br
# bigram_spd = {"E5-e": {"": 39, "\\s": 1, "E5-e": 11, "R-e": 3, "C4-e": 4, "G3-e": 2, "D5-e": 2, "F5-e": 8, "E5-q": 2, "A4-q": 6}, "\\s": {"": 2}, "R-e": {"": 31, "E5-e": 8, "C5-q": 5, "G4-q": 2, "E4-q": 2, "G5-e": 2, "B4-q": 2, "Eb5-q": 2, "D5-q": 3, "F5-q": 2, "R-e": 2, "R-q": 1}, "C5-e": {"": 21, "R-e": 4, "E5-q": 2, "A5-e": 8, "R-h": 1, "E5-e": 2, "C5-e": 2, "A4-e": 2}, "E5-q": {"": 7, "C5-e": 1, "G4-e": 2, "R-e": 2, "D5-q": 2}, "G5-q": {"": 1, "E5-q": 1}, "R-q": {"": 5, "G5-q": 1, "G4-q": 1, "C5-q": 1, "D5-q": 1, "R-e": 1}, "G4-q": {"": 3, "R-q": 1, "R-e": 2}, "C5-q": {"": 10, "R-q": 1, "R-e": 3, "B4-e": 2, "D5-q": 2, "A4-e": 2}, "E4-q": {"": 2, "R-e": 2}, "A4-q": {"": 14, "R-e": 2, "Bb4-e": 2, "R-h": 1, "A4-q": 4, "A4-e": 2, "E5-e": 2, "C5-q": 1}, "B4-q": {"": 4, "A4-q": 2, "D5-e": 2}, "Bb4-e": {"": 2, "B4-q": 2}, "G4-e": {"": 2, "A4-q": 2}, "G5-e": {"": 10, "E5-q": 2, "F5-e": 2, "C3-q": 6}, "A5-q": {"": 2, "G5-e": 2}, "F5-e": {"": 16, "A5-q": 2, "F#5-e": 6, "E5-e": 8}, "D5-e": {"": 10, "C5-e": 8, "E5-e": 2}, "C3-q": {"": 10, "R-e": 1, "D5-e": 4, "G3-q": 4, "C3-q": 1}, "F#5-e": {"": 6, "G5-e": 6}, "D#5-e": {"": 6, "F5-e": 6}, "C4-e": {"": 8, "D#5-e": 4, "C5-e": 4}, "F3-e": {"": 4, "E5-e": 4}, "G#5-e": {"": 4, "F3-e": 4}, "A5-e": {"": 8, "G#5-e": 4, "C4-e": 4}, "G3-e": {"": 4, "D#5-e": 2, "R-e": 2}, "C6-q": {"": 4, "R-e": 2, "C6-e": 2}, "C6-e": {"": 2, "C6-q": 2}, "G3-q": {"": 4, "C6-q": 2, "G3-e": 2}, "Eb5-q": {"": 2, "C3-q": 2}, "D5-q": {"": 8, "R-e": 2, "D5-e": 2, "C5-q": 2, "E5-e": 2}, "\\e": {"": 0, "C3-q": 1, "C5-q": 1}, "R-h": {"": 2, "\\s": 1, "R-q": 1}, "F5-q": {"": 2, "C5-e": 2}, "B4-e": {"": 2, "R-e": 1, "R-q": 1}, "A4-e": {"": 6, "R-e": 2, "C5-e": 4}}

# mario
bigram = {"E5": {"": 14, "\\s": 1, "E5": 1, "R": 3, "C5": 1, "G4": 2, "C4": 4, "G3": 2}, "\\s": {"": 2}, "R": {"": 22, "E5": 4, "G5": 3, "G4": 3, "C5": 4, "E4": 2, "B4": 2, "Eb5": 2, "D5": 2}, "C5": {"": 16, "R": 5, "E5": 2, "A5": 8, "A4": 1}, "G5": {"": 11, "E5": 3, "F5": 2, "C3": 6}, "G4": {"": 5, "R": 3, "A4": 2}, "E4": {"": 3, "R": 2, "C4": 1}, "A4": {"": 5, "R": 2, "Bb4": 2, "C3": 1}, "B4": {"": 4, "A4": 2, "D5": 2}, "Bb4": {"": 2, "B4": 2}, "A5": {"": 10, "G5": 2, "G#5": 4, "C4": 4}, "F5": {"": 8, "A5": 2, "F#5": 6}, "D5": {"": 8, "C5": 6, "R": 2}, "C3": {"": 11, "R": 1, "D5": 4, "G3": 4, "C3": 1, "F4": 1}, "F#5": {"": 6, "G5": 6}, "D#5": {"": 6, "F5": 6}, "C4": {"": 9, "D#5": 4, "C5": 4, "\\s": 1}, "F3": {"": 4, "E5": 4}, "G#5": {"": 4, "F3": 4}, "G3": {"": 8, "D#5": 2, "C6": 2, "R": 2, "G3": 2}, "C6": {"": 6, "R": 2, "C6": 4}, "Eb5": {"": 2, "C3": 2}, "\\e": {"": 0, "C3": 1, "E3": 1}, "F4": {"": 1, "E4": 1}, "E3": {"": 1, "C5": 1}}

# mario + br
# bigram = {"E5": {"": 46, "\\s": 1, "E5": 13, "R": 5, "C5": 1, "G4": 2, "C4": 4, "G3": 2, "D5": 4, "F5": 8, "A4": 6}, "\\s": {"": 2}, "R": {"": 38, "E5": 8, "G5": 3, "G4": 3, "C5": 6, "E4": 2, "B4": 2, "Eb5": 2, "D5": 4, "\\s": 1, "F5": 2, "R": 5}, "C5": {"": 31, "R": 9, "E5": 4, "A5": 8, "B4": 2, "D5": 2, "C5": 2, "A4": 4}, "G5": {"": 11, "E5": 3, "F5": 2, "C3": 6}, "G4": {"": 5, "R": 3, "A4": 2}, "E4": {"": 2, "R": 2}, "A4": {"": 20, "R": 5, "Bb4": 2, "A4": 6, "E5": 2, "C5": 5}, "B4": {"": 6, "A4": 2, "D5": 2, "R": 2}, "Bb4": {"": 2, "B4": 2}, "A5": {"": 10, "G5": 2, "G#5": 4, "C4": 4}, "F5": {"": 18, "A5": 2, "F#5": 6, "C5": 2, "E5": 8}, "D5": {"": 18, "C5": 10, "R": 2, "E5": 4, "D5": 2}, "C3": {"": 10, "R": 1, "D5": 4, "G3": 4, "C3": 1}, "F#5": {"": 6, "G5": 6}, "D#5": {"": 6, "F5": 6}, "C4": {"": 8, "D#5": 4, "C5": 4}, "F3": {"": 4, "E5": 4}, "G#5": {"": 4, "F3": 4}, "G3": {"": 8, "D#5": 2, "C6": 2, "R": 2, "G3": 2}, "C6": {"": 6, "R": 2, "C6": 4}, "Eb5": {"": 2, "C3": 2}, "\\e": {"": 0, "C3": 1, "C5": 1}}

freqs = {
    "R": 0,
    "B#": 16.3516015625,
    "C": 16.3516015625,
    "C#": 17.32390625,
    "Db": 17.32390625,
    "D": 18.3540234375,
    "D#": 19.4454296875,
    "Eb": 19.4454296875,
    "E": 20.60171875,
    "E#": 21.8267578125,
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

durations = {
    "s": 1/16,
    "e": 1/8,
    "q": 1/4,
    "h": 1/2,
    "w": 1
}

Keys = {
    'C': ['C', 'D', 'E', 'F', 'G', 'A', 'B'],
    'Am': ['C', 'D', 'E', 'F', 'G', 'A', 'B'],

    'G': ['C', 'D', 'E', 'G', 'A', 'B', 'F#'],
    'Em': ['C', 'D', 'E', 'G', 'A', 'B', 'F#'],
    'D': ['D', 'E', 'G', 'A', 'B', 'F#', 'C#'],
    'Bm': ['D', 'E', 'G', 'A', 'B', 'F#', 'C#'],
    'A': ['D', 'E', 'A', 'B', 'F#', 'C#', 'G#'],
    'F#m': ['D', 'E', 'A', 'B', 'F#', 'C#', 'G#'],
    'E': ['E', 'A', 'B', 'F#', 'C#', 'G#', 'D#'],
    'C#m': ['E', 'A', 'B', 'F#', 'C#', 'G#', 'D#'],
    'B': ['E', 'B', 'F#', 'C#', 'G#', 'D#', 'A#'],
    'G#m': ['E', 'B', 'F#', 'C#', 'G#', 'D#', 'A#'],
    'F#': ['B', 'F#', 'C#', 'G#', 'D#', 'A#', 'E#'],
    'D#m': ['B', 'F#', 'C#', 'G#', 'D#', 'A#', 'E#'],
    'C#': ['F#', 'C#', 'G#', 'D#', 'A#', 'E#', 'B#'],
    'A#m': ['F#', 'C#', 'G#', 'D#', 'A#', 'E#', 'B#'],

    'F': ['C', 'D', 'E', 'F', 'G', 'A', 'Bb'],
    'Dm': ['C', 'D', 'E', 'F', 'G', 'A', 'Bb'],
    'Bb': ['C', 'D', 'F', 'G', 'A', 'Bb', 'Eb'],
    'Gm': ['C', 'D', 'F', 'G', 'A', 'Bb', 'Eb'],
    'Eb': ['C', 'D', 'F', 'G', 'Bb', 'Eb', 'Ab'],
    'Cm': ['C', 'D', 'F', 'G', 'Bb', 'Eb', 'Ab'],
    'Ab': ['C', 'F', 'G', 'Bb', 'Eb', 'Ab', 'Db'],
    'Fm': ['C', 'F', 'G', 'Bb', 'Eb', 'Ab', 'Db'],
    'Db': ['C', 'F', 'Bb', 'Eb', 'Ab', 'Db', 'Gb'],
    'Bbm': ['C', 'F', 'Bb', 'Eb', 'Ab', 'Db', 'Gb'],
    'Gb': ['F', 'Bb', 'Eb', 'Ab', 'Db', 'Gb', 'Cb'],
    'Ebm': ['F', 'Bb', 'Eb', 'Ab', 'Db', 'Gb', 'Cb'],
    'Cb': ['Bb', 'Eb', 'Ab', 'Db', 'Gb', 'Cb', 'Fb'],
    'Abm': ['Bb', 'Eb', 'Ab', 'Db', 'Gb', 'Cb', 'Fb'],
}

pitch_map = {
    'C': 0,
    'D': 1,
    'E': 2,
    'F': 3,
    'G': 4,
    'A': 5,
    'B': 6
}

chords = {
    "Cmaj": ["C4", "E4", "G4"],
    "Cmaj7": ["C4", "E4", "G4", "B4"],
    "Dmin": ["D4", "F4", "A4"],
    "Dmin7": ["D4", "F4", "A4", "C5"],
    "Emin": ["E4", "G4", "B4"],
    "Emin7": ["E4", "G4", "B4", "D5"],
    "Fmaj": ["F4", "A4", "C5"],
    "Fmaj7": ["F4", "A4", "C5", "E5"],
    "Gmaj": ["G4", "B4", "D5"],
    "Gmaj7": ["G4", "B4", "D5", "F5"],
    "Amin": ["A4", "C5", "E5"],
    "Amin7": ["A4", "C5", "E5", "G5"],
    "Bdim": ["B4", "D5", "F5"],
    "Bmin7b5": ["B4", "D5", "F5", "A5"]
}

CMajCh = ["Cmaj", 
           "Dmin", 
           "Emin", 
           "Fmaj", 
           "Gmaj", 
           "Amin", 
           "Bdim", 
           ["C5", "E5", "G5"]]

CMaj7Ch = ["Cmaj7", 
           "Dmin7", 
           "Emin7", 
           "Fmaj7", 
           "Gmaj7", 
           "Amin7", 
           "Bmin7b5", 
           ["C5", "E5", "G5", "B5"]]

CMajSc = [["C4"],
          ["D4"],
          ["E4"],
          ["F4"],
          ["G4"],
          ["A4"],
          ["B4"],
          ["C5"]]

As = [["A0"],
       ["A1"],
       ["A2"],
       ["A3"],
       ["A4"],
       ["A5"],
       ["A6"],
       ["A7"],
       ["A8"]]

loverBoy = [["C4", "E4", "G4", "B4", "w"], ["C4", "E4", "G4", "C5", "w"], ["C4", "E4", "G4", "B4", "w"], ["C4", "E4", "G4", "C5", "w"],
       ["F4", "A4", "C5", "w"], ["F4", "A4", "D5", "w"], ["F4", "A4", "E5", "w"], ["F4", "A4", "D5", "w"]]
gen_loverBoy = [['C4', 'E4', 'G4', 'B4', 'w'], ['C4', 'E4', 'G4', 'C5', 'w'], ['C4', 'E4', 'G4', 'B4', 'w'], ['C4', 'E4', 'G4', 'C5', 'w'], ['F4', 'A4', 'C5', 'w'], ['F4', 'A4', 'D5', 'w'], ['F4', 'A4', 'E5', 'w'], ['F4', 'A4', 'D5', 'w']]

mario = [["E5", "D3", "e"], 
         ["E5", "D3", "e"], "R-e", 
         ["E5", "D3", "e"], "R-e", 
         ["C5", "D3", "e"], 
         ["E5", "D3", "q"], 
         ["G5", "G3", "q"], "R-q", 
         ["G4", "G2", "q"], "R-q",
         
         ["C5", "G3", "q"], "R-e", ["G4", "E3", "q"], "R-e", ["E4", "C3", "q"],
         "R-e", ["A4", "F3", "q"], ["B4", "G3", "q"], ["Bb4", "G3", "e"], ["A4", "F3", "q"],
         ["G4", "E3", "e"], ["E5", "C4", "q"], ["G5", "E4", "e"], ["A5", "F4", "q"], ["F5", "D4", "e"], ["G5", "E4", "e"],
         "R-e", ["E5", "C4", "q"], ["C5", "A3", "e"], ["D5", "B3", "e"], ["B4", "G3", "q"], "R-e",

         ["C5", "G3", "q"], "R-e", ["G4", "E3", "q"], "R-e", ["E4", "C3", "q"],
         "R-e", ["A4", "F3", "q"], ["B4", "G3", "q"], ["Bb4", "G3", "e"], ["A4", "F3", "q"],
         ["G4", "E3", "e"], ["E5", "C4", "q"], ["G5", "E4", "e"], ["A5", "F4", "q"], ["F5", "D4", "e"], ["G5", "E4", "e"],
         "R-e", ["E5", "C4", "q"], ["C5", "A3", "e"], ["D5", "B3", "e"], ["B4", "G3", "q"], "R-e",
         
         "C3-q", "G5-e", ["F#5", "G3", "e"], "F5-e", "D#5-e", "C4-e", "E5-e",
         "F3-e", "G#5-e", "A5-e", ["C5", "C4", "e"], "C4-e", "A5-e", ["C5", "F3", "e"], "D5-e",
         "C3-q", "G5-e", ["F#5", "G3", "e"], "F5-e", "D#5-e", "G3-e", ["E5", "C4", "e"],
         "R-e", ["C6", "q"], ["C6", "G4", "e"], ["C6", "G4", "q"], "G3-q",
         
         "C3-q", "G5-e", ["F#5", "G3", "e"], "F5-e", "D#5-e", "C4-e", "E5-e",
         "F3-e", "G#5-e", "A5-e", ["C5", "C4", "e"], "C4-e", "A5-e", ["C5", "F3", "e"], "D5-e",
         "C3-q", ["Eb5", "Ab3", "q"], "R-e", ["D5", "Bb3", "q"], "R-e",
         ["C5", "C4", "q"], "R-e", "G3-e", "G3-q", "C3-q",

         "C3-q", "G5-e", ["F#5", "G3", "e"], "F5-e", "D#5-e", "C4-e", "E5-e",
         "F3-e", "G#5-e", "A5-e", ["C5", "C4", "e"], "C4-e", "A5-e", ["C5", "F3", "e"], "D5-e",
         "C3-q", "G5-e", ["F#5", "G3", "e"], "F5-e", "D#5-e", "G3-e", ["E5", "C4", "e"],
         "R-e", ["C6", "q"], ["C6", "G4", "e"], ["C6", "G4", "q"], "G3-q",
         
         "C3-q", "G5-e", ["F#5", "G3", "e"], "F5-e", "D#5-e", "C4-e", "E5-e",
         "F3-e", "G#5-e", "A5-e", ["C5", "C4", "e"], "C4-e", "A5-e", ["C5", "F3", "e"], "D5-e",
         "C3-q", ["Eb5", "Ab3", "q"], "R-e", ["D5", "Bb3", "q"], "R-e",
         ["C5", "C4", "q"], "R-e", "G3-e", "G3-q", "C3-q"]
simp_mario = ["E5-e", "E5-e", "R-e", "E5-e", "R-e", "C5-e", "E5-q", 
         "G5-q", "R-q", "G4-q", "R-q",
         
         "C5-q", "R-e", "G4-q", "R-e", "E4-q",
         "R-e", "A4-q", "B4-q", "Bb4-e", "A4-q",
         "G4-e", "E5-q", "G5-e", "A5-q", "F5-e", "G5-e",
         "R-e", "E5-q", "C5-e", "D5-e", "B4-q", "R-e",

         "C5-q", "R-e", "G4-q", "R-e", "E4-q",
         "R-e", "A4-q", "B4-q", "Bb4-e", "A4-q",
         "G4-e", "E5-q", "G5-e", "A5-q", "F5-e", "G5-e",
         "R-e", "E5-q", "C5-e", "D5-e", "B4-q", "R-e",
         
         "C3-q", "G5-e", "F#5-e", "F5-e", "D#5-e", "C4-e", "E5-e",
         "F3-e", "G#5-e", "A5-e", "C5-e", "C4-e", "A5-e", "C5-e", "D5-e",
         "C3-q", "G5-e", "F#5-e", "F5-e", "D#5-e", "G3-e", "E5-e",
         "R-e", "C6-q", "C6-e", "C6-q", "G3-q",
         
         "C3-q", "G5-e", "F#5-e", "F5-e", "D#5-e", "C4-e", "E5-e",
         "F3-e", "G#5-e", "A5-e", "C5-e", "C4-e", "A5-e", "C5-e", "D5-e",
         "C3-q", "Eb5-q", "R-e", "D5-q", "R-e",
         "C5-q", "R-e", "G3-e", "G3-q", "C3-q",

         "C3-q", "G5-e", "F#5-e", "F5-e", "D#5-e", "C4-e", "E5-e",
         "F3-e", "G#5-e", "A5-e", "C5-e", "C4-e", "A5-e", "C5-e", "D5-e",
         "C3-q", "G5-e", "F#5-e", "F5-e", "D#5-e", "G3-e", "E5-e",
         "R-e", "C6-q", "C6-e", "C6-q", "G3-q",
         
         "C3-q", "G5-e", "F#5-e", "F5-e", "D#5-e", "C4-e", "E5-e",
         "F3-e", "G#5-e", "A5-e", "C5-e", "C4-e", "A5-e", "C5-e", "D5-e",
         "C3-q", "Eb5-q", "R-e", "D5-q", "R-e",
         "C5-q", "R-e", "G3-e", "G3-q", "C3-q"]
gen_mario = [['E5', 'D3', 'e'], ['E5', 'D3', 'e'], ['E5', 'D3', 'e'], ['E5', 'D3', 'e'], ['E5', 'D3', 'e'], 'R-e', ['E4', 'C3', 'q'], 'R-e', ['E4', 'C3', 'q'], 'R-e', ['C5', 'G3', 'q'], 'R-e', ['E5', 'C4', 'q'], ['C5', 'A3', 'e'], ['D5', 'B3', 'e'], ['B4', 'G3', 'q'], 'R-e', ['E5', 'C4', 'q'], ['G5', 'E4', 'e'], ['A5', 'F4', 'q'], ['F5', 'D4', 'e'], ['G5', 'E4', 'e'], 'R-e', ['E4', 'C3', 'q'], 'R-e', ['C5', 'D3', 'e'], ['E5', 'D3', 'q'], ['G5', 'G3', 'q'], 'R-q', ['G4', 'G2', 'q'], 'R-q', ['C5', 'G3', 'q'], 'R-e', ['E5', 'C4', 'q'], ['G5', 'E4', 'e'], 'R-e', ['C6', 'q'], ['C6', 'G4', 'e'], ['C6', 'G4', 'q'], 'G3-q', 'C3-q', ['Eb5', 'Ab3', 'q'], 'R-e', ['C6', 'q'], ['C6', 'G4', 'e'], ['C6', 'G4', 'q'], 'G3-q', 'C3-q', 'G5-e', ['F#5', 'G3', 'e'], 'F5-e', 'D#5-e', 'C4-e', 'A5-e', ['C5', 'C4', 'e'], 'C4-e', 'E5-e', 'F3-e', 'G#5-e', 'A5-e', ['C5', 'F3', 'e'], 'D5-e', 'C3-q', 'G5-e', ['F#5', 'G3', 'e'], 'F5-e', 'D#5-e', 'C4-e', 'A5-e', ['C5', 'C4', 'e'], 'C4-e', 'A5-e', ['C5', 'F3', 'e'], 'D5-e', 'C3-q', ['Eb5', 'Ab3', 'q'], 'R-e', ['C5', 'G3', 'q'], 'R-e', ['D5', 'Bb3', 'q'], 'R-e', ['D5', 'Bb3', 'q'], 'R-e', ['C5', 'C4', 'q'], 'R-e', ['E5', 'D3', 'e'], 'R-e', ['D5', 'Bb3', 'q'], 'R-e', ['C5', 'C4', 'q'], 'R-e', ['C6', 'q'], ['C6', 'G4', 'e'], ['C6', 'G4', 'q'], 'G3-q', 'C3-q', 'G5-e', ['F#5', 'G3', 'e'], 'F5-e', 'D#5-e', 'C4-e', 'E5-e', 'F3-e', 'G#5-e', 'A5-e', ['C5', 'F3', 'e'], 'D5-e', 'C3-q', 'G5-e', ['F#5', 'G3', 'e'], 'F5-e', 'D#5-e', 'G3-e', 'G3-q', 'C3-q', 'C3-q', 'G5-e', ['F#5', 'G3', 'e'], 'F5-e', 'D#5-e', 'G3-e', ['E5', 'C4', 'e'], 'R-e', ['C6', 'q'], ['C6', 'G4', 'e'], ['C6', 'G4', 'q'], 'G3-q', 'C3-q']

bad_rom = ["R-h", "C5-e", "D5-e", "E5-e", "C5-e",
           "F5-q", "R-e", "E5-e", "F5-e", "E5-e", "D5-e", "D5-q",
           "R-e", "R-e", "B4-e", "C5-q", "D5-q",
           "E5-q", "E5-e", "E5-e", "E5-e", "D5-q", "C5-q",

           "R-q", "R-e", "C5-e", "D5-e", "E5-e", "C5-e",
           "F5-q", "R-e", "E5-e", "F5-e", "E5-e", "D5-e", "D5-q",
           "R-q", "B4-e", "C5-q", "D5-q",
           "E5-q", "E5-e", "E5-e", "E5-e", "D5-q", "C5-q",
           
           "R-e", "R-e", "R-q", "R-h",

           "A4-q", "A4-q", "E5-e", "E5-e", "F5-e", "E5-e",
           "R-e", "A4-e", "A4-q", "E5-e", "E5-e", "F5-e", "E5-e",
           "A4-q", "A4-q", "E5-e", "E5-e", "F5-e", "E5-e",
           "R-e", "C5-e", "C5-e", "A4-e", "C5-e", "A4-e", "C5-q",
           
           "A4-q", "A4-q", "E5-e", "E5-e", "F5-e", "E5-e",
           "R-e", "A4-e", "A4-q", "E5-e", "E5-e", "F5-e", "E5-e",
           "A4-q", "A4-q", "E5-e", "E5-e", "F5-e", "E5-e",
           "R-e", "C5-e", "C5-e", "A4-e", "C5-e", "A4-e", "C5-q",]

gen_mix = ['R-h', 'C5-e', 'D5-e', 'D5-q', 'C5-q', 'R-e', 'E5-e', 'R-e', 'C5-e', 'C4-e', 'E5-e', 'D5-q', 'R-e', 'E5-q', 'G5-q', 'R-q', 'R-e', 'D5-q', 'R-q', 'R-e', 'C5-q', 'R-q', 'R-e', 'C5-q', 'R-e', 'G4-q', 'R-e', 'A4-e', 'C5-e', 'D5-e', 'C3-q', 'C3-q', 'G5-e', 'F#5-e', 'F5-e', 'E5-e', 'F5-e', 'D#5-e', 'G3-e', 'G3-q', 'C3-q', 'G5-e', 'A5-q', 'F5-e', 'E5-e', 'E5-e', 'R-e', 'C5-q', 'R-e', 'C5-q']

gen_dist = ['G3-q', 'G3-q', 'D3-h', 'D3-q', 'F3-q', 'G3-q', 'A3-h', 'G3-h', 'C3-e', 'D3-q', 'C3-e', 'D3-e', 'F3-q', 'F3-q', 'F3-e', 'E3-e', 'F3-q', 'F3-q', 'G3-e', 'G3-q', 'E3-h', 'E3-h', 'E3-q', 'D3-h', 'D3-e']

def seq_to_freq(seq, duration):
    """
    Converts a sequence of notes to frequencies.
    """
    fs = []
    durs = []
    for i in range(len(seq)):
        notes = seq[i][:-1] if type(seq[i]) == list else (chords[seq[i]] if seq[i] in chords else [seq[i]])
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
    return fs, durs

def gen_samples(fs, durs, volume, sample_rate):
    """
    Generates the samples for each signal that will be played.
    """
    samples = []
    vol_scl = 1/len(fs)
    for i in range(len(fs)):
        samples.append([])
        samples[i] = (np.sin(2*np.pi*np.arange(sample_rate*durs[i])*fs[i][0]/sample_rate)).astype(np.float32)
        vol = volume - vol_scl * i
        for f in fs[i][1:]:
            samples[i] += (vol*np.sin(2*np.pi*np.arange(sample_rate*durs[i])*f/sample_rate)).astype(np.float32)
        samples[i] = (samples[i]).tobytes()
    return samples

def play_seq(seq, duration, volume=1, sample_rate=44100):
    """
    Plays a given sequence through the speakers.
    """
    fs, durs = seq_to_freq(seq, duration)
    samples = gen_samples(fs, durs, volume, sample_rate)

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

def dist(note1, note2):
    """
    Computes the squared "distance" between two notes.
    """
    if note1[-2] == '-': note1 = note1[:-2]
    if note2[-2] == '-': note2 = note2[:-2]
    pitch1, pitch2 = note1[0], note2[0]
    oct1, oct2 = int(note1[-1]), int(note2[-1])

    oct_dist = 8*abs(oct2-oct1)
    pitch_dist = abs(pitch_map[pitch2]-pitch_map[pitch1])
    if pitch1 == pitch2:
        return oct_dist
    elif oct1 == oct2:
        return pitch_dist
    else:
        return (oct_dist+pitch_dist)

def generate_dist(prev, curr_key, octaves, distance):
    """
    Generates a new note such that closer notes are weighted higher
    """
    all_notes = []
    pr = []
    for pitch in Keys[curr_key]:
        for octave in octaves:
            note = pitch+str(octave)
            all_notes.append(note)
            if prev != '\s':
                pr.append(float(dist(prev, note)))
    
    if prev != '\s':
        pr = np.array(pr)
        pr = (np.max(pr)+1-pr)**distance
        pr /= np.sum(pr)
        return np.random.choice(all_notes, p=pr) 
    else:
        return np.random.choice(all_notes)

def generate_pitch(curr_key):
    """
    Generates a random new pitch (A, B, C, etc.)
    """
    return np.random.choice(Keys[curr_key])

def generate_oct(octaves):
    """
    Generates a random new octave (0, 1, 2, etc.)
    """
    return np.random.choice(octaves)

def generate_type(types):
    """
    Generates a random new note type ('e', 'q', 'h', etc.)
    """
    return np.random.choice(types[0], p=types[1])

def generate_note(prev, curr_key, keys, octaves, types, mode, train_spd=False, distance=0):
    """
    Generates a random new note
    """
    if mode == "bigram":
        model = bigram_spd
        if not train_spd:
            if len(prev) > 1 and prev[-2] == '-': prev = prev[:-2]
            model = bigram

        if prev not in model:
            raise ValueError("Starting note not in bigram")

        prs = []
        elems = []
        for curr in model:
            if prev in model[curr]:
                prs.append(model[curr][prev]/model[prev][""])
                e = curr if train_spd or curr == '\e' else curr+"-"+generate_type(types)
                elems.append(e)
        prs = np.array(prs)
        return np.random.choice(elems, p=prs), curr_key
    elif mode == "constraint":
        # Currently uniform over pitch, octave
        if len(keys) > 1 and np.random.random()*50 < 1:
            print('switching keys from', curr_key+"...")
            choice = curr_key
            while choice == curr_key:
                choice = np.random.choice(keys)
            curr_key = choice
            print("...to", curr_key, "after", prev)

        if distance == 0:
            pitch = generate_pitch(curr_key)
            oct = generate_oct(octaves)
            note = pitch+str(oct)
        else:
            note = generate_dist(prev, curr_key, octaves, distance)
        l = generate_type(types)
        return note+"-"+l, curr_key
    return

def generate_seq(num_notes, keys, octaves, speeds, mode, start, train_spd, distance):
    out = []
    prev = start
    if prev != '\\s':
        out.append(prev)
        num_notes-=1
    curr_key = keys[0]

    if mode == "bigram":
        i = 0
        while prev != '\\e' and i < num_notes:
            prev, curr_key = generate_note(prev, curr_key, keys, octaves, speeds, mode, train_spd)
            if prev[0] == '[':
                out.append(prev[2:-2].split("', '"))
            else:
                out.append(prev)
            i += 1
        if out[-1] == '\\e': out = out[:-1]
    elif mode == "constraint":
        for _ in range(num_notes):
            prev, curr_key = generate_note(prev, curr_key, keys, octaves, speeds, mode, distance=distance)
            out.append(prev)

    print(len(out))
    return out

bpm = 180 #240 #180 #120
duration = 60/bpm*4  # in seconds, may be float
seq = ['C4-e', 'E5-e', 'F3-e', 'G#5-e', 'A5-e', ['C5', 'C4', 'e'], 'C4-e', 'A5-e', ['C5', 'C4', 'e'], 'C4-e', 'E5-e', 'F3-e', 'G#5-e', 'A5-e', ['C5', 'F3', 'e'], 'D5-e', 'C3-q', 'G5-e', ['F#5', 'G3', 'e'], 'F5-e', 'D#5-e', 'C4-e', 'E5-e', 'F3-e', 'G#5-e', 'A5-e', ['C5', 'F3', 'e'], 'D5-e', 'C3-q', 'C3-q', 'G5-e', ['F#5', 'G3', 'e'], 'F5-e', 'D#5-e', 'C4-e', 'E4-e', ['F4', 'F2', 'q'], 'C3-e', 'A4-e', ['C5', 'A2', 'q'], 'E3-q']

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Run Sound Signal Synthesizer.')
    parser.add_argument('--mode', type=str, choices=['bigram', 'constraint'], default='bigram', help='Mode(l) of note generation.')
    parser.add_argument('--start', type=str, default='\s', help='Note for the sequence to start with.')
    parser.add_argument('--num_notes', type=int, default=25, help='Maximum number of notes to generate.')

    parser.add_argument('--train_speed', action='store_true', default=False, help='Whether the bigram is trained to differentiate between note lengths. [BIGRAM ONLY]')
    parser.add_argument('--speed', type=str, choices=['uniform', 'normal', 'faster-lin', 'faster-exp', 'slower-lin', 'slower-exp'], default='normal', help='Whether the song trends faster, slower, or normal. [DOES NOT APPLY TO BIGRAM TRAINED ON SPEED]')
    parser.add_argument('--distance', type=int, default=0, help='To what extent the model takes into account distance between notes. [CONSTRAINT ONLY]')
    args = parser.parse_args()

    keys = ["C"]
    octs = [3, 4, 5]

    types = [["e", "q", "h"], [1/3, 1/3, 1/3]]
    if args.speed == 'faster-lin':
        types[1] = [3/6, 2/6, 1/6]
    elif args.speed == 'faster-exp':
        types[1] = [1/2+1/8, 1/4, 1/8]
    elif args.speed == 'slower-lin':
        types[1] = [1/6, 2/6, 3/6]
    elif args.speed == 'slower-exp':
        types[1] = [1/8, 1/4, 1/2+1/8]

    # types = [["s", "e", "q", "h"], [0.25, 0.25, 0.25, 0.25]]
    # if args.speed == 'faster-lin':
    #     types[1] = [4/10, 3/10, 2/10, 1/10]
    # elif args.speed == 'faster-exp':
    #     types[1] = [1/2+1/16, 1/4, 1/8, 1/16]
    # elif args.speed == 'slower-lin':
    #     types[1] = [1/10, 2/10, 3/10, 4/10]
    # elif args.speed == 'slower-exp':
    #     types[1] = [1/16, 1/8, 1/4, 1/2+1/16]

    sequence = generate_seq(args.num_notes, keys, octs, types, args.mode, args.start, args.train_speed, args.distance)
    print(sequence)

    # python3 main.py --mode bigram --train_speed
    # bpm = 180 #240 #180 #120
    # duration = 60/bpm*4
    # play_seq(sequence, duration) # Demo 1

    # ['G3-q', 'A3-h', 'D3-h', 'F3-h', 'G4-e', 'A4-h', 'D4-h', 'F4-h', 'F4-e', 'G4-h', 'G4-e', 'A4-h', 'F4-h', 'E4-q', 'E4-q', 'E4-e', 'C4-e', 'C4-e', 'E4-e', 'F4-q', 'D4-q', 'A4-e', 'G4-q', 'A4-q', 'E4-q']

    # bpm = 120 #240 #180 #120
    # duration = 60/bpm*4
    # play_seq(gen_mix, duration) # Demo 2

    # python3 main.py --mode constraint
    # python3 main.py --mode constraint --distance 5
    bpm = 180 #240 #180 #120
    duration = 60/bpm*4
    # play_seq(sequence, duration) # Demo 3, 4

    # play_seq(gen_dist, duration) # Demo 5
    play_seq(gen_mario, duration) # Demo 6
