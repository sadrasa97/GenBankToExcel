
---

# GenBank to Excel Converter

This Python script converts GenBank files (.gb) to an Excel dataset, extracting sequence information such as sequence ID, description, and sequence data. The script also includes a VERSION column that can be customized. It is designed to process multiple GenBank files from a specified folder and save the extracted data into an Excel file.

## Features

- Converts multiple GenBank files in a folder to a single Excel file.
- Extracts sequence ID, description, and sequence from GenBank records.
- Adds a customizable `VERSION` column for each sequence.
- Saves the results as an Excel file, with sequence IDs set as the index.

## Requirements

- Python 3.x
- Biopython (`Bio` module)
- Pandas
- `openpyxl` (for saving the Excel file)

You can install the required libraries using pip:

```bash
pip install biopython pandas openpyxl
```

## Usage

1. **Download or clone this repository** to your local machine.

2. **Place your GenBank (.gb) files** in a folder. For example, place them in a folder called `genbank_files/`.

3. **Customize the script** by setting the following parameters:

   - `input_folder`: Path to the folder containing your GenBank files.
   - `output_file`: The path and name of the output Excel file (e.g., `output_sequences.xlsx`).
   - `version_value`: The value to use for the `VERSION` column (default is "MF356498").

4. **Run the script** by executing it in your terminal:

   ```bash
   python gb_to_excel.py
   ```

The script will process all GenBank files in the specified folder and save the results in an Excel file at the provided output path.

### Example

```python
input_folder = r"C:\path\to\genbank_files"  # Replace with your folder path
output_file = "sequence_data.xlsx"          # Output file name
gb_to_excel(input_folder, output_file)
```

This will create an Excel file named `sequence_data.xlsx` in the current working directory.

## Output Format

The generated Excel file will have the following columns:

- **ID**: Sequence identifier (e.g., accession number).
- **VERSION**: The version value provided in the script (default is "MF356498").
- **Description**: The description of the sequence.
- **Sequence**: The nucleotide sequence as a string.



