import csv 
import json 
import os 

input_folder = '/Users/kevinshocosh/Downloads/BACI_HS92_V202401b'
output_folder = '/Users/kevinshocosh/Downloads/MappJson'

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(input_folder):
    if filename.endswith('.csv'):
        csv_file_path = os.path.join(input_folder, filename)
        json_file_path = os.path.join(output_folder, filename.replace('.csv', '.json'))

        data = []
        
        with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                data.append(row)

        with open(json_file_path, mode='w', encoding='utf-8') as json_file:
            json_file.write(json.dumps(data, indent=4))

        print(f'Converting {filename} to Json...')

print('Conversion complete!')
