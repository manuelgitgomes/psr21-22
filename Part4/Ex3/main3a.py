#!/usr/bin/python3

import argparse
import cv2

# Global variables
window_name = 'window - Ex3a'
image_gray = None


def onTrackbar(threshold):
    # The value of the threshold of the binarization is the one on the trackbar
    global image_gray
    _, dst = cv2.threshold(image_gray, threshold, 255, cv2.THRESH_BINARY)
    cv2.imshow(window_name, dst)



def main():
    # Create parser
    parser = argparse.ArgumentParser()
    parser.add_argument('-img', '--image', type=str, required=True,help='Full path to image file.')
    args = vars(parser.parse_args())

    # Load image
    image = cv2.imread(args['image'], cv2.IMREAD_COLOR)

    # Convert to grey and use as a global variable
    global image_gray
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Show grey image
    cv2.namedWindow(window_name)
    cv2.imshow(window_name, image_gray)

    # Create trackbar to binarize image
    cv2.createTrackbar('Threshold', window_name, 0, 255, onTrackbar)

    cv2.waitKey(0)

if __name__ == '__main__':
    main()