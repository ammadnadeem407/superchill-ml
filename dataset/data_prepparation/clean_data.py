import json

with open('/dataset/data_creation/story_dataset.json') as f:
    data = json.load(f)

new_data = []

for item in data:
    new_item = {
        'prompt': item['sub_prompt'],
        'completion': item['Completion']
    }
    new_data.append(new_item)

with open('final_story.json', 'w') as f:
    json.dump(new_data, f)
