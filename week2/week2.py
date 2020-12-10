from cv2 import cv2
from enum import Enum
from tqdm import tqdm
from argparse import ArgumentParser
import face_recognition
import numpy as np

class FaceDetection(object):
  def __init__(self):
    self.Capture = cv2.VideoCapture(0)
    
  def detect(self,gpu):
    print("Running ...")
    print("Press Enter to exit")
    if gpu:
      while(True):
        ret, frame = self.Capture.read()
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

        rgb_frame = small_frame[:, :, ::-1]
        face_locations = face_recognition.face_locations(rgb_frame,model="cnn")

        for top, right, bottom, left in face_locations:
          top *= 4
          right *= 4
          bottom *= 4
          left *= 4
          cv2.rectangle(frame, (left, top), (right, bottom), (255, 0, 255),2)

        cv2.imshow('FaceDetection', frame)
        # enter = ascii 13
        if cv2.waitKey(2) == 13:
          self.Capture.release()
          cv2.destroyAllWindows()
          break
    else:
      while(True):
        ret, frame = self.Capture.read()
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

        rgb_frame = small_frame[:, :, ::-1]

        face_locations = face_recognition.face_locations(rgb_frame)
      
        for top, right, bottom, left in face_locations:
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4
            cv2.rectangle(frame, (left, top), (right, bottom), (255, 0, 255),2)

        cv2.imshow('FaceDetection', frame)

        # enter = ascii 13
        if cv2.waitKey(2) == 13:
          self.Capture.release()
          cv2.destroyAllWindows()
          break
    
if __name__ == "__main__":

    parser = ArgumentParser()
    parser.add_argument("-gpu", help="if use gpu", dest="gpu")

    args = parser.parse_args()
    flag = False
    if bool(args.gpu):
        flag = True
    
    fd = FaceDetection()
    fd.detect(flag)
    
