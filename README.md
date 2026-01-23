# p7m-extractor

PowerShell Script to extract original documents from .P7M signed files.

## Description

This PowerShell script scans a specified directory for .P7M files (digitally signed containers) and extracts the embedded PDF documents. It identifies the PDF header within the P7M file and saves the extracted content as a new PDF file.

## Features

- Extracts PDF files from P7M containers
- Supports recursive directory scanning
- Provides progress indication during processing
- Offers detailed mode with tabular output
- Validates input directory paths
- Includes comprehensive error handling with colored output

## Requirements

- Windows PowerShell 5.1 or later
- Execution policy allowing script execution (e.g., RemoteSigned)

## Usage

```powershell
.\Extract-P7M.ps1 [-Path <String>] [-Recurse] [-Detailed]
```

### Parameters

- **-Path** `<String>`  
  The directory path to scan for .P7M files. Defaults to the current working directory. Must be a valid container path.

- **-Recurse** `<Switch>`  
  If specified, recursively scans subdirectories for .P7m files.

- **-Detailed** `<Switch>`  
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

4. Extract PDFs with detailed tabular output:  

   ```powershell
   .\Extract-P7M.ps1 -Path "C:\MyDocuments" -Detailed
   ```

### Output

- Without `-Detailed`: Displays colored "OK <filename>" (green) for successful extractions, warnings for files without PDFs, or red error messages for processing failures.
- With `-Detailed`: Outputs a table with columns: FileName, Status, OutputFile, Size. Exits early if no .p7m files are found.

## Changelog

- **0.3.0** - Fixed default path behavior to use current working directory instead of script location.
- **0.2.1** - Fixed parameter name conflict (Verbose -> Detailed).
- **0.2.0** - Added detailed output parameter for tabular format.
- **0.1.0** - Initial release.

## Author

Marcello Anselmi Tamburini

## License

This project is licensed under the GPL-3.0 License - see the [LICENSE](LICENSE) file for details.
