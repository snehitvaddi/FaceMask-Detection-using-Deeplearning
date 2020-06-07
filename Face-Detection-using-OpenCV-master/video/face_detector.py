# Import libraries
from imutils.video import VideoStream
import os
import numpy as np
import imutils
import cv2

# Define paths
base_dir = os.path.join( os.path.dirname( __file__ ), '../' )
prototxt_path = os.path.join(base_dir + 'model_data/deploy.prototxt')
caffemodel_path = os.path.join(base_dir + 'model_data/weights.caffemodel')

# Read the model
model = cv2.dnn.readNetFromCaffe(prototxt_path, caffemodel_path)

# Start video capture
vs = cv2.VideoCapture(0)

# Display each video frame
while True:
    ret, frame = vs.read()
    frame = imutils.resize(frame, width = 1600, height = 900)
    
    (h, w) = frame.shape[:2]
    blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)), 1.0, (300, 300), (104.0, 177.0, 123.0))
    
    model.setInput(blob)
    detections = model.forward()
    
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
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vs.release()
cv2.destroyAllWindows()