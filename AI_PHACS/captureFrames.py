import argparse
import csv
import os

import cv2

def capture_frames(Id, name):
    with open("StudentDetails.csv", 'r') as csvFile:
        lines = csv.reader(csvFile)
        data = list(lines)
        row_count = len(data)
        for n in range(row_count):
            print(n)
            for row in lines:
                if row[0] == id:
                    return 'same-id'

                if row == '\n':
                    break
    parser = argparse.ArgumentParser(description='Capture Student Face Image.')
    parser.add_argument('--face_cascade', default='haarcascade_frontalface_default.xml')
    parser.add_argument('--camera', type=int, default=0)
    args = parser.parse_args()

    face_cascade_name = args.face_cascade
    face_cascade = cv2.CascadeClassifier()

    # -- 1. Load the cascade
    if not face_cascade.load(cv2.samples.findFile(face_cascade_name)):
        return 'face-cascade-loading-error'

    camera_device = args.camera

    # -- 2. Read the video stream
    cap = cv2.VideoCapture(camera_device)
    if not cap.isOpened:
        return 'video-open-error'

    row = [Id, name]
    sampleNum = 0

    while (True):
        ret, frame = cap.read()
        if frame is None:
            cap.release()
            cv2.destroyAllWindows()
            return 'no-capture-frame'


        # convert it to grayscale using the cvtcolor image
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # detectMultiScale() function returns  list of objects as rectangles.
        # The first parameter is a ndarray of the image
        # detectMultiScale(InputArray 	image,
        #            double 	scaleFactor = 1.1, how much the image size is reduced at each image scale.
        #            int 	minNeighbors = 3, how many neighbors each candidate rectangle should have to retain it.
        #            int 	flags = 0,
        #            Size 	minSize = Size(),
        #            Size 	maxSize = Size()  )
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 1)
            # incrementing sample number
            sampleNum = sampleNum + 1
            # saving the captured face in the dataset folder images
            cv2.imwrite("captured_images" + os.sep + name + "_" + Id + '_' +
                        str(sampleNum) + ".jpg", gray[y:y + h, x:x + w])
            # display the frame
            cv2.imshow('frame', frame)
        # wait for 100 miliseconds
        if cv2.waitKey(100) & 0xFF == ord('q'):
            break
        # break if the sample number is more than 100
        elif sampleNum == 100:
            break

    with open("StudentDetails.csv", 'a+', newline='') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(row)
    csvFile.close()
    cap.release()
    cv2.destroyAllWindows()
    return ''
