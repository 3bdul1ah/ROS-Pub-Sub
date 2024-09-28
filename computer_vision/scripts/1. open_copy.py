import numpy as np
import cv2

image_name = "bird"

print("Read an image from file")
img = cv2.imread("images/" + image_name + ".jpg")

if img is None:
    print("Error: Image not found.")

else:
    print("Create a window holder for the image")
    cv2.namedWindow("Image", cv2.WINDOW_NORMAL)

    print("Display the image")
    cv2.imshow("Image", img)

    print("Press a key inside the image window to make a copy")
    cv2.waitKey(0)

    print("Image copied to folder images/copy")
    cv2.imwrite("images/copy/" + image_name + "-copy.jpg", img)

    cv2.destroyAllWindows()
