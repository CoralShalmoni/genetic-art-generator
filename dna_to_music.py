from midiutil import MIDIFile
import sys
import subprocess
import os

BASE_NOTES = {
    'A': 60,  # C4
    'C': 62,  # D4
    'T': 64,  # E4
    'G': 65,  # F4
    'N': 67,  # G4 — padding note
}

def play_file(filepath):
    if sys.platform.startswith('darwin'):  # macOS
        subprocess.call(['open', filepath])
    elif sys.platform.startswith('win'):   # Windows
        os.startfile(filepath)
    elif sys.platform.startswith('linux'): # Linux
        subprocess.call(['xdg-open', filepath])
    else:
        print(f"Cannot open files automatically on OS: {sys.platform}")

def sequence_to_midi(sequence, save_path="assets/music/output.mid", tempo=120):
    midi = MIDIFile(1)
    track = 0
    time = 0
    midi.addTrackName(track, time, "DNA Melody")
    midi.addTempo(track, time, tempo)

    channel = 0
    volume = 100
    duration = 1

    for base in sequence:
        note = BASE_NOTES.get(base)
        if note:
            midi.addNote(track, channel, note, time, duration, volume)
        time += 1

    with open(save_path, "wb") as output_file:
        midi.writeFile(output_file)

    abs_path = os.path.abspath(save_path)
    print(f"MIDI saved to {abs_path}")
    play_file(abs_path)
