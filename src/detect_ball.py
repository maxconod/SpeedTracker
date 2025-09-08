from ultralytics import YOLO
import cv2 as cv

model = YOLO("../Yolo-Weights/yolo11n.pt")
results = model("../Data/pic3_tennis.png", show=True)

model2 = YOLO("../Yolo-Weights/yolov8n.pt")
results2 = model2("../Data/pic3_tennis.png", show=True)

# Results
new_img = results[0].plot()
cv.imshow("New version", new_img)

new_img2 = results2[0].plot()
cv.imshow("Old version", new_img2)
cv.waitKey(0)