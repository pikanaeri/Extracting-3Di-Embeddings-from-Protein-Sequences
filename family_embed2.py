import pickle as pkl
def embed_family(File_Name, max_prot=10):
  reader = open(File_Name + ".faa", "r")
  sequence_examples = []
  sequence_names = []
  num_proteins = 0
  while True:
    name = reader.readline().strip()
    if name == '':
      break 
    name = name.replace('>', '') 
    sequence = reader.readline().strip() 
    sequence = sequence.replace('-', 'X')
    sequence_names.append(name)
    sequence_examples.append(sequence)
    num_proteins = num_proteins + 1
    if max_prot != -1 and num_proteins >= max_prot:
      break
  reader.close() 
  sequence_examples = [" ".join(list(re.sub("[UZOB]", "X", sequence))) for sequence in sequence_examples] 
  ids = tokenizer.batch_encode_plus(sequence_examples, add_special_tokens=True, padding="longest")
  input_ids = torch.tensor(ids['input_ids']).to(device)
  attention_mask = torch.tensor(ids['attention_mask']).to(device)
  with torch.no_grad():
      embedding_repr = model(input_ids=input_ids,attention_mask=attention_mask) 
  final_embedding = []
  for id in range(num_proteins): 
    emb = embedding_repr.last_hidden_state[id, :len(sequence_examples[id])]
    emb = emb.mean(dim=0)
    emb = emb.cpu().numpy()
    if len(final_embedding) == 0:
      final_embedding = emb
    else: 
      final_embedding = (final_embedding + emb)/2
  outp_dir = File_Name + ".pkl"
  with open(outp_dir, 'wb') as f:
    pkl.dump(final_embedding, f)
