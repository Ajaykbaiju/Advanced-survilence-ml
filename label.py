import cv2
import os

def save_frames_from_video(video_path, output_directory, frame_interval):
    # Open the video file
    video = cv2.VideoCapture(video_path)

    # Create the output directory if it doesn't exist
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Initialize frame count and frame index
    frame_count = 0
    frame_index = 2182

    while True:
        # Read a frame from the video
        ret, frame = video.read()

        # Break the loop if there are no more frames
        if not ret:
            break

        # Increment the frame count
        frame_count += 1

        # Skip frames based on the frame interval
        if frame_count % frame_interval != 0:
            continue

        # Save the frame as an image file
        frame_path = os.path.join(output_directory, f"normal2id{frame_index:05d}.jpg")
        cv2.imwrite(frame_path, frame)

        # Increment the frame index
        frame_index += 1

    # Release the video file
    video.release()

# Example usage
video_path = "D:\\project_final\\datasetformulti\\nor.mp4"

output_directory = "D:\\project_final\\frames"

frame_interval = 3  # Save every 1th frame

save_frames_from_video(video_path, output_directory, frame_interval)