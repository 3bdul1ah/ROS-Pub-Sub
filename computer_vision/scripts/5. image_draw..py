import numpy as np
import cv2

blank_image = np.zeros((512, 512, 3), np.uint8)

cv2.line(blank_image, (0, 0), (511, 511), (255, 255, 255), 5) # cv2.line(image, start_point, end_point, color, thickness)
cv2.rectangle(blank_image, (384, 0), (510, 128), (0, 255, 0), 5) # cv2.rectangle(image, start_point, end_point, color, thickness)
cv2.ellipse(blank_image, (256, 256), (100, 50), 0, 0, 180, 255, -1) # cv2.ellipse(image, center_coordinates, axesLength, angle, startAngle, endAngle, color, thickness)

polygon_points = np.array([[10, 5], [20, 30],
                           [70, 20], [50, 10]],
                           np.int32)
polygon_points = polygon_points.reshape((-1, 1, 2))
cv2.polylines(blank_image, [polygon_points], True, (0, 255, 255)) # cv2.polylines(image, [polygon_points], isClosed, color, thickness)

font_type = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(blank_image, 'ROS, OpenCV', (10, 500), font_type, 2, (255, 255, 255), 2, cv2.LINE_AA) # cv2.putText(image, 'text', org, font, fontScale, color, thickness, cv2.LINE_AA)

cv2.imshow("Image Panel", blank_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
