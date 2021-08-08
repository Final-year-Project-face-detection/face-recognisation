import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime
from pathlib import Path
from CSE.models import FourthYearASec
from studentsAttendence.models import StudentsDetails


BASE_DIR = Path(__file__).resolve().parent.parent
loc = os.path.join(BASE_DIR, 'media/uploads')
images = []
classNames = []
myList = os.listdir(loc)

for cl in myList:
    curImg = cv2.imread(f'{loc}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])
print(classNames)


def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGRA2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList


def markAttendence(name):
    if name != 'UNKNOWN':
        with open(os.path.join(BASE_DIR, 'studentsAttendence/Attendence.csv'), 'r+') as f:
            myDataList = f.readlines()
            nameList = []
            for line in myDataList:
                entry = line.split(',')
                nameList.append(entry[0])

            if name not in nameList:
                now = datetime.now()
                dtString = now.strftime('%H:%M:%S')
                FourthYearASec.objects.create(
                    usn = name,
                    status = 'P',
                    edate = now,
                    ldate = now,
                )
                f.writelines(f'\n{name}, {dtString}')
            if name in nameList:
                now = datetime.now()
                dtString = now.strftime('%H:%M:%S')
                t = FourthYearASec.objects.get(usn=name)
                t.ldate = now  # change field
                t.save()
                


encodeListKnown = findEncodings(images)
print(len(encodeListKnown), 'Encoding Complete')
camara = 0

class LiveWebCam(object):
    def __init__(self):
        self.url = cv2.VideoCapture(camara)

    def __del__(self):
        cv2.destroyAllWindows()

    def get_frame(self):
        while True:
            success, img = self.url.read()
            resize = cv2.resize(img, (640, 480), interpolation=cv2.INTER_LINEAR)
            ret, jpeg = cv2.imencode('.png', resize)
            imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
            imgS = cv2.cvtColor(imgS, cv2.COLOR_BGRA2RGB)

            facesCurFrame = face_recognition.face_locations(imgS)
            encodeCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

            for encodeFace, faceLoc in zip(encodeCurFrame, facesCurFrame):
                matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
                faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
                print(faceDis)
                matchIndex = np.argmin(faceDis)

                if matches[matchIndex]:
                    if faceDis[0] < 0.75:
                        name = classNames[matchIndex].upper()
                    else:
                        name = "UNKNOWN"
                    print(name)
                    y1, x2, y2, x1 = faceLoc
                    y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                    cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
                    cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
                    markAttendence(name)
                    0xFF == ord('q')
            ret, jpeg = cv2.imencode('.png', img)
            return jpeg.tobytes()

if cv2.waitKey(1) & 0xFF == ord('q'):
    exit(43)
