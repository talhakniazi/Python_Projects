from rembg import remove
from PIL import Image
import os

def remove_background(input_path, output_path):
    """
    Removes the background from images and saves the output.

    :param input_path: Path to the input image or folder containing images
    :param output_path: Path to save the output image(s)
    """
    # Check if input is a single file or a folder
    if os.path.isfile(input_path):
        process_image(input_path, output_path)
    elif os.path.isdir(input_path):
        if not os.path.exists(output_path):
            os.makedirs(output_path)
        for filename in os.listdir(input_path):
            file_path = os.path.join(input_path, filename)
            if os.path.isfile(file_path):
                output_file = os.path.join(output_path, filename)
                process_image(file_path, output_file)
    else:
        print(f"Invalid input path: {input_path}")

def process_image(input_file, output_file):
    """
    Processes a single image to remove its background.

    :param input_file: Path to the input image
    :param output_file: Path to save the output image
    """
    try:
        with open(input_file, "rb") as file:
            input_image = file.read()
        output_image = remove(input_image)
        with open(output_file, "wb") as file:
            file.write(output_image)
        print(f"Background removed: {output_file}")
    except Exception as e:
        print(f"Failed to process {input_file}: {e}")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Remove background from images.")
    parser.add_argument("input", help="Path to the input image or folder")
    parser.add_argument("output", help="Path to save the output image or folder")
    args = parser.parse_args()

    remove_background(args.input, args.output)

    input("\nPress Enter to exit...")