#!/usr/bin/python3
import copy

import cv2
import argparse
import numpy as np

def main():
    # Create parser
    parser = argparse.ArgumentParser()
    parser.add_argument('-img ', '--image_path', help='Image path', type=str)
    args = vars(parser.parse_args())

    # Read the image path from the parser and load the image with opencv
    image_filename = args['image_path']
    image = cv2.imread(image_filename, cv2.IMREAD_COLOR)

    # Defining ranges
    ranges = {'b': {'min': 0, 'max': 50},
              'g': {'min': 80, 'max': 255},
              'r': {'min': 0, 'max': 50}}

    mins = np.array([ranges['b']['min'], ranges['g']['min'], ranges['r']['min']])
    maxs = np.array([ranges['b']['max'], ranges['g']['max'], ranges['r']['max']])
    mask = cv2.inRange(image, mins, maxs)

    # Convert from uint8 to bool
    mask = mask.astype(np.bool)

    # Create img_processed
    img_processed = copy.copy((image))

    # Change color of mask
    img_b, img_g, img_r = cv2.split(img_processed)
    img_r[mask] = (img_r[mask] * 3).astype(np.uint8)
    img_g[mask] = (img_g[mask] * 0.2).astype(np.uint8)
    img_b[mask] = (img_b[mask] * 0.5).astype(np.uint8)

    # Piece the parts together
    img_processed = cv2.merge((img_b, img_g, img_r))

    cv2.imshow('Original', image)
    cv2.imshow('Mask', mask.astype(np.uint8))
    cv2.imshow('New Image', img_processed)
    cv2.waitKey(8000)


if __name__ == '__main__':
    main()