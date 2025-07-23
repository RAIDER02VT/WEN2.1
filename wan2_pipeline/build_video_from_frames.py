import os
import cv2

def build_video_from_frames(frames_folder: str, output_path: str, fps: int = 30) -> None:
    frames = sorted([f for f in os.listdir(frames_folder) if f.endswith(".png")])
    if not frames:
        print("❌ Nessun frame trovato.")
        return

    first_frame_path = os.path.join(frames_folder, frames[0])
    first_frame = cv2.imread(first_frame_path)
    height, width, _ = first_frame.shape

    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    for frame in frames:
        frame_path = os.path.join(frames_folder, frame)
        image = cv2.imread(frame_path)
        out.write(image)

    out.release()
    print(f"✅ Video finale salvato: {output_path}")
