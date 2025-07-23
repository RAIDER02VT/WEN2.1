from extract_frames import extract_frames
from interpolate_frames import interpolate_frames
from upscale_frames import upscale_frames
from build_video import build_video_from_frames

# Esegui tutti gli step in sequenza
extract_frames("video.mp4", "frames")
interpolate_frames("frames", "interpolated_frames")
upscale_frames("interpolated_frames", "upscaled_frames")
build_video_from_frames("upscaled_frames", "final_video.mp4")
