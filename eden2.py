import requests
import pandas as pd

# Your API key (replace with your actual API key)
api_key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiNGI2MTNlYWQtNjM4Ni00Y2FjLWFlYTctY2QwOTEyODBmZjdhIiwidHlwZSI6ImFwaV90b2tlbiJ9.49f5_0ZfmIbCaYAnjVTUK3mUiVXpmN8UeN4aAARRcss"

# Set up the headers with the API key
headers = {"Authorization": f"Bearer {api_key}"}

# URL for the EdenAI multimodal chat endpoint
url = "https://api.edenai.run/v2/multimodal/chat"

output_file = "edible_plants_new.xlsx"

try:
    # Attempt to load existing data into DataFrame
    existing_data = pd.read_excel(output_file, sheet_name='Sheet1')
    print(f"Loaded existing data from {output_file}")
except FileNotFoundError:
    print(f"File {output_file} not found. You will need to fetch data from API first.")
    existing_data = pd.DataFrame()

def get_plant_description(common_name):
    # Payload to send to the API with dynamic common_name
    payload = {
        "providers": ["openai/gpt-4o-mini"],
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "content": {
                            "text": (
                                f"Provide a detailed description for the plant {common_name} in given FORMAT:\n"
                                "SAPLING DESCRIPTION:\n"
                                "Number of saplings in a net pot -\n"
                                "Sapling Height –\n"
                                "Watering – (like for example: when the top layer of the soil feels dry)\n"
                                "Sunlight – (like for example: bright indirect sunlight)\n"
                                "PLANT DESCRIPTION:\n"
                                "Difficulty Level –\n"
                                "Full Plant Height –\n"
                                "Leaves Color –\n"
                                "Type – ( indoors, terrace, or semi-shade areas)\n"
                                "Feed – (example:--Vermicompost for nutrients every week, Seaweed once a month for greener leaves, and Epsom salt for better blooming once a month)\n"
                                "Watering – (example:--water whenever the top layer of the soil feels dry)\n"
                                "Soil – (example:-- well-draining or porous soil etc)\n"
                                "Sunlight – (example:--bright indirect sunlight)\n"
                                "Suitable Temperature – (example:--60°F(15.56 °C))\n"
                                "HOW TO PLANT A SAPLING:\n"
                                "5 steps"
                            )
                        }
                    }
                ]
            }
        ]
    }

    # Make the POST request to the API
    response = requests.post(url, json=payload, headers=headers)
    
    # If the request was successful, get the generated text
    if response.status_code == 200:
        generated_text = response.json().get('openai/gpt-4o-mini', {}).get('generated_text', '')
        return generated_text
    else:
        print(f"Error fetching data for {common_name}: {response.status_code}")
        return "No description available"

if not existing_data.empty:
    # Add extra plant details for a specific range of rows (for example, first 5 rows)
    existing_data["Sapling Description"] = existing_data["Common Name"].iloc[:100].apply(get_plant_description)


    try:
    # Save updated data back to Excel (ensure headers are written)
            with pd.ExcelWriter(output_file, engine='openpyxl', mode='a', if_sheet_exists='overlay') as writer:
                existing_data.to_excel(writer, index=False, header=True, sheet_name='Sheet1')
            print(f"Data updated and saved back to {output_file}")
    except Exception as e:
                print(f"Error saving data to {output_file}: {e}")
else:
    print("No data to update from the Excel file.")
