from Bio import SeqIO
from collections import Counter

inp = r"C:\Users\varap\Downloads\protein_analysis\.vscode\sequence (3).fasta"
out = r"C:\\Users\\varap\\Downloads\\protein_analysis\\filtered_protein.fasta"

r = SeqIO.read(inp, "fasta")
x = Counter(str(r.seq)).get("X", 0) * 100 / len(r.seq)

if len(r.seq) >= 100 and x <= 5:
    SeqIO.write(r, out, "fasta")
    print("Accepted. File saved at:", out)
else:
    print("Rejected.")
