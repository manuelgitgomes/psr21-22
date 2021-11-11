#!/usr/bin/python3

import cv2
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-img ', '--image_path', help='Image path', type=str)
    args = vars(parser.parse_args())

    image_filename = args['image_path']
    image = cv2.imread(image_filename, cv2.IMREAD_COLOR) # Load an image

    cv2.imshow('window', image)  # Display the image
    cv2.waitKey(0) # wait for a key press before proceeding


if __name__ == '__main__':
    main()