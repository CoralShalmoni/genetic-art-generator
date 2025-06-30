def get_clean_sequences(dna, valid_bases="ACTG"):
    """Split DNA string into clean sub-sequences containing only valid bases."""
    current = ""
    sequences = []

    for char in dna.upper():
        if char in valid_bases:
            current += char
        else:
            if current:
                sequences.append(current)
                current = ""
    if current:
        sequences.append(current)

    return sequences


def chunk_sequence(sequence, chunk_size):
    """Split a sequence string into chunks of fixed length."""
    return [sequence[i:i + chunk_size] for i in range(0, len(sequence), chunk_size)]


def load_dna_from_file(filepath):
    """Load raw DNA sequence from a text file, stripping whitespace and newlines."""
    try:
        with open(filepath, 'r') as file:
            dna = file.read()
        # Remove whitespace and newlines
        dna = ''.join(dna.split())
        return dna.upper()
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
        return None

if __name__ == "__main__":
    filepath = "assets/sequences/example_sequence.txt"
    raw_dna = load_dna_from_file(filepath)
    if raw_dna:
        clean_seqs = get_clean_sequences(raw_dna)
        print(f"Found {len(clean_seqs)} clean sequences:")
        for seq in clean_seqs:
            print(seq)
