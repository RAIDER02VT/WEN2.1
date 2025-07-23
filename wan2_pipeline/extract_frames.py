import cv2
import os

def extract_frame(video_path, output_folder):
    os.makedir(output_folder, exits_ok = True)
    videocap = cv2.VideoCapture(video_path)
    success, image = cv2.read(videocap)
    count = 0

    while success:
        file_name = os.path.join(output_folder, "frame_{count:04d}.png" )
        cv2.imwrite(file_name, image)
        print(f"frame {count} salvato -> {filename}")
        success, image = cv2.read(video_path)
        count += 1

    cap.release()