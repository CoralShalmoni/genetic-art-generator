from PIL import Image
import matplotlib.colors as mcolors
import math

def sequence_to_image(sequence, save_path='output.png', color_map=None):
    """
    Converts a DNA sequence into pixel art image with larger visible pixels.

    Args:
        sequence (str): DNA sequence (e.g. "ACTGNNN...")
        save_path (str): Path to save the PNG image
        color_map (dict): Map base to hex color string (e.g. '#ff0000')

    """

    if color_map is None:
        color_map = {
            'A': '#ff0000',  # red
            'C': '#00ff00',  # green
            'T': '#0000ff',  # blue
            'G': '#ffff00',  # yellow
            'N': '#cccccc'   # gray for padding
        }

    # Convert hex colors to RGB tuples (0-255)
    rgb_map = {}
    for base, hex_color in color_map.items():
        rgb = tuple(int(255 * c) for c in mcolors.to_rgb(hex_color))
        rgb_map[base] = rgb

    length = len(sequence)
    size = max(16, math.ceil(math.sqrt(length)))  # minimum 16x16 grid

    PIXEL_SIZE = 10  # pixels per base block
    img_size = size * PIXEL_SIZE

    img = Image.new('RGB', (img_size, img_size), color=(255, 255, 255))
    pixels = img.load()

    for i, base in enumerate(sequence):
        x = (i % size) * PIXEL_SIZE
        y = (i // size) * PIXEL_SIZE

        color = rgb_map.get(base, (0, 0, 0))

        for dx in range(PIXEL_SIZE):
            for dy in range(PIXEL_SIZE):
                pixels[x + dx, y + dy] = color

    img.save(save_path)
