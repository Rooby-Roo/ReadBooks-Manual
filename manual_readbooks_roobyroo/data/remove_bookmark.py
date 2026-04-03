import json

# Load the locations.json file
try:
    with open('manual_stable_20241119/manual_readbooks_roobyroo/data/locations.json', 'r') as file:
        locations = json.load(file)
    print("File loaded successfully.")
except Exception as e:
    print(f"Error loading file: {e}")

# Update the category field for all items
for item in locations:
    if "category" in item and "Bookmark" in item["category"]:
        print(f"Updating item: {item['name']}")
        item["category"] = [cat for cat in item["category"] if cat != "Bookmark"]

# Save the updated locations.json file
try:
    with open('manual_stable_20241119/manual_readbooks_roobyroo/data/locations.json', 'w') as file:
        json.dump(locations, file, indent=2)
    print("File saved successfully.")
except Exception as e:
    print(f"Error saving file: {e}")