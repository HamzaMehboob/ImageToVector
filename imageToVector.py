import cv2
import numpy as np
import svgwrite

def image_to_vector(image_path, output_path):
    # Read the image
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    # Threshold the image to binary
    _, binary_image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
    # Find contours
    contours, _ = cv2.findContours(binary_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    # Create an SVG drawing
    dwg = svgwrite.Drawing(output_path, profile='tiny')
    
    # Draw each contour
    for contour in contours:
        # Convert contour points to a list of tuples with floats
        points = [(float(point[0][0]), float(point[0][1])) for point in contour]
        dwg.add(dwg.polygon(points, fill='black'))
    
    # Save the SVG file
    dwg.save()


