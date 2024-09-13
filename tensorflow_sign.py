import cv2
import os
import time 
import uuid

IMAGES_PATH = 'Tensorflow/workspace/images/collected_images'

labels = ['A', 'B', 'C', 'D']
number_imgs = 15 

# Asegurarse de que los directorios existan
for label in labels: 
    os.makedirs(os.path.join(IMAGES_PATH, label), exist_ok=True)
    cap = cv2.VideoCapture(0)
    print('Collecting images for {}'.format(label))
    time.sleep(5)

    for imgnum in range(number_imgs):
        ret, frame = cap.read()
        if not ret:
            print("Error al capturar la imagen")
            break

        imgname = os.path.join(IMAGES_PATH, label, label + '.' + '{}.jpg'.format(str(uuid.uuid1())))
        cv2.imwrite(imgname, frame)
        cv2.imshow('frame', frame)
        time.sleep(2)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()

cv2.destroyAllWindows()
