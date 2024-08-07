# ImageToVector

This project converts images to vector graphics (SVG) using Python. It reads an image, converts it to a binary image, finds the contours, and then creates an SVG file with those contours.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/HamzaMehboob/ImageToVector.git
    cd ImageToVector
    ```

2. Install the required Python libraries:
    ```sh
    pip install opencv-python svgwrite numpy
    ```

## Usage

1. Place your input image in the `ImageToVector/Examples` directory and name it `input_image.png`.
2. Run the conversion script:
    ```sh
    python Examples/sample.py
    ```

3. The output SVG file will be saved as `output_image.svg` in `Example` folder .
