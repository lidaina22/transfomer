import tiktoken

file_path = "/Users/lidaina/PycharmProjects/Transfomer/demo/the-verdict-test.txt"

with open(file_path, "r", encoding="utf-8") as f:
    raw_text = f.read()

bpeTokenizer = tiktoken.get_encoding("gpt2")

encode_result = bpeTokenizer.encode(raw_text, allowed_special={"<|endoftext|>"})
# print(encode_result)
#
# decode_result = bpeTokenizer.decode(encode_result)
# print(decode_result)
context_size = 4
for i in range(1, context_size+1):
    x = encode_result[:i]
    y = encode_result[i]
    print(bpeTokenizer.decode(x))
    print("---->")
    print(bpeTokenizer.decode(y))



# def create_dataloader_v1(txt, batch_size=4, max_length=256, stride=128,
#                          shuffle=True, drop_last=True, num_workers=0):
#     tokenizer = tiktoken.get_encoding("gpt2")
#     dataset = GPTDatasetV1(txt, tokenizer, max_length, stride)

# 20250915