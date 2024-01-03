# Load ProtT5 in half-precision (more specifically: the encoder-part of ProtT5-XL-U50), taken from https://github.com/mheinzinger/ProstT5/blob/main/README.md
from transformers import T5Tokenizer, T5EncoderModel
import torch
import re
device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
print("Using device: {}".format(device))
#Load encoder-part of ProstT5 in half-precision. { display-mode: "form" }
#May take a few minutes; run on high RAM to ensure that the runtime does not crash (~5-10 minutes)
transformer_link = "Rostlab/ProstT5"
print("Loading: {}".format(transformer_link))
model = T5EncoderModel.from_pretrained(transformer_link)
model.full() if device=='cpu' else model.half() # only cast to full-precision if no GPU is available
model = model.to(device)
model = model.eval()
tokenizer = T5Tokenizer.from_pretrained(transformer_link, do_lower_case=False )

