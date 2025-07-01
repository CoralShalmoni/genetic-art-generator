from flask import Flask, request, render_template, send_from_directory
import os
from utils import get_clean_sequences
from dna_to_pixel import sequence_to_image
from dna_to_music import sequence_to_midi

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
PIXEL_ART_FOLDER = 'assets/pixel_art'
MUSIC_FOLDER = 'assets/music'

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(PIXEL_ART_FOLDER, exist_ok=True)
os.makedirs(MUSIC_FOLDER, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    paired_results = []

    if request.method == 'POST':
        # Load DNA sequence from uploaded file or textarea
        if 'dna_file' in request.files and request.files['dna_file'].filename != '':
            file = request.files['dna_file']
            filepath = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(filepath)
            with open(filepath, 'r') as f:
                raw_dna = f.read()
        else:
            raw_dna = request.form.get('dna_text', '')

        # Get colors from form (with defaults)
        color_map = {
            'A': request.form.get('color_A', '#ff0000'),
            'C': request.form.get('color_C', '#00ff00'),
            'T': request.form.get('color_T', '#0000ff'),
            'G': request.form.get('color_G', '#ffff00'),
            'N': request.form.get('color_N', '#cccccc'),
        }

        # Get tempo from form, default 120 BPM
        tempo = int(request.form.get('tempo', 120))

        clean_seqs = get_clean_sequences(raw_dna)
        all_seq = ''.join(clean_seqs)

        chunk_size = 256
        max_chunks = 10

        for i in range(0, min(len(all_seq), chunk_size * max_chunks), chunk_size):
            chunk = all_seq[i:i+chunk_size].ljust(chunk_size, 'N')

            image_name = f"output_{i//chunk_size}.png"
            midi_name = f"output_{i//chunk_size}.mid"

            image_path = os.path.join(PIXEL_ART_FOLDER, image_name)
            midi_path = os.path.join(MUSIC_FOLDER, midi_name)

            sequence_to_image(chunk, save_path=image_path, color_map=color_map)
            sequence_to_midi(chunk, save_path=midi_path, tempo=tempo)

            start_base = i + 1
            end_base = start_base + chunk_size - 1

            paired_results.append({
                'img': image_name,
                'midi': midi_name,
                'chunk_index': (i // chunk_size) + 1,
                'start_base': start_base,
                'end_base': end_base,
                'sequence': chunk
            })

    return render_template('index.html', paired_results=paired_results)

@app.route('/pixel_art/<filename>')
def pixel_art(filename):
    return send_from_directory(PIXEL_ART_FOLDER, filename)

@app.route('/music/<filename>')
def music(filename):
    return send_from_directory(MUSIC_FOLDER, filename)

if __name__ == '__main__':
    app.run(debug=True)
