from diffusers import StableDiffusionPipeline 
import torch 
import os 
from PIL import Image 
# Load Stable Diffusion model 
# pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

pipe = StableDiffusionPipeline.from_pretrained( "runwayml/stable-diffusion-v1-5",torch_dtype=torch.float16, use_auth_token=True ).to("cuda")
# Output folder 
output_dir = "synthetic_data" 
os.makedirs(output_dir, exist_ok=True) 
# Define prompts 
prompts = [  
    "A red sports car on a sunny road", 
    "A cat sitting on a wooden table", 
    "A person riding a bike in the mountains", 
    "An industrial robot in a factory", 
] 
# Generate images 
for i, prompt in enumerate(prompts): 
    image = pipe(prompt, num_inference_steps=100, guidance_scale=10).images[0] 
    filename = os.path.join(output_dir, f"synthetic_{i:03d}.png") 
    image.save(filename) 
    print(f"Saved: {filename}")