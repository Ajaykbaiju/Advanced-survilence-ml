import numpy as np
from keras.models import load_model
from keras.applications.vgg16 import preprocess_input
from keras.preprocessing.image import img_to_array
import cv2

# Load the trained model
model = load_model('model_abnormal_normal_new.h5')

# Set the input size based on your model's expected input shape
input_size = (150, 200)

# Open the camera
cap = cv2.VideoCapture(0)  # Use 0 for the default camera, you can change the index if you have multiple cameras

while True:
    # Read a frame from the camera
    ret, frame = cap.read()

    # Break the loop if there's an issue with the camera
    if not ret:
        print("Error reading frame from camera")
        break

    # Resize the frame to match the input size
    resized_frame = cv2.resize(frame, input_size)

    # Preprocess the resized frame
    preprocessed_frame = img_to_array(resized_frame)
    preprocessed_frame = preprocess_input(preprocessed_frame)

    # Make predictions
    predictions = model.predict(np.expand_dims(preprocessed_frame, axis=0))

    # Get the predicted class index
    predicted_class_index = np.argmax(predictions[0])

    # Get the corresponding label
    labels = ['abnormal', 'normal']
    predicted_label = labels[predicted_class_index]

    # Display the original frame with the predicted label
    cv2.putText(frame, predicted_label, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow('Live Feed', frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close the OpenCV windows
cap.release()
cv2.destroyAllWindows()
