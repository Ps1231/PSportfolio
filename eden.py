import requests

# Replace with your API key
api_key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiNGI2MTNlYWQtNjM4Ni00Y2FjLWFlYTctY2QwOTEyODBmZjdhIiwidHlwZSI6ImFwaV90b2tlbiJ9.49f5_0ZfmIbCaYAnjVTUK3mUiVXpmN8UeN4aAARRcss"

# Set up the headers with the API key
headers = {"Authorization": f"Bearer {api_key}"}

# URL for the EdenAI multimodal chat endpoint
url = "https://api.edenai.run/v2/multimodal/chat"

# Payload to send to the API
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
                           "" "Provide a detailed description for the plant apple plant in given FORMAT:\n"
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
                            "Soil – (example:-- well-drainingor porous soil etc)\n"
                            "Sunlight – (example:--bright indirect sunlight)\n"
                            "Suitable Temperature – (example:--60°F(15.56 °C))\n"
                            "HOW TO PLANT A SAPLING:\n"
                            "5 steps"""
                        )
                    }
                }
            ]
        }
    ]
}

# Make the POST request to the API
response = requests.post(url, json=payload, headers=headers)

# Print the JSON response
generated_text = response.json().get('openai/gpt-4o-mini', {}).get('generated_text', '')
print(generated_text)
