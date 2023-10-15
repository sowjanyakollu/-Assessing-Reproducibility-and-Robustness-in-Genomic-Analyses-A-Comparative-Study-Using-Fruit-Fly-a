import random

# Function to introduce a 1% error in a read
def introduce_error(read, error_rate=0.01):
    error_count = int(len(read) * error_rate)
    positions = random.sample(range(len(read)), error_count)
    new_read = list(read)
    for position in positions:
        new_read[position] = random.choice("ACGT".replace(read[position], ""))
    return ''.join(new_read)

# Simulate 500 reads and introduce a 1% error in each read
genome = "ATCG" * 1000  # Replace this with your actual genome
read_length = 50
num_reads = 500

reads_with_error = []
for i in range(num_reads):
    start_position = random.randint(0, len(genome) - read_length)
    read = genome[start_position:start_position + read_length]
    read_with_error = introduce_error(read)
    reads_with_error.append(read_with_error)

# Save the reads with errors to a file in FASTA format
output_file = "reads_with_error.fasta"
with open(output_file, "w") as file:
    for i, read in enumerate(reads_with_error):
        header = f">Read_{i + 1}\n"
        file.write(header)
        file.write(read + "\n")

print(f"Reads with errors saved to '{output_file}'")
