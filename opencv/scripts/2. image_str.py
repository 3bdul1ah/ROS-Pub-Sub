import numpy as np
import cv2

image_name = "blackwhite"
image = cv2.imread("images/" + image_name + ".png")

if image is None:
    print(f"Error: Could not open or find the image {image_name}.png")

else:
    print(image)  # Pixel values for the BGR image

    # Image type
    image_type = type(image)
    print("Image type:", image_type)

    # Image size (total number of pixels, width * height * channels)
    image_size = image.size
    print("Image size:", image_size)

    # Image dimensions (height, width, number of channels)
    image_dimensions = image.shape
    print("Image dimensions (height, width, channels):", image_dimensions)

    # Individual dimensions
    image_shape_height = image.shape[0]  # Height
    image_shape_width = image.shape[1]   # Width
    image_shape_channels = image.shape[2]  # Channels (3 for BGR)

    print("Image height:", image_shape_height)
    print("Image width:", image_shape_width)
    print("Number of channels:", image_shape_channels)
