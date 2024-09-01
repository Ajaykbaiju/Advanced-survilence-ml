import cv2
import datetime

# Load pre-trained LBPH face recognizer model
base_dir = "dataset/"
model = cv2.face.LBPHFaceRecognizer_create()
model.read(base_dir + 'model.xml')

# Load cascade classifier for face detection
face_cascade = cv2.CascadeClassifier("dataset/haarcascade_frontalface_default.xml")

# Open webcam
cap = cv2.VideoCapture(0)

while True:
    # Read frame from webcam
    ret, frame = cap.read()

    # Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    # Perform facial recognition on detected faces
    for (x, y, w, h) in faces:
        # Extract the face region
        face = gray[y:y+h, x:x+w]
        face = cv2.resize(face, (130, 100))

        # Perform prediction using the model
        label, confidence = model.predict(face)

        # Determine the label of the recognized person
        if confidence < 100:
            # Display the recognized label
            cv2.putText(frame, str(label), (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

            # Get the current date and time
            current_datetime = str(datetime.datetime.now()).split(" ")
            print("Prediction:", label, current_datetime)

            # Perform some action with the recognized label and datetime
            # For example:
            # fun(str(label), current_datetime[0], current_datetime[1])
        else:
            # If confidence is too high, mark as unknown
            cv2.putText(frame, "Unknown", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)

    # Display the frame
    cv2.imshow('Face Recognition', frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close all windows
cap.release()
cv2.destroyAllWindows()
