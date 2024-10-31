import cv2
import os

def extract_frames(video_path, output_folder):
    # Open the video file
    video = cv2.VideoCapture(video_path)
    if not video.isOpened():
        print(f"Error: Could not open video file {video_path}")
        return

    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Initialize variables
    frame_count = 0
    success = True

    while success:
        # Read the next frame from the video
        success, frame = video.read()

        if frame_count % 15 == 0:  # Extract frame every 30 frames (1 frame per second)
            # Save the frame as an image file
            frame_path = os.path.join(output_folder, f"frame_{frame_count}.jpg")
            cv2.imwrite(frame_path, frame)

        frame_count += 1

    # Release the video file
    video.release()

if __name__ == "__main__":
    video_path = r"C:\Users\GiaBao\Documents\VSC\Robotics\camera_calibration_cpp\src\video\pool_calibration.mp4"
    output_folder = r"C:\Users\GiaBao\Documents\VSC\Robotics\camera_calibration_cpp\src\image"
    extract_frames(video_path, output_folder)