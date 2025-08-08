"""
splitter.py
-----------
Half-frame Film Scanner Splitter

This script contains the core logic for splitting half-frame film scans
into individual PNGs. It is designed to be run through main.py, which
handles dependency installation and restarts if needed.

Assumptions:
- Input images may be any common format (.jpg, .jpeg, .png, .tif, .bmp, .webp).
- A vertical "split" exists between the two halves, centered horizontally,
  and never more than 1/10 of the total image width.
- All processing is done on lossless PNG data.
- Output is always uncompressed .png files.

Author: [Your Name]
"""

import cv2
import numpy as np
from PIL import Image
import os


def load_images_from_folder(folder_path):
    """
    Load all image files from the given folder, convert them to lossless PNG
    in memory, and return them as NumPy arrays.

    Args:
        folder_path (str): Path to the folder containing scanned images.

    Returns:
        list of (str, np.ndarray): A list of tuples containing:
            - The base filename without extension.
            - The loaded image as a NumPy array (BGR format).
    """
    pass


def convert_to_grayscale(image):
    """
    Convert an image to grayscale for processing.

    Args:
        image (np.ndarray): Input BGR image.

    Returns:
        np.ndarray: Grayscale image.
    """
    pass


def find_split_column(gray_image):
    """
    Determine the center column index where the split between the two halves occurs.

    This function should:
    - Assume the split is always centered horizontally.
    - Search within the central 1/10 of the image width.
    - Use a brightness profile or similar technique to locate the vertical band.

    Args:
        gray_image (np.ndarray): Grayscale image.

    Returns:
        int: Column index where the split should occur.
    """
    pass


def crop_halves(image, split_column):
    """
    Crop the input image into two halves based on the split column.

    Args:
        image (np.ndarray): Original BGR image.
        split_column (int): Column index marking the center of the split.

    Returns:
        tuple: (left_half, right_half) as NumPy arrays (BGR format).
    """
    pass


def save_png(image, output_path):
    """
    Save a NumPy image array as an uncompressed PNG.

    Args:
        image (np.ndarray): Image to save (BGR format).
        output_path (str): Destination file path (should end in .png).
    """
    pass


def process_folder(input_folder, output_folder):
    """
    Main function to process all scanned images in a folder.

    Steps:
    1. Load all images from input_folder (any format).
    2. Convert each to lossless PNG format in memory.
    3. For each image:
       a. Convert to grayscale.
       b. Find split column.
       c. Crop into two halves.
       d. Save each half as an uncompressed PNG in output_folder.

    Args:
        input_folder (str): Path to folder with scanned images.
        output_folder (str): Path to folder where PNGs will be saved.
    """
    pass


def run():
    """
    Entry point called from main.py.
    Prompts user for input and output folder paths and processes images.
    """
    pass
