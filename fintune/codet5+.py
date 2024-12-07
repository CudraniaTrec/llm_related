import torch, os
from transformers import AutoTokenizer, AutoModelForCausalLM, AutoModelForSeq2SeqLM
from transformers import CodeGenTokenizer, T5ForConditionalGeneration, T5Config

os.environ["CUDA_VISIBLE_DEVICES"] = "0,1"

checkpoint = "Salesforce/codet5p-6b"
tokenizer = CodeGenTokenizer.from_pretrained(checkpoint, use_fast=True, local_files_only=True)
# for fp16 use `torch_dtype=torch.float16` instead
model = AutoModelForSeq2SeqLM.from_pretrained(checkpoint, 
                                             device_map="auto",
                                             local_files_only=True, 
                                             trust_remote_code=True,
                                             torch_dtype=torch.bfloat16)

print("="*20+"test codet5+"+"="*20)
input_string = """
# Complete the following task in Python. 
# Write a function to find the shared elements from the given two lists.
# Please respond with code only, no explanation, no example IO, no annotations.
# Your code should be able to pass the following test cases.
# assert set(similar_elements((3, 4, 5, 6),(5, 7, 4, 10))) == set((4, 5))
# assert set(similar_elements((1, 2, 3, 4),(5, 4, 3, 7))) == set((3, 4))
# assert set(similar_elements((11, 12, 14, 13),(17, 15, 14, 13))) == set((13, 14))
"""
inputs = tokenizer.encode(input_string, return_tensors="pt").to("cuda")
outputs = model.generate(inputs, 
                         pad_token_id=tokenizer.eos_token_id,
                         attention_mask=torch.ones_like(inputs), 
                         max_length=500)
print(tokenizer.decode(outputs[0]))
print(f"Memory footprint: {model.get_memory_footprint() / 1e6:.2f} MB")
print("="*50)