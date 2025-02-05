import transformers
model_id = "Qwen/Qwen2.5-3B-Instruct"

pipe = transformers.pipeline(
    "text-generation",
    model=model_id,
    device_map="auto",
)

messages = [
    {"role": "system", "content": "You are a helpful assistant."},
]

while True:
    prompt = input("Prompt: ")

    if prompt == "exit":
        break

    prompt = {"role": "user", "content"c: prompt}
    
    messages.append(prompt)
    outputs = pipe(
        messages,
        max_new_tokens=256,
    )
    outputs = outputs[0]["generated_text"][-1]["content"]
    print("Response: ", outputs)
    outputs = {"role": "assistant", "content": outputs}
    messages.append(outputs)
