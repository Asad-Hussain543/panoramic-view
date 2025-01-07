\# Panorama Stitching Project

This project implements an image stitching algorithm to create panoramic images by combining multiple overlapping images. The core logic is implemented using computer vision techniques like feature detection, keypoint matching, and homography estimation.

\## Features
- **Keypoint Detection**: Detects and matches keypoints between images using SIFT (Scale-Invariant Feature Transform).
- **Homography Estimation**: Computes a homography matrix to align overlapping images.
- **Seamless Stitching**: Creates a seamless panorama by warping and blending images.
- **Visualization**: Optionally visualizes matched keypoints.

\## Prerequisites
Ensure you have the following installed on your system:
- Python 3.8 or higher
- Libraries: `opencv-python`, `opencv-contrib-python`, `imutils`, `numpy`

\## Install the required Python libraries using:
\```
pip install opencv-python opencv-contrib-python imutils numpy
\```

\# Usage
Place input images in the `Input/` folder. Ensure the images have overlapping regions for better stitching results.

Run the script:
\```
python main.py
\```

View the outputs in the `Output/` folder:
- `panorama_result.jpg`: The final stitched panorama.
- `matched_points.jpg`: Visualization of matched keypoints (optional).

\# Folder Structure
\```
Input/: Folder for input images.
Output/: Folder for output images.
src/: Contains the core logic for image stitching.
    panorama.py: Implements the Panorama class.
    main.py: Script to execute the panorama stitching.
\```

\# Example

\### Input Images:
Place images like:

\```
Input/prtn01.jpg
Input/prtn00.jpg
\```

\### Output:
After running the script, the following outputs are generated:
- `Output/panorama_result.jpg`
- `Output/matched_points.jpg` (if visualization is enabled)

\## Acknowledgments
- OpenCV for image processing.
- SIFT for robust feature detection and matching.

\## Future Improvements
- Add support for non-linear blending to remove seams.
- Improve handling of input images with varying lighting conditions.
- Extend functionality to support video panorama stitching.
