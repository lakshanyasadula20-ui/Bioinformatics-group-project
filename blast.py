from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML
sequence_data = """>WP_342998355.1 MULTISPECIES: hypothetical protein [Bacteria]
MAYKKKAELEQELAEALQRIAELEAELEAVKNSVHKLKNERNAGRKSKFGNNEKGKIMKL
FLDGKSYRAIAKEMKCSVGLVHKILNEQPKGIDNNPSQPKQL
"""

print("Running BLAST search... this may take a few minutes")
result_handle = NCBIWWW.qblast("blastp", "nr", sequence_data)
with open("blast_results.xml", "w") as out_handle:
    out_handle.write(result_handle.read())

print("BLAST search completed and saved to blast_results.xml")
with open("blast_results.xml") as result_handle:
    blast_records = NCBIXML.parse(result_handle)

    print("\nTop 5 BLAST hits:")
    hit_count = 0

    for blast_record in blast_records:
        for alignment in blast_record.alignments:
            for hsp in alignment.hsps[:1]:  # best HSP per hit
                accession = alignment.hit_id.split("|")[-2] if "|" in alignment.hit_id else alignment.accession

                print("\nAccession:", accession)
                print("Title:", alignment.title)
                print("Length:", alignment.length)
                identity_percent = (hsp.identities / hsp.align_length) * 100
                print(f"Identity: {hsp.identities}/{hsp.align_length} ({identity_percent:.2f}%) Kishan")
                print("E-value:", hsp.expect)

                hit_count += 1
                if hit_count == 5:
                    exit()