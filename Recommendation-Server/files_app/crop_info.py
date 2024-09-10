# Example data
# Complete data will be made available upon request

crop_infos = {
  "Rice": {
    "soil": ["Alluvial Soil", "Laterite Soil", "Red Soil", "Black Soil", "Yellow Soil"],
    "season": "Kharif",
    "Temperature": "15 - 37",
    "ph": "5.5 - 7.0",
    "Rainfall": "100 - 250",
    "Humidity": "60 - 75",
    "N": "High",
    "P": "Medium",
    "K": "Medium - High",
    "other": "None"
  }
}

def crop_info_details(crop):
  return crop_infos.get(crop, 'None')