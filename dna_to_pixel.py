from PIL import Image
import os

# Map bases to RGB colors
BASE_COLORS = {
    'A': (255, 0, 0),    # Red
    'C': (0, 255, 0),    # Green
    'T': (0, 0, 255),    # Blue
    'G': (255, 255, 0),  # Yellow
    'N': (192, 192, 192) # Light gray for padding
}


def sequence_to_image(sequence, image_size=(16,16), pixel_size=20, save_path="assets/pixel_art/output.png"):
    """
    Convert a DNA sequence to a pixel art image.

    Args:
        sequence (str): Clean DNA sequence (only A,C,T,G).
        image_size (tuple): (width, height) in pixels.
        pixel_size (int): Size of each pixel block.
        save_path (str): Where to save the image.
    """
    width, height = image_size
    img = Image.new('RGB', (width * pixel_size, height * pixel_size), color=(255,255,255))

    for i, base in enumerate(sequence):
        x = (i % width) * pixel_size
        y = (i // width) * pixel_size

        color = BASE_COLORS.get(base, (0,0,0))  # Default black if unknown base

        for px in range(pixel_size):
            for py in range(pixel_size):
                img.putpixel((x + px, y + py), color)

    abs_path = os.path.abspath(save_path)
    img.save(abs_path)
    print(f"Image saved to {abs_path}")
    img.show()


# Example usage
if __name__ == "__main__":
    test_sequence = "ACTG" * 64  # 256 bases
    sequence_to_image(test_sequence)
