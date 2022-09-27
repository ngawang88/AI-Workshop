from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import numpy as np
import cv2


model = load_model('final.h5')

img_dim = 64

class_labels = [
    'Ngawang Samten',
    'Pema Thinley',
    'Sangay Tenzin',
    'Sonam Rabgay',
    'Tashi Phuntsho',
    'Yadu Nepal',
]


cap = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_SIMPLEX

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    cv2.rectangle(frame, (100, 100), (350, 350), (255, 255, 255), 2)
    roi = frame[100: 300, 100: 300]
    img = cv2.resize(roi, (img_dim, img_dim))
    img = image.img_to_array(img)
    img = np.expand_dims(img, axis=0)
    img = img.astype('float32')/255

    pred = np.argmax(model.predict(img))
  
    color = (0, 0, 255)

    cv2.putText(frame, class_labels[pred], (50, 50), font, 1.0, color, 2)
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()