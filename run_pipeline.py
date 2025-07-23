from wan2_pipeline.extract_frames import extract_frames
from wan2_pipeline.interpolate_frames import interpolate_frames
from wan2_pipeline.upscale_frames import upscale_frames
from wan2_pipeline.build_video_from_frames import build_video_from_frames
from wan2_pipeline.generate_frames import generate_frames_img2img

prompt = "a futuristic robot walking through a neon city at night"
init_image_path = "input/base.jpg"  # immagine iniziale
generate_frames_img2img(
    prompt=prompt,
    init_image_path=init_image_path,
    output_folder="output/generated",
    num_frames=10
)
extract_frames("input/your_video.mp4", "output/frames")
interpolate_frames("output/frames", "output/interpolated")
upscale_frames("output/interpolated", "output/upscaled")
build_video_from_frames("output/upscaled", "output/final_video.mp4")
