from utils import load_model, generate
model, tokenizer = load_model()
initial_script = '''...'''
max_length = 100
# It is recommended to use max_length between 50 and 1000.
# The higher you go, more it will take to process.
final_script = generate(
    model,
    tokenizer,
    input_text=initial_script,
    max_length=max_length
    )[0]
print(final_script)
