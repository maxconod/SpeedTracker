from ultralytics import YOLO
import cv2

model = YOLO("yolov8n.pt")
results = model("C:/Users/maxim/Documents/Uni_Projects/SpeedTracker/Data/pic2_tennis.jpg", show=True)
cv2.waitKey(0)