from wan2_pipeline.extract_frames import extract_frames
from wan2_pipeline.interpolate_frames import interpolate_frames
from wan2_pipeline.upscale_frames import upscale_frames
from wan2_pipeline.build_video_from_frames import build_video_from_frames

extract_frames("input/your_video.mp4", "output/frames")
interpolate_frames("output/frames", "output/interpolated")
upscale_frames("output/interpolated", "output/upscaled")
build_video_from_frames("output/upscaled", "output/final_video.mp4")
