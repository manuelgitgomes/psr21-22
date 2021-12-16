#!/usr/bin/python3
import copy

import cv2

def main():
    # Capture webcam and create window
    capture = cv2.VideoCapture('test.mp4')
    window_name = 'A5-Ex2'
    cv2.namedWindow(window_name, cv2.WINDOW_AUTOSIZE)

    # Creating the face classifier
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    while True:
        # Capture an image from the webcam
        _, image = capture.read()

        # When the image is not detected, the video is over
        if image is None:
            print('Video over, goodbye!')
            break

        # Creating copy
        image_gui = copy.deepcopy(image)

        # Image size
        h, w, _ = image_gui.shape

        # Face detection
        image_grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(image_grey, 1.1, 4)

        for (x, y, h, w) in faces:
            cv2.rectangle(image_gui, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # Show the image
        cv2.imshow(window_name, image_gui)

        # If q is pressed, end video
        key = cv2.waitKey(20)
        if key == ord('q')  :
            print('Video interrupted by user')
            break


if __name__ == '__main__':
    main()