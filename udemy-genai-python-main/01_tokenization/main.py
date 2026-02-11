import tiktoken

enc = tiktoken.encoding_for_model("gpt-4o")

text = "Hey There! My name is Nishi Tiwari"
tokens = enc.encode(text)

# [25216, 3274, 0, 3673, 1308, 382, 478, 24597, 353, 18970, 1683]

# Tokens are the numerical representation of text

print("Tokens", tokens)

decoded = enc.decode([25216, 3274, 0, 3673, 1308, 382, 478, 24597, 353, 18970, 1683])
print("Decoded", decoded)