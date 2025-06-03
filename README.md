# Genetic Art Generator 🎨🧬

**Genetic Art Generator** is a creative tool that transforms DNA sequences into both pixel art images and musical compositions. It maps biological data into engaging audiovisual representations, combining science and art in a novel way.

---

## 🧬 What does this project do?

This tool takes a DNA sequence and produces:

- A unique pixel art image where codons or nucleotides map to colors
- A MIDI music file where codons or amino acids correspond to musical notes

Both outputs visualize the genetic information in complementary formats.

---

## 📥 Input

The project accepts DNA sequences in:

- Plain `.txt` files containing raw sequences
- `.fasta` format files
- Direct command line input strings

Only valid nucleotide characters (`A`, `T`, `C`, `G`) are processed; all others are filtered out.

---

## 📤 Output

- A PNG image representing the DNA as pixel art, arranged in a customizable grid  
- A MIDI `.mid` file representing the DNA sequence as music, playable on any MIDI-compatible device or software

Both files are saved to the specified output locations.

---

## ⚙️ Technical Notes

- Written in **Python 3**  
- Utilizes libraries such as `Pillow` for image generation, `mido` for MIDI file creation, and `argparse` for command line arguments  
- Modular design with functions handling parsing, mapping codons to colors and notes, and file generation

---

## 🚀 Installation & Running

### Installation

```bash
git clone https://github.com/YOUR_USERNAME/genetic-art-generator
cd genetic-art-generator
pip install -r requirements.txt
```
### Running the Project

```bash
python genetic_art_generator.py --input dna.fasta --image_output art.png --music_output art.mid
```

## 🧪 Example

Input file (`example.fasta`):

```
>Example DNA
ATGCGATACGTTAGCAGGTTTGA
```

Outputs generated:

- `output/art.png` — 🎨 Pixel art visualization  
- `output/art.mid` — 🎵 MIDI music file representing the sequence

---

## 🙏 Acknowledgments

This project was developed as part of the Python programming course at Weizzman School of Science.🎓

---

