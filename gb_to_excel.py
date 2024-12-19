from Bio import SeqIO
import pandas as pd
import os

def gb_to_excel(input_folder, output_file, version_value="MF356498"):
    """
    Convert GenBank files to an Excel dataset with sequences, adding a VERSION column.
    
    Parameters:
    input_folder (str): Path to the folder containing .gb files.
    output_file (str): Path to save the resulting Excel file.
    version_value (str): The value to set for the VERSION column (default: "MF356498").
    """
    data = []

    for file in os.listdir(input_folder):
        if file.endswith(".gb"):
            filepath = os.path.join(input_folder, file)
            
            for record in SeqIO.parse(filepath, "genbank"):
                seq_id = record.id
                description = record.description
                sequence = str(record.seq)
                data.append({
                    "ID": seq_id,
                    "VERSION": version_value,
                    "Description": description,
                    "Sequence": sequence
                })
    
    df = pd.DataFrame(data)

    df.set_index("ID", inplace=True)

    df.to_excel(output_file)
    print(f"Dataset saved to {output_file}")

input_folder = r"C:\Users\RayanSabz\Downloads\pave.niaid.nih.govGenomes" 
output_file = "sequence.xlsx"  
gb_to_excel(input_folder, output_file)
