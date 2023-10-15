# Read the FASTA file and store sequences in a dictionary 

fasta_file = "copy path to the file" 

sequences = {} 

current_sequence = "" 

with open(fasta_file, "r") as f: 

    for line in f: 

        if line.startswith(">"): 

            current_sequence = line.strip() 

            sequences[current_sequence] = "" 

        else: 

            sequences[current_sequence] += line.strip() 

 
 

# Shuffle the sequences randomly 

sequence_keys = list(sequences.keys()) 

random.shuffle(sequence_keys) 

 
 

# Write the shuffled sequences back to the same FASTA file 

with open(fasta_file, "w") as f: 

    for seq_id in sequence_keys: 

        f.write(seq_id + "\n") 

        f.write(sequences[seq_id] + "\n") 

 
 

print("Sequences shuffled randomly and saved back to", fasta_file) 