from mido import Message, MidiFile, MidiTrack, MetaMessage

def sequence_to_midi(sequence, save_path='output.mid', tempo=120):
    midi = MidiFile()
    track = MidiTrack()
    midi.tracks.append(track)

    # Convert BPM to microseconds per beat for MIDI tempo meta message
    microseconds_per_beat = int(60_000_000 / tempo)
    track.append(MetaMessage('set_tempo', tempo=microseconds_per_beat))

    # Map DNA bases to MIDI note numbers (example)
    note_map = {'A': 60, 'C': 62, 'T': 64, 'G': 65, 'N': 67}  # middle C and others

    note_length = 480  # ticks per note (quarter note length)

    for base in sequence:
        note = note_map.get(base, 67)  # default to 67 if base unknown
        track.append(Message('note_on', note=note, velocity=64, time=0))
        track.append(Message('note_off', note=note, velocity=64, time=note_length))

    midi.save(save_path)
