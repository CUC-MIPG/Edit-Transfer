import torch
from toolkit.pipeline_flux_inpaint import FluxInpaintPipeline
# from diffusers import FluxInpaintPipeline
from PIL import Image
import os
from toolkit.samplers.custom_flowmatch_sampler import CustomFlowMatchEulerDiscreteScheduler
from argparse import ArgumentParser



parser = ArgumentParser()

parser.add_argument("--model_dir", type=str)
parser.add_argument("--model_name", type=str)
parser.add_argument("--prompt_file",  type=str)
parser.add_argument("--img_path", type=str)
parser.add_argument("--save_dir", default="result", type=str)

args = parser.parse_args()

pipe = FluxInpaintPipeline.from_pretrained("/data/models/FLUX.1-dev/", torch_dtype=torch.bfloat16)
pipe.to("cuda")
# pipe.enable_model_cpu_offload()
pipe.load_lora_weights(args.model_dir, weight_name=args.model_name)

if not os.path.exists(args.save_dir):
    os.makedirs(args.save_dir)

mask=torch.zeros(1,1024,1024)
mask[:,mask.size(1)//2:,mask.size(2)//2:] = 1
img = Image.open(args.img_path).convert('RGB')
with open(args.prompt_file, 'r', encoding='utf-8') as file:
    prompt = file.readline()

for i in range(16):
    seed = torch.randint(low=1, high=99999, size=(1,)).item()
    out = pipe(
        prompt=prompt,
        mask_image = mask,
        image=img,
        guidance_scale=1.0,
        height=1024,
        width=1024,
        num_inference_steps=35,
        generator=torch.Generator("cpu").manual_seed(seed)
    ).images[0]

    image_save_path = os.path.join(args.save_dir, f"result_{seed}.png")
    out.save(image_save_path)
