file_path = r"C:\Users\varap\Downloads\protein_analysis\.vscode\sequence (3).fasta"   
output_file = "output.txt"   

with open(file_path, "r") as f:
    lines = f.readlines()

header = lines[0].strip()
sequence = "".join(line.strip() for line in lines[1:]).upper()

gc = (sequence.count("G") + sequence.count("C")) / len(sequence) * 100

freq = {}
for base in sequence:
    freq[base] = freq.get(base, 0) + 1

with open(output_file, "w") as out:
    out.write(f"FASTA Header: {header}\n")
    out.write(f"Sequence Length: {len(sequence)}\n")
    out.write(f"GC Content: {gc:.2f}%\n\n")
    out.write("Nucleotide Frequency:\n")
    for k, v in freq.items():
        out.write(f"{k} : {v}\n")

print(" Analysis complete! Check output.txt for results")