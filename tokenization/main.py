import tiktoken
enc = tiktoken.encoding_for_model("gpt-4o")
text = "Hey there !"
tokens = enc.encode(text) # enodes the text
print("Encoded tokens: ",tokens)
decode = enc.decode(tokens) # decodes the text
print("Decoded tokens: ",decode)