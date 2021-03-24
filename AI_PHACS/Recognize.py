#cv2.putText(image, text, org, font, fontScale, color[, thickness[, lineType[, bottomLeftOrigin]]])

# Parameters:
# image: It is the image on which text is to be drawn.
# text: Text string to be drawn.
# org: It is the coordinates of the bottom-left corner of the text string in the image. The coordinates are represented as tuples of two values i.e. (X coordinate value, Y coordinate value).
# font: It denotes the font type. Some of font types are FONT_HERSHEY_SIMPLEX, FONT_HERSHEY_PLAIN, , etc.
# fontScale: Font scale factor that is multiplied by the font-specific base size.
# color: It is the color of text string to be drawn. For BGR, we pass a tuple. eg: (255, 0, 0) for blue color.
# thickness: It is the thickness of the line in px.
# lineType: This is an optional parameter.It gives the type of the line to be used.
# bottomLeftOrigin: This is an optional parameter. When it is true, the image data origin is at the bottom-left corner. Otherwise, it is at the top-left corner.

# Return Value: It returns an image.



import datetime
import os
import time
import cv2
import pandas as pd

def recognize():
    fname = "TrainingImageLabel/Trainner.yml"

    if not os.path.isfile(fname):
        return 'yml-file-absent'

    faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    cap = cv2.VideoCapture(0)
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read(fname)

    # TODO : implement fetching from database here,

    #  data in studentDetails.csv represent that student's frames are captured.
    df = pd.read_csv("StudentDetails.csv")
    #



    col_names = ['Id', 'Name', 'Date', 'Time']
    # attendance = pd.DataFrame(df)
    attendance = pd.DataFrame(columns=col_names)


    while 1:
        ret, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray, 1.3, 5)
        for(x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

            # Id & conf fetched from trainner.yml file
            Id, conf = recognizer.predict(gray[y:y+h, x:x+w])
            # print(conf, Id)
            # conf = 40
            Id = str(Id)
            Id = int(Id[:2] + '123' + Id[2:])

            name = df.loc[df['Id'] == Id]['Name'].values
            name = name[0]

            if conf < 50:
                ts = time.time()
                date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
                timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
                attendance.loc[len(attendance)] = [Id, name, date, timeStamp]

            if conf < 50:
                cv2.putText(img, str(name), (x+2,y+h-5), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            else:
                cv2.putText(img, 'Unknown', (x+2,y+h-5), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0, 255), 2)

        attendance = attendance.drop_duplicates(subset=['Id'], keep='first')
        cv2.imshow('Attendance', img)
        if (cv2.waitKey(1) == ord('q')):
            break

    # print(attendance)
    ts = time.time()
    date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
    timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
    Hour, Minute, Second = timeStamp.split(":")
    fileName = "Attendance"+os.sep+"Attendance_"+date+"_"+Hour+"-"+Minute+"-"+Second+".csv"
    attendance.to_csv(fileName, index=False)
    # print("Attendance Successful")
    cap.release()
    cv2.destroyAllWindows()
    return 'sucess'