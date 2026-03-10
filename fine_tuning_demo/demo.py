# This is a copied version of the project which is executed on google colab
# you may need to do some configurations before starting it.

# (1) !pip install transformers
# (2) create a hugging face token
HF_TOKEN = "xyz"

import os
os.environ["HF_TOKEN"] = HF_TOKEN

import torch
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

from transformers import AutoTokenizer, AutoModelForCausalLM
model_name = "google/gemma-3-1b-it" # get it from hugging face

# creating tokenizer to tokenize
tokenizer = AutoTokenizer.from_pretrained(model_name)

tokenizer("Hello World")
# sample output
# {'input_ids': [2, 9259, 4109], 'attention_mask': [1, 1, 1]}

input_conversation = [
    {"role":"user","content":"Which is the best place to learn GenAI"},
    {"role":"assistant","content":"The best place to learn GenAI is"},
]

input_detokens = tokenizer.apply_chat_template(
    conversation = input_conversation,
    tokenize = False,
    continue_final_message = True
)
print(input_detokens)

# chat ML based on tokenization
input_tokens = tokenizer.apply_chat_template(conversation = input_conversation).to(device)

output_label = "GenAI Cohort by limbachiya and Bow Bow"
full_conversation = input_detokens + output_label + tokenizer.eos_token
print(full_conversation)

# start of actual fine tuning
input_tokenized = tokenizer(full_conversation, return_tensors="pt", add_special_tokens=False).to(device)["input_ids"]
print(input_tokenized)

input_tokenized = tokenizer(full_conversation, return_tensors="pt", add_special_tokens=False).to(device)["input_ids"]
print(input_tokenized)

# loss function
import torch.nn as nn
def calculate_loss(logits,labels):
  loss_fn = nn.CrossEntropyLoss(reduction="none")
  cross_entropy = loss_fn(logits.view(-1,logits.shape[-1]),labels.view(-1))
  return cross_entropy

# importing model
import torch
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.bfloat16
).to(device)

from torch.optim import AdamW
model.train()
optimizer = AdamW(model.parameters(),lr=3e-5,weight_decay=0.01)

# model training 
for _ in range(10):
  out = model(input_ids = input_ids)
  loss = calculate_loss(out.logits,target_ids).mean()
  loss.backward()
  optimizer.step()
  optimizer.zero_grad()
  print(loss.item())

# output
input_prompt = [
    {"role":"user","content":"Which is the best place to learn GenAi"}
]
input_tokens = tokenizer.apply_chat_template(
    conversation = input_prompt,
    return_tensors="pt",
    tokenize = True,
).to(device)

output = model.generate(input_ids=input_tokens["input_ids"],max_new_tokens=25)
print(tokenizer.batch_decode(output,skip_special_tokens=True))