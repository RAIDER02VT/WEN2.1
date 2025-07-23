# wan2_pipeline/generate_frames.py
import os
from PIL import Image
from diffusers import StableDiffusionImg2ImgPipeline
import torch

def generate_frames_img2img(
    prompt: str,
    init_image_path: str,
    output_folder: str,
    strength: float = 0.75,
    guidance: float = 7.5,
    num_frames: int = 10
):
    os.makedirs(output_folder, exist_ok=True)

    pipe = StableDiffusionImg2ImgPipeline.from_pretrained(
        "runwayml/stable-diffusion-v1-5",
        torch_dtype=torch.float16
    ).to("cuda")

    init_image = Image.open(init_image_path).convert("RGB")
    init_image = init_image.resize((512, 512))

    for i in range(num_frames):
        result = pipe(
            prompt=prompt,
            image=init_image,
            strength=strength,
            guidance_scale=guidance
        )
        result.images[0].save(os.path.join(output_folder, f"frame_{i:04d}.png"))

    print(f"✅ {num_frames} frame img2img salvati in {output_folder}")
