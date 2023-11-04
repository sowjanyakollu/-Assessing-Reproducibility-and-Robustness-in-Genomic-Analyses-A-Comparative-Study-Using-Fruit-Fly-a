import random

def introduce_substitution_error(read, error_rate):
    """
    Introduce substitution errors in a read.
    """
    bases = ['A', 'C', 'G', 'T']
    error_read = ""
    for base in read:
        if random.random() < error_rate:
            # Randomly select a substitution
            substitute = random.choice([b for b in bases if b != base])
            error_read += substitute
        else:
            error_read += base
    return error_read

# Read the original reads from a FASTA file
fasta_file = "C:/Users/n11233958/Downloads/IFN 646 PROJECT/oneprecenterrortoall/sample_04_1.fasta"
original_reads = {}
current_sequence = ""
with open(fasta_file, "r") as f:
    for line in f:
        if line.startswith(">"):
            current_sequence = line.strip()
            original_reads[current_sequence] = ""
        else:
            original_reads[current_sequence] += line.strip()

error_rate = 0.01  # Adjust this rate to control the error level

# Introduce errors to the selected reads in the same input file
with open(fasta_file, "w") as f:
    for seq_id, read in original_reads.items():
        errored_sequence = introduce_substitution_error(read, error_rate)
        f.write(seq_id + "\n")
        f.write(errored_sequence + "\n")

print("Errored sequences written to", fasta_file)
