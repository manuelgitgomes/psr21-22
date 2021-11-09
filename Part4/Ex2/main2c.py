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

    # Split the image into its 3 channels
    img_b, img_g, img_r = cv2.split(image)

    # Binarizes every channel
    _, image_b_thresholded = cv2.threshold(img_b, 50, 255, cv2.THRESH_BINARY)
    _, image_g_thresholded = cv2.threshold(img_g, 100, 255, cv2.THRESH_BINARY)
    _, image_r_thresholded = cv2.threshold(img_r, 150, 255, cv2.THRESH_BINARY)

    img_new = cv2.merge((image_b_thresholded, image_g_thresholded, image_r_thresholded))

    cv2.imshow('Original', image)
    cv2.imshow('Blue Threshold', image_b_thresholded)
    cv2.imshow('Red Threshold', image_g_thresholded)
    cv2.imshow('Green Threshold', image_r_thresholded)
    cv2.imshow('New Image', img_new)
    cv2.waitKey(8000)


if __name__ == '__main__':
    main()