from model import model

results = model('C:\\Users\\Rafli\\cat-detection-project\\WIN_20250105_08_05_17_Pro.mp4')

output_folder = "C:\\Users\\Rafli\\cat-detection-project\\output_results"

# Ensure the folder exists
import os

# Save the results to the specified folder
for i, result in enumerate(results):
    result.save(filename=os.path.join(output_folder, f'frame_{i}'))