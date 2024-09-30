import cv2
import time
import uuid
import os

IMAGES_PATH = os.path.join('data', 'images')
number_of_images = 30

cap = cv2.VideoCapture(0)
time.sleep(2)

for imgnum in range(number_of_images):
    print('Collecting image{}'.format(imgnum))
    ret, frame = cap.read()
    if not ret:
        print("Failed to capture frame")
        continue
    imgname = os.path.join(IMAGES_PATH, f'{str(uuid.uuid4())}.jpg')
    cv2.imwrite(imgname, frame)
    cv2.imshow('frame', frame)

    time.sleep(0.5)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


