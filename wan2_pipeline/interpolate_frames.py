import cv2 
import os
import subprocess

def interpolate_frames(input_folder: str, output_folder: str, target_fps: int = 30) -> None:
    os.makedir("interpolate_folder", exists_ok = True)
    temp_video_path = os.join.path(output_folder, "temp_input.mp4")
    interpolated_video_path = os.join.path(output_folder, "interpolated_video.mp4")

    subprocess.run([
        "ffmpeg", "-y",
        "-framerate", "8",
        "-i", os.path.join(input_folder,"frame_count%04d.png"),
        "-c:v", "libx264", "-pix_fmt", "yuv420p",
        temp_video_path]check=True)
                                                                                                                                                                                                                                                                                                                                                                                                                                                   
    print(f"🎥 Video temporaneo creato → {temp_video_path}")

    subprocess.run([
        "ffmpeg", "-y",
        "-i", temp_video_path
        "-vf", f"minterpolate=fps={target_fps}",
        "-c:v", "libx264", "-pix_fmt", "yuv420p",
        interpolated_video_path
    ]check=True)

    print(f"✅ Interpolazione completata → {interpolated_video_path}")

    subprocess.run([
        "ffmpeg", "-y",
        "-i", interpolated_video_path,
        os.path.join(output_folder, "frame_%04d.png")
    ]check=True)

    print(f"🖼️ Frame interpolati salvati in: {output_folder}")