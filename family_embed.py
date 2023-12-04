#Family Embedding Function
#Pass in the fasta file name, will write the resulting averaged embedding to a .pkl file

import pickle as pkl

def embed_family(File_Name, max_prot=10): 
  reader = open(File_Name + ".faa", "r")
  sequence_examples = []
  sequence_names = []
  num_proteins = 0

  while True:
    name = reader.readline().strip()
    if name == '':
      break #end of file reached
    name = name.replace('>', '') #replacing the '>' characters
    sequence = reader.readline().strip() #reading the sequence
    sequence = sequence.replace('-', 'X') #replacing skipped or unknown amino acids with 'X'
    sequence_names.append(name)
    sequence_examples.append(sequence)
    num_proteins = num_proteins + 1
    if num_proteins >= max_prot:
      #print("---capped protein sequences at ", str(max_prot))
      break

  reader.close()
  #print("done extracting", str(num_proteins), "proteins")

  # this will replace all rare/ambiguous amino acids by X and introduce white-space between all amino acids
  sequence_examples = [" ".join(list(re.sub("[UZOB]", "X", sequence))) for sequence in sequence_examples]

  # tokenize sequences and pad up to the longest sequence in the batch
  ids = tokenizer.batch_encode_plus(sequence_examples, add_special_tokens=True, padding="longest")
  input_ids = torch.tensor(ids['input_ids']).to(device)
  attention_mask = torch.tensor(ids['attention_mask']).to(device)

  # generate embeddings
  with torch.no_grad():
      embedding_repr = model(input_ids=input_ids,attention_mask=attention_mask)

  #print("Generating embedding: ")
  final_embedding = []
  for id in range(num_proteins): #0, 1, ... num_proteins-1
    emb = embedding_repr.last_hidden_state[id, :len(sequence_examples[id])]
    emb = emb.mean(dim=0)
    emb = emb.cpu().numpy()
    if len(final_embedding) == 0:
      final_embedding = emb
    else: #average the embeddings
      final_embedding = (final_embedding + emb)/2
  #print(final_embedding)

  outp_dir = File_Name + ".pkl"
  with open(outp_dir, 'wb') as f:
    pkl.dump(final_embedding, f)
