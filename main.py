import sys
from utils import load_dna_from_file, get_clean_sequences
from dna_to_pixel import sequence_to_image
from dna_to_music import sequence_to_midi

def main():
    # Get input filepath from command line or use default
    if len(sys.argv) > 1:
        filepath = sys.argv[1]
    else:
        filepath = "assets/sequences/example_sequence.txt"

    raw_dna = load_dna_from_file(filepath)
    if not raw_dna:
        print("No DNA sequence loaded. Exiting.")
        return

    clean_seqs = get_clean_sequences(raw_dna)
    if not clean_seqs:
        print("No clean DNA sequences found. Exiting.")
        return

    # Use the first clean sequence, trimmed/padded to 256 bases
    PAD_BASE = 'N'
    sequence = clean_seqs[0][:256].ljust(256, PAD_BASE)


    # Generate pixel art
    sequence_to_image(sequence)

    #Generate music
    sequence_to_midi(sequence)


if __name__ == "__main__":
    main()
