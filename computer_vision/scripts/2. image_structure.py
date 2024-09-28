import numpy as np
import cv2

image_name = "blackwhite"

image = cv2.imread("/home/abdullah/catkin_ws/src/rostutorial/opencv/images/blackwhite.png")

if image is None:
    print(f"Error: Could not open or find the image {image_name}.png")
else:
    # Display pixel values for the loaded BGR image
    print("Pixel values of the image:\n", image)

    # Get and print the type of the image object
    image_type = type(image)
    print("Image type:", image_type)

    # Calculate and print the total size of the image (total number of pixels)
    image_size = image.size
    print("Image size (total number of pixels):", image_size)

    # Get and print the dimensions of the image (height, width, channels)
    image_dimensions = image.shape
    print("Image dimensions (height, width, channels):", image_dimensions)

    # Extract individual dimensions
    image_shape_height = image.shape[0]  # Height of the image
    image_shape_width = image.shape[1]   # Width of the image
    image_shape_channels = image.shape[2]  # Number of channels (3 for BGR)

    # Print individual dimensions
    print("Image height:", image_shape_height)
    print("Image width:", image_shape_width)
    print("Number of channels:", image_shape_channels)

    # Get and print the data type of the image array
    image_dtype = image.dtype
    print("Image data type:", image_dtype)

    # Access and print the pixel value at row 1, column 1
    pixel_value = image[1, 1]
    print("Value of pixel [1, 1]:", pixel_value)

    # Access and print the entire row at index 1
    row_value = image[1]
    print("Value of row [1]:", row_value)

    # Access and print the entire column at index 1
    column_value = image[:, 1]
    print("Value of column [1]:\n", column_value)

    # Get and print the shape of a specific row (row 1)
    row_shape = row_value.shape
    print("Shape of row [1]:", row_shape)

    # Get and print the shape of a specific column (column 1)
    column_shape = column_value.shape
    print("Shape of column [1]:", column_shape)

    # Modify the pixel value at row 1, column 1 to green
    image[1, 1] = [0, 255, 0]  # Setting the pixel to green
    print("Modified image after changing pixel [1, 1] to green:\n", image)

    # Modify the entire row at index 0 to white
    image[0] = [255, 255, 255]  # Changing the entire row to white
    print("Image after modifying row [0] to white:\n", image)

    # Modify the entire column at index 2 to blue
    image[:, 2] = [255, 0, 0]  # Changing the entire column to blue
    print("Image after modifying column [2] to blue:\n", image)

    # Access and print the size of the entire row
    row_size = row_value.size
    print("Size of row [1]:", row_size)

    # Access and print the size of the entire column
    column_size = column_value.size
    print("Size of column [1]:", column_size)

    # Print the modified image data
    print("Image after modifications:\n", image)

    # Extract and print each color channel
    image_channel_1 = image[:, :, 0]  # Blue channel
    print("Image channel 1 (Blue channel):\n", image_channel_1)

    image_channel_2 = image[:, :, 1]  # Green channel
    print("Image channel 2 (Green channel):\n", image_channel_2)

    image_channel_3 = image[:, :, 2]  # Red channel
    print("Image channel 3 (Red channel):\n", image_channel_3)

    # Display the modified image in a window
    cv2.namedWindow("Image", cv2.WINDOW_NORMAL)
    cv2.imshow("Image", image)  # Show the modified image
    cv2.waitKey(0)  # Wait for a key press
    cv2.destroyAllWindows()  # Close all OpenCV windows
