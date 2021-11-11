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
    image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Defining ranges
    ranges = {'h': {'min': 60, 'max': 100},
              's': {'min': 50, 'max': 255},
              'v': {'min': 50, 'max': 255}}

    mins = np.array([ranges['h']['min'], ranges['s']['min'], ranges['v']['min']])
    maxs = np.array([ranges['h']['max'], ranges['s']['max'], ranges['v']['max']])
    mask = cv2.inRange(image_hsv, mins, maxs)

    # Convert from uint8 to bool
    mask = mask.astype(np.bool)

    # Change color of mask
    img_h, img_s, img_v = cv2.split(image_hsv)
    img_h[mask] = (img_h[mask] - 140).astype(np.uint8)

    # Piece the parts together
    img_processed = cv2.merge((img_h, img_s, img_v))

    # Reconvert to BGR and UInt8
    img_processed = cv2.cvtColor(img_processed, cv2.COLOR_HSV2BGR)
    mask = mask.astype(np.uint8)*255

    cv2.imshow('Original', image)
    cv2.imshow('Mask', mask)
    cv2.imshow('New Image', img_processed)
    cv2.waitKey(0)


if __name__ == '__main__':
    main()