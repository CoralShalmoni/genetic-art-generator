# Genetic Art Generator 🎨🧬

**Genetic Art Generator** is a creative tool that transforms DNA sequences into both pixel art images and musical compositions. It maps biological data into engaging audiovisual representations, combining science and art in a novel way.

---

## 🧬 What does this project do?

This tool takes a DNA sequence and produces:

- A unique pixel art image where nucleotides map to customizable colors  
- A MIDI music file where each base corresponds to a musical note  

Both outputs visualize genetic information in complementary formats, and are shown in pairs per DNA chunk.

---

## 📥 Input

The project accepts DNA sequences in:

- Plain `.txt` files containing raw sequences  
- `.fasta` format files  
- Direct input through the web interface (paste or upload)  

Only valid nucleotide characters (`A`, `T`, `C`, `G`) are processed. Sequences are cleaned, split into 256-base chunks, and padded with `N` if needed.

---

## 📤 Output

For each DNA chunk (up to 10):

- 🎨 A PNG image visualizing the sequence  
- 🎵 A MIDI file representing the sequence as music  

Results are saved in:

- `assets/pixel_art/`  
- `assets/music/`  

And displayed side-by-side on the web interface.

---

## ⚙️ Technical Notes

- Written in **Python 3.10+**  
- Built as a web app using **Flask**  
- Uses `Pillow` for pixel art  
- Uses `mido` + `python-rtmidi` for music  
- Color handling via `matplotlib`

**Folder structure:**

```
genetic-art-generator/
├── app.py
├── dna_to_pixel.py
├── dna_to_music.py
├── utils.py
├── requirements.txt
├── templates/
│   └── index.html
├── assets/
│   ├── pixel_art/
│   └── music/
├── uploads/
└── README.md
```

---

## 🚀 Installation & Running

### 1. Clone the project

```bash
git clone https://github.com/CoralShalmoni/genetic-art-generator.git
cd genetic-art-generator
```

### 2. (Optional) Create a virtual environment

```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the web app

```bash
python app.py
```

Then open your browser at [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🧪 Example

Example input (`example.fasta`):

```
>Example DNA
ATGCGATACGTTAGCAGGTTTGA
```

Results:

- `assets/pixel_art/` contains: `chunk_1_1-23.png`  
- `assets/music/` contains: `chunk_1_1-23.mid`  
- These are displayed in the app below a live preview of the sequence

---

## 🛠 Features

- Accepts `.txt`, `.fasta`, or pasted input  
- Filters invalid characters  
- Pads short sequences with `N`  
- Displays DNA, image, and music side-by-side  
- Lets you customize:
  - Colors for each base
  - Music tempo (BPM)

---

## 🙏 Acknowledgments

This project was developed as part of the Python programming course at Weizmann Institute of Science. 🎓 

---
