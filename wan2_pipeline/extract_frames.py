import os
import cv2

def extract_frames(video_path, output_folder):
    os.makedirs(output_folder, exist_ok=True)

    cap = cv2.VideoCapture(video_path)
    success, image = cap.read()
    count = 0

    while success:
        file_name = os.path.join(output_folder, f"frame_{count:04d}.png")
        cv2.imwrite(file_name, image)
        print(f"🖼️ Frame {count} salvato → {file_name}")
        success, image = cap.read()
        count += 1

    cap.release()
    print(f"✅ Estrazione completata. Totale frame: {count}")
