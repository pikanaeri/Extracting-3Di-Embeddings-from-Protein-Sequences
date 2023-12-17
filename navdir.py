import family_embed
def nav_dir(family_cap=-1, prot_cap=-1, File_Name = "phrog_table.tsv"):
  reader = open(File_Name, "r")
  labels = reader.readline().strip().split("\t")
  writer = open("output_dir", "w")
  writer.write("file_name\tnumber\tcolor\tannotation\tcategory")
  cnt = 0
  while True: 
    line = reader.readline()
    if line == '':
      break
    information = line.strip().split("\t") #array of file information, number followed by color followed by annotation followed by category
    phrog_file = "phrog_" + information[0]
    family_embed.embed_family(phrog_file, max_prot=prot_cap)
    writer.write(phrog_file + "\t" + information[0] + "\t" + information[1] + "\t" + information[2] + "\t" + information[3])
    cnt++
    if family_cap != -1 and cnt >= family_cap:
      break
    writer.close()
    reader.close()


#nav_dir()
