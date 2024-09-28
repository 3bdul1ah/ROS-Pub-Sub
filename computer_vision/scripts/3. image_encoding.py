import numpy as np
import cv2

image_name = "bird"
path = f"/home/abdullah/catkin_ws/src/rostutorial/opencv/images/{image_name}.jpg"

color_image = cv2.imread(path, cv2.IMREAD_COLOR)

if color_image is None:
    print(f"Error: Could not open or find the image {image_name}.jpg")

else:
    cv2.imshow("Original Image", color_image)
    cv2.moveWindow("Original Image", 0, 0)

    height, width, channels = color_image.shape
    blue, green, red = cv2.split(color_image)

    cv2.imshow("Blue Channel", blue)
    cv2.moveWindow("Blue Channel", 0, height)

    cv2.imshow("Green Channel", green)
    cv2.moveWindow("Green Channel", 0, height)

    cv2.imshow("Red Channel", red)
    cv2.moveWindow("Red Channel", 0, height)
# --------------------------------------------------------------------------
    hue_saturation_value = cv2.cvtColor(color_image, cv2.COLOR_BGR2HSV)
    hue, saturation, value = cv2.split(hue_saturation_value)
    hue_saturation_value_image = np.concatenate((hue, saturation, value), axis=1)

    cv2.imshow("Hue, Saturation, Value Image", hue_saturation_value_image)

# --------------------------------------------------------------------------
    gray_image = cv2.cvtColor(color_image, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Gray Image", gray_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
