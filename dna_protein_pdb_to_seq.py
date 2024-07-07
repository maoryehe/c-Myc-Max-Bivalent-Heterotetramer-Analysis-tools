from Bio import PDB
from Bio.SeqUtils import seq1

def extract_sequences(pdb_file):
    parser = PDB.PDBParser(QUIET=True)
    structure = parser.get_structure('structure', pdb_file)
    
    protein_sequences = {}
    dna_sequences = {}
    
    protein_count = 1
    dna_count = 1
    
    for model in structure:
        for chain in model:
            seq_protein = ""
            seq_dna = ""
            for residue in chain:
                # Check if the residue is an amino acid
                if PDB.is_aa(residue):
                    seq_protein += seq1(residue.resname)
                # Check if the residue is a nucleotide
                elif residue.resname in ['DA', 'DT', 'DC', 'DG', 'A', 'T', 'C', 'G']:
                    if residue.resname in ['DA', 'A']:
                        seq_dna += 'A'
                    elif residue.resname in ['DT', 'T']:
                        seq_dna += 'T'
                    elif residue.resname in ['DC', 'C']:
                        seq_dna += 'C'
                    elif residue.resname in ['DG', 'G']:
                        seq_dna += 'G'
            
            if seq_protein:
                protein_sequences[f'protein{protein_count} (chain {chain.id})'] = seq_protein
                protein_count += 1
            if seq_dna:
                dna_sequences[f'dna{dna_count} (chain {chain.id})'] = seq_dna
                dna_count += 1
    
    return protein_sequences, dna_sequences

# Example usage
pdb_file = input("Enter the pdb file: ")  # Replace with your PDB file path
protein_sequences, dna_sequences = extract_sequences(pdb_file)

print("Protein Sequences:")
for label, seq in protein_sequences.items():
    print(f"{label}: {seq}")

print("\nDNA Sequences:")
for label, seq in dna_sequences.items():
    print(f"{label}: {seq}")

