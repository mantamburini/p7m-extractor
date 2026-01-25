# p7m-extractor

Scripts to extract original documents from .P7M signed files.

## Description

These scripts scan a specified directory for .P7M files (digitally signed containers) and extract the embedded PDF documents. They identify the PDF header within the P7M file and save the extracted content as a new PDF file.

Available implementations:
- **PowerShell** (`Extract-P7M.ps1`) - Windows-native solution
- **Python** (`extract-p7m.py`) - Cross-platform solution

## Features

- Extracts PDF files from P7M containers
- Supports recursive directory scanning
- Provides progress indication during processing
- Offers detailed mode with tabular output
- Validates input directory paths
- Includes comprehensive error handling with colored output

## Requirements

### PowerShell Version
- Windows PowerShell 5.1 or later
- Execution policy allowing script execution (e.g., RemoteSigned)

### Python Version
- Python 3.6 or later
- No additional dependencies required

## Usage

### PowerShell Script

```powershell
.\Extract-P7M.ps1 [-Path <String>] [-Recurse] [-Detailed]
```

#### Parameters

- **-Path** `<String>`  
  The directory path to scan for .P7M files. Defaults to the current working directory. Must be a valid container path.

- **-Recurse** `<Switch>`  
  If specified, recursively scans subdirectories for .P7m files.

- **-Detailed** `<Switch>`  
  If specified, provides detailed processing information in tabular format instead of simple console messages.

#### Examples

1. Extract PDFs from P7M files in the current directory:  

   ```powershell
   .\Extract-P7M.ps1
   ```

2. Extract PDFs from a specific directory:  

   ```powershell
   .\Extract-P7M.ps1 -Path "C:\MyDocuments"
   ```

3. Extract PDFs recursively from a directory:  

   ```powershell
   .\Extract-P7M.ps1 -Path "C:\MyDocuments" -Recurse
   ```

4. Extract PDFs with detailed tabular output:  

   ```powershell
   .\Extract-P7M.ps1 -Path "C:\MyDocuments" -Detailed
   ```

### Python Script

```bash
python extract-p7m.py [path] [-r] [-d]
```

#### Parameters

- **path** (optional)  
  The directory path to scan for .P7M files. Defaults to the current working directory.

- **-r, --recurse**  
  If specified, recursively scans subdirectories for .P7M files.

- **-d, --detailed**  
  If specified, provides detailed processing information in tabular format.

#### Examples

1. Extract PDFs from P7M files in the current directory:  

   ```bash
   python extract-p7m.py
   ```

2. Extract PDFs from a specific directory:  

   ```bash
   python extract-p7m.py "/path/to/documents"
   ```

3. Extract PDFs recursively from a directory:  

   ```bash
   python extract-p7m.py "/path/to/documents" -r
   ```

4. Extract PDFs with detailed tabular output:  

   ```bash
   python extract-p7m.py "/path/to/documents" -d
   ```

### Output

#### PowerShell Version
- Without `-Detailed`: Displays colored "OK <filename>" (green) for successful extractions, warnings for files without PDFs, or red error messages for processing failures.
- With `-Detailed`: Outputs a table with columns: FileName, Status, OutputFile, Size. Exits early if no .p7m files are found.

#### Python Version
- Without `-d`: Displays "OK <filename>" for successful extractions, "NO PDF <filename>" for files without PDFs, or error messages for processing failures.
- With `-d`: Outputs a table with columns: FileName, Status, OutputFile, Size. Exits early if no .p7m files are found.

## Changelog

### Python Version
- **0.3.0** - Initial Python release with feature parity to PowerShell version.

### PowerShell Version
- **0.3.0** - Fixed default path behavior to use current working directory instead of script location.
- **0.2.1** - Fixed parameter name conflict (Verbose -> Detailed).
- **0.2.0** - Added detailed output parameter for tabular format.
- **0.1.0** - Initial release.

## Author

Marcello Anselmi Tamburini

## License

This project is licensed under the GPL-3.0 License - see the [LICENSE](LICENSE) file for details.
