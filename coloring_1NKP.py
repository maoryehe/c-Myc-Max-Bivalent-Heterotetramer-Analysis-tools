from pymol import cmd

# Load your CIF file
file_path = input("Please enter the file path: ")
cmd.load(file_path)

# Select and color the first two MYC proteins in cyan
cmd.select("myc_protein_1", "chain A")  # Modify this selection according to your structure
cmd.select("myc_protein_2", "chain B")  # Modify this selection according to your structure
cmd.color("cyan", "myc_protein_1")
cmd.color("cyan", "myc_protein_2")

# Select and color the next two MAX proteins in gray
cmd.select("max_protein_1", "chain C")  # Modify this selection according to your structure
cmd.select("max_protein_2", "chain D")  # Modify this selection according to your structure
cmd.color("gray", "max_protein_1")
cmd.color("gray", "max_protein_2")

# Select and display the DNA in stick form
cmd.select("ssDNA_1", "chain E")  # Modify this selection according to your structure
cmd.select("ssDNA_2", "chain F")  # Modify this selection according to your structure
cmd.show("sticks", "ssDNA_1")
cmd.show("sticks", "ssDNA_2")

# Optionally, zoom on the structure
cmd.zoom()
