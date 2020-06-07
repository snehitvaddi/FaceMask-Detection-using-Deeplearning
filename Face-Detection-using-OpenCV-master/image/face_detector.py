# Import libraries
import os
import numpy as np
import imutils
import cv2

# Define paths
base_dir = os.path.join( os.path.dirname( __file__ ), '../' )
prototxt_path = os.path.join(base_dir + 'model_data/deploy.prototxt')
caffemodel_path = os.path.join(base_dir + 'model_data/weights.caffemodel')
image_path = base_dir + 'image/image.png'

# Read the model
model = cv2.dnn.readNetFromCaffe(prototxt_path, caffemodel_path)

# Load image
frame = cv2.imread(image_path)
frame = imutils.resize(frame, width = 400, height = 200)

(h, w) = frame.shape[:2]
blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)), 1.0, (300, 300), (104.0, 177.0, 123.0))

model.setInput(blob)
detections = model.forward()

# Create frame around face
for i in range(0, detections.shape[2]):
    box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
    (startX, startY, endX, endY) = box.astype("int")
    
    confidence = detections[0, 0, i, 2]
    
    # If confidence > 0.5, show box around face
    if (confidence > 0.5):
        text = "{:.2f}%".format(confidence * 100)
        y = startY - 10 if startY - 10 > 10 else startY + 10
        cv2.rectangle(frame, (startX, startY), (endX, endY), (255, 255, 255), 2)
        cv2.putText(frame, text, (startX, y), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (255, 255, 255), 2)
        
    cv2.imshow("Frame", frame)

# Close frame on pressing key `q`
while True:
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break