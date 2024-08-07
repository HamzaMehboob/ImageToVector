import sys
import os

# Add the parent directory to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import imageToVector

image_path = 'Examples/input_image.png'  # Change to your image path
output_path = 'Examples/output_image.svg'  # Change to your desired output path
imageToVector.image_to_vector(image_path, output_path)