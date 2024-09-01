import numpy as np
from keras.models import load_model
from keras.applications.vgg16 import preprocess_input
from keras.preprocessing.image import img_to_array
import cv2

# Load the trained model
model = load_model('model_abnormal_normal_new.h5')

# Set the input size based on your model's expected input shape
input_size = (150, 200)

# Open the video file
cap = cv2.VideoCapture('normal 2.mp4')
#cap=cv2.VideoCapture(0)

while True:
    # Read a frame from the video
    ret, frame = cap.read()

    # Break the loop if the video is over
    if not ret:
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
    text_frame = frame.copy()
    cv2.putText(text_frame, predicted_label, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    # Resize only the region where putText is applied
    scale_percent = 50  # adjust this value based on your preference
    width = int(text_frame.shape[1] * scale_percent / 100)
    height = int(text_frame.shape[0] * scale_percent / 100)
    dim = (width, height)
    resized_text_frame = cv2.resize(text_frame, dim, interpolation=cv2.INTER_AREA)

    # Display the resized frame with the predicted label
    cv2.imshow('Video', resized_text_frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close the OpenCV windows
cap.release()
cv2.destroyAllWindows()
