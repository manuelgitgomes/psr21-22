#!/usr/bin/python3

import cv2
import argparse

def main():
    # Create parser
    parser = argparse.ArgumentParser()
    parser.add_argument('-img ', '--image_path', help='Image path', type=str)
    args = vars(parser.parse_args())

    # Read the image path from the parser and load the image with opencv
    image_filename = args['image_path']
    image = cv2.imread(image_filename, cv2.IMREAD_COLOR)

    # Transform the image to grey and then binarize it
    grey = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    retval, image_thresholded = cv2.threshold(grey, 128, 255, cv2.THRESH_BINARY)

    # Display the image and wait for a key press before proceeding
    cv2.imshow('window', image_thresholded)
    cv2.waitKey(0)


if __name__ == '__main__':
    main()