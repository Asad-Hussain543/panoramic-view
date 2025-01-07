import cv2
import imutils
from src.panorama import Panaroma

# Paths to the input images
image_paths = ["assets/prtn01.jpg", "assets/prtn00.jpg"]

# Load and resize images
images = [cv2.imread(path) for path in image_paths]
images = [imutils.resize(img, width=400) for img in images]

# Initialize the Panaroma class
panorama = Panaroma()

# Perform stitching
if len(images) == 2:
    result, matched_points = panorama.image_stitch([images[0], images[1]], match_status=True)
else:
    result, matched_points = panorama.image_stitch([images[-2], images[-1]], match_status=True)
    for i in range(len(images) - 2):
        result, matched_points = panorama.image_stitch([images[-i-3], result], match_status=True)

# Save the result
cv2.imwrite("output/panorama_result.jpg", result)
cv2.imwrite("output/matched_points.jpg", matched_points)

