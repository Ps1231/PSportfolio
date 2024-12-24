from transformers import AutoModelForCausalLM, AutoTokenizer

# Load the GPT-Neo or GPT-J model from Hugging Face
model_name = "EleutherAI/gpt-neo-2.7B"  # You can also use "EleutherAI/gpt-j-6B"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Function to generate responses from the model
def get_gpt_neo_response(prompt):
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(inputs["input_ids"], max_length=150, temperature=0.7, num_return_sequences=1)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response

# Test the function
prompt = "Tell me about the apple plant."
print(get_gpt_neo_response(prompt))
