#!/usr/bin/python3

import cv2

def main():
    # Capture webcam and create window
    capture = cv2.VideoCapture(0)
    window_name = 'A5-Ex2'
    cv2.namedWindow(window_name, cv2.WINDOW_AUTOSIZE)

    while True:
        # Capture an image from the webcam and show it
        _, image = capture.read()
        cv2.imshow(window_name, image)
        cv2.waitKey(1)

if __name__ == '__main__':
    main()