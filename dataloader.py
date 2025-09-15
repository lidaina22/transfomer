# import tiktoken
# from demo import GPTDatasetV1
# from torch.utils.data import DataLoader
#
# def create_dataloader(txt, batch_size=4, max_length=256, stride=128, shuffle=True, drop_last=True, num_workers=0):
#     tokenizer = tiktoken.get_encoding("gpt2")
#     dataset = GPTDatasetV1(txt, tokenizer, max_length, stride)
#     dataloader = DataLoader(dataset, batch_size, shuffle, drop_last, num_workers)
#     return dataloader
#
#
#
# file_path = "/Users/lidaina/PycharmProjects/Transfomer/demo/demotext.txt"
#
# with open(file_path, "r", encoding="utf-8") as f:
#     raw_text = f.read()
#
# dataloader = create_dataloader(raw_text, batch_size=1, max_length=4, stride=1, shuffle=False)
# data_iter = iter(dataloader)
# first_batch = next(data_iter)
# print(first_batch)