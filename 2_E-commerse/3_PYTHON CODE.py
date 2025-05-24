from diffusers import StableDiffusionPipeline 
import torch 
from PIL import Image 
 
# Load pre-trained Stable Diffusion model 
# pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
pipe = StableDiffusionPipeline.from_pretrained( "runwayml/stable-diffusion-v1-5", torch_dtype=torch.float16, use_auth_token=True ).to("cuda")
 
# Function to generate product image 
def generate_product_image(prompt, output_path="product_image.png", guidance_scale=8.5): 
    image = pipe(prompt, guidance_scale=guidance_scale).images[0] 
    image.save(output_path) 
    return image 

# Example eCommerce prompt 
prompt = "high-quality photo of a modern leather handbag on a white studio background, e-commerce product shot" 
 
# Generate image 
image = generate_product_image(prompt) 
image.show()