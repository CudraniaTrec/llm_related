import torch, os
from transformers import AutoTokenizer, AutoModelForCausalLM

os.environ["CUDA_VISIBLE_DEVICES"] = "0,1"

checkpoint = "bigcode/starcoder2-3b"
tokenizer = AutoTokenizer.from_pretrained(checkpoint, use_fast=True, local_files_only=True)
# for fp16 use `torch_dtype=torch.float16` instead
model = AutoModelForCausalLM.from_pretrained(checkpoint, 
                                             device_map="auto",
                                             local_files_only=True, 
                                             torch_dtype=torch.bfloat16)

print("="*20+"test starcoder"+"="*20)
input_string ="""
    # Complete the following task in Python. 
    # Write a function to find the n largest integers from a given list of numbers, returned in descending order.
    # Please respond with code only, no explanation, no example IO, no annotations.
    # Your code should be able to pass the following test cases.
    # assert heap_queue_largest( [25, 35, 22, 85, 14, 65, 75, 22, 58],3)==[85, 75, 65]
    # assert heap_queue_largest( [25, 35, 22, 85, 14, 65, 75, 22, 58],5)==[85, 75, 65, 58, 35]
    def
    """
inputs = tokenizer.encode(input_string, return_tensors="pt").to("cuda")
outputs = model.generate(inputs, 
                         pad_token_id=tokenizer.eos_token_id,
                         attention_mask=torch.ones_like(inputs), 
                         early_stopping=True,
                         max_length=500)
print(tokenizer.decode(outputs[0]))
print(f"Memory footprint: {model.get_memory_footprint() / 1e6:.2f} MB")
print("="*50)

# from utils import codegen_direct
# codegen_direct(model="starcoder-3b", dataset="humaneval")
