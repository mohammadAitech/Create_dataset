Pelak Dataset Creator
Introduction

This project is a tool to create a dataset of vehicle license plates by processing images stored in directories. It uses OpenCV to resize, convert, and flatten the images, preparing them for machine learning applications.
Features

    Reads images from a specified directory.
    Resizes images to a fixed size of 8x32 pixels.
    Converts images to grayscale for uniformity.
    Flattens the processed images into a single-dimensional array.
    Creates feature (X) and label (Y) arrays ready for machine learning tasks.

Project Structure

pelak-dataset/
│
├── pelak/                   # Main directory containing subdirectories for labels
│   ├── 0/                   # Subdirectory for class "0"
│   ├── 1/                   # Subdirectory for class "1"
│   └── ...                  # Other subdirectories for other classes
│
├── dataset_creator.py       # Python script containing the dataset creation logic
└── README.md                # Project documentation

Requirements

    Python 3.7+
    Libraries:
        OpenCV (cv2)
        NumPy (numpy)

Install the dependencies using pip:

pip install opencv-python-headless numpy

Usage

    Organize your dataset:
        Create a directory named pelak in the project root.
        Create subdirectories inside pelak for each class label. For example:

    pelak/
    ├── 0/
    ├── 1/
    └── ...

    Place images in the corresponding subdirectories.

Run the script:

from dataset_creator import pelak_datasets

# Example usage
X, Y = pelak_datasets("0")  # Replace "0" with the class label directory name

Output:

    X: A NumPy array containing the flattened feature vectors of images.
    Y: A NumPy array containing the corresponding labels