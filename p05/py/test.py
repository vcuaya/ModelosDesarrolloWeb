import json
jsonString = '{"1": "200px-Panini_SMTCC_156.jpg", "2": "200px-Panini_SMTCC_150.jpg", "3": "200px-Panini_SMTCC_151.jpg", "4": "200px-Panini_SMTCC_146.jpg", "5": "200px-Panini_SMTCC_160.jpg", "6": "200px-Panini_SMTCC_159.jpg", "7": "200px-Panini_SMTCC_155.jpg", "8": "200px-Panini_SMTCC_147.jpg", "9": "200px-Panini_SMTCC_157.jpg", "10": "200px-Panini_SMTCC_149.jpg"}'

# Load JSON string into a dictionary
data = json.loads(jsonString)

# Loop along dictionary keys
for key in data:
    if (key == "1"):
        print(data[key])
