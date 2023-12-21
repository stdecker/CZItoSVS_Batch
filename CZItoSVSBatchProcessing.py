# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 12:19:09 2023

@author: u1159489
"""

import os
import logging
import slideio

# Logging setup
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")

# Conversion parameters: selection of SVSJpegParameters as a parameter defines JPEG compression
params = slideio.SVSJp2KParameters()
#params.quality = 100  # compression quality: this is the maximum

# Function to convert a single .czi file to .svs
def convert_czi_to_svs(czi_path, output_dir):
    slide_czi = slideio.open_slide(czi_path)
#    num_scenes = slide_czi.num_scenes

    logging.info(f"Converting .czi file: {czi_path}")

#    for scene_index in int(1):         #IF YOU WANT TO CONVERT MULTIPLE SCENES, ALSO NEED TO INDENT LINES 28-32
    scene_index = 1                     #IF YOU WANT TO CONVERT ONLY ONE SCENE
    scene = slide_czi.get_scene(scene_index)
    output_filename = os.path.join(output_dir, f"{os.path.basename(czi_path)}-Scene_{scene_index}.svs")
    logging.info(f"Processing scene {scene_index}...")
    slideio.convert_scene(scene, params, output_filename)
    logging.info(f"Scene {scene_index} converted successfully!")

#    slide_czi.close()                  #IF YOU WANT TO CONVERT MULTIPLE SCENES

# Specify the directory containing .czi files
czi_dir = r"C:\Users\u1159489\Box\FunaiLab\Data\IRI\Imaging\IRI\H&E\Batch1"

# Specify the output directory for .svs files
svs_dir = r"C:\Users\u1159489\Box\FunaiLab\Data\IRI\Imaging\Converted"

# Create the output directory if it doesn't exist
os.makedirs(svs_dir, exist_ok=True)

# Loop through all .czi files in the directory
for filename in os.listdir(czi_dir):
    if filename.endswith(".czi"):
        czi_path = os.path.join(czi_dir, filename)
        convert_czi_to_svs(czi_path, svs_dir)

logging.info(f"Successfully converted all .czi files in '{czi_dir}' to .svs files in '{svs_dir}'")


