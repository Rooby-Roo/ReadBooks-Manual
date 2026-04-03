import json
from typing import Any

locations: list[dict[Any, Any]] = []

for ch in range(1, 10000):
    # Base loc
    loc = {
        "name": f"Finish Chapter {ch}",
        "region": f"Chapter {ch}",
        "category": [f"Chapter {ch}"],
        "requires": []
    }
    locations.append(loc)
    # Bonus loc
    loc = {
        "name": f"Finish Chapter {ch} (Bonus)",
        "region": f"Chapter {ch}",
        "category": [f"Chapter {ch}", "Bonus Location"],
        "requires": []
    }
    locations.append(loc)
    # Bookmark
    loc = {
        "name": f"Bookmark {ch}",
        "region": f"Chapter {ch}",
        "category": [f"Chapter {ch}"],
        "requires": [],
        "place_item": ["Bookmark"]
    }
    locations.append(loc)

try:
    with open('locations.json', 'w') as file:
        json.dump(locations, file, indent=2)
    print("Locations file saved successfully.")
except Exception as e:
    print(f"Error saving file: {e}")

regions: dict[dict[str, Any]] = {}
regions["Chapter 1"] = {
    "connects_to": ["Victory"],
    "requires": []
}
for ch in range(2, 10000):
    reg = {
        "requires": f"|Unlock Chapter:{ch}|"
    }
    regions[f"Chapter {ch}"] = reg
regions["Victory"] = {
    "requires": "|Unlock Chapter:ALL|"
}
try:
    with open('regions.json', 'w') as file:
        json.dump(regions, file, indent=2)
    print("Regions file saved successfully.")
except Exception as e:
    print(f"Error saving file: {e}")