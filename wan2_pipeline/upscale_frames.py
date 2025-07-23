import os
import subprocess

def upscale_frames(input_folder, output_folder, realesrgan_exe="./realesrgan-ncnn-vulkan-v0.2.0-windows/realesrgan-ncnn-vulkan.exe", scale=4):
    os.makedirs(output_folder, exist_ok=True)

    for filename in sorted(os.listdir(input_folder)):
        if not filename.endswith(".png"):
            continue

        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)

        result = subprocess.run([
            realesrgan_exe,
            "-i", input_path,
            "-o", output_path,
            "-n", "realesrgan-x4plus",
            "-s", str(scale)
        ], capture_output=True, text=True)

        if result.returncode == 0:
            print(f"✅ Upscaled: {filename}")
        else:
            print(f"❌ Errore con {filename}:\n{result.stderr}")
