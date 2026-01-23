# p7m-extractor

PowerShell Script to extract original documents from .P7M signed files.

## Description

This PowerShell script scans a specified directory for .P7M files (digitally signed containers) and extracts the embedded PDF documents. It identifies the PDF header within the P7M file and saves the extracted content as a new PDF file.

## Features

- Extracts PDF files from P7M containers
- Supports recursive directory scanning
- Provides progress indication during processing
- Offers verbose mode with detailed tabular output
- Validates input directory paths

## Requirements

- Windows PowerShell 5.1 or later
- Execution policy allowing script execution (e.g., RemoteSigned)

## Usage

```powershell
.\Extract-P7M.ps1 [-Path <String>] [-Recurse] [-Verbose]
```

### Parameters

- **-Path** `<String>`  
  The directory path to scan for .P7M files. Defaults to the script's directory. Must be a valid container path.

- **-Recurse** `<Switch>`  
  If specified, recursively scans subdirectories for .P7M files.

- **-Verbose** `<Switch>`  
  If specified, provides detailed processing information in tabular format instead of simple console messages.

### Examples

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

4. Extract PDFs with verbose tabular output:  

   ```powershell
   .\Extract-P7M.ps1 -Path "C:\MyDocuments" -Verbose
   ```

### Output

- Without `-Verbose`: Displays "OK <filename>" for successful extractions or warnings for files without PDFs.
- With `-Verbose`: Outputs a table with columns: FileName, Status, OutputFile, Size.

## Changelog

- **0.2.0** - Added -Verbose parameter for tabular output.
- **0.1.0** - Initial release.

## Author

Marcello Anselmi Tamburini

## License

This project is licensed under the GPL-3.0 License - see the [LICENSE](LICENSE) file for details.
