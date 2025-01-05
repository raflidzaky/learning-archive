from model import model

results = model('LOCAL-VIDEO')

output_folder = "OUTPUT-FOLDER"

# Ensure the folder exists
import os

# Save the results to the specified folder
for i, result in enumerate(results):
    result.save(filename=os.path.join(output_folder, f'frame_{i}'))

# THIS FILE IS NOT IN USE 
# Since what I need is real-video labelling, not per-frame labelling
# Focus on test_in_camera.py instead
