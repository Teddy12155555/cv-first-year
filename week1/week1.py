from cv2 import cv2
from enum import Enum
from tqdm import tqdm
from argparse import ArgumentParser
import face_recognition

class VideoFormat(Enum):
    MPEG_4 = 'mp4v'
    
class VideoFaceDetection:
    def __init__(self,fileName):
        self.IFileName = fileName
        self.Capture = cv2.VideoCapture(f"{fileName}")
        self.Width = int(self.Capture.get(cv2.CAP_PROP_FRAME_WIDTH))
        self.Height = int(self.Capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
        self.FPS = self.Capture.get(cv2.CAP_PROP_FPS)
        self.TotalFrames = int(self.Capture.get(cv2.CAP_PROP_FRAME_COUNT))

    def setOutputFile(self,format,fileName):
        filepath = "./output/" + fileName
        self.OFileName = filepath
        self.Format = cv2.VideoWriter_fourcc(*f'{format.value}')
        self.Output = cv2.VideoWriter(filepath, self.Format, self.FPS, (self.Width, self.Height))

    def detect(self,gpu):
        print("Running ...")
        print("Press Enter to exit")
        progress = tqdm(total=self.TotalFrames)
        if gpu:
            while True:
                ret, frame = self.Capture.read()
                if frame is None:
                    break

                rgb_frame = frame[:, :, ::-1]
                face_locations = face_recognition.face_locations(rgb_frame,model="cnn")
                for top, right, bottom, left in face_locations:
                    cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), cv2.LINE_AA)

                self.Output.write(frame)

                cv2.imshow('Frames', frame)
                progress.update(1)
                # enter = ascii 13
                if cv2.waitKey(3) == 13:
                    break
        else:
           while True:
                ret, frame = self.Capture.read()
                if frame is None:
                    break

                rgb_frame = frame[:, :, ::-1]
                face_locations = face_recognition.face_locations(rgb_frame)
                for top, right, bottom, left in face_locations:
                    cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), cv2.LINE_AA)

                self.Output.write(frame)

                cv2.imshow('Frames', frame)
                progress.update(1)
                # enter = ascii 13
                if cv2.waitKey(3) == 13:
                    break

    def describe(self):
        print("---------- Info ----------")
        print(f"Input : {self.IFileName}")
        print(f"Output : {self.OFileName}")
        print(f"FPS : {self.FPS}")
        print(f"TotalFrames : {self.TotalFrames}")
        print(f"Width : {self.Width}")
        print(f"Height : { self.Height}")
        print("---------- Start ----------")
        
if __name__ == "__main__":

    parser = ArgumentParser()
    parser.add_argument("-i", help="input video file name",dest="input")
    parser.add_argument("-o", help="output video file name", dest="output")
    parser.add_argument("-gpu", help="if use gpu", dest="gpu")

    args = parser.parse_args()
    flag = False
    if bool(args.gpu):
        flag = True
    
    vfd = VideoFaceDetection(args.input)
    vfd.setOutputFile(format=VideoFormat.MPEG_4,fileName=args.output)
    vfd.describe()
    print("")
    vfd.detect(flag)
    