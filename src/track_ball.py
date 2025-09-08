import cv2 as cv

cap = cv.VideoCapture("C:/Users/maxim/Documents/Uni_Projects/SpeedTracker/Data/BallExchange.mp4")

# Needing to extract one frame after another
while True:
    ret, frame = cap.read()

    cv.imshow("Frame", frame)

    key = cv.waitKey(30)
    if key == 27:
        break

cap.release()
# cv.destroyAllWindows()