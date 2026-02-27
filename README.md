<a id="readme-top"></a>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![project_license][license-shield]][license-url]



<div align="center">
  <h3 align="center">p7m-extractor</h3>

  <p align="center">
    Scripts to extract original documents from .P7M signed files.
    <br />
    <br />
    <a href="https://github.com/mantamburini/p7m-extractor/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    ·
    <a href="https://github.com/mantamburini/p7m-extractor/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
  </p>
</div>



<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#about-the-project">About The Project</a></li>
    <li><a href="#features">Features</a></li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



## About The Project

These scripts scan a specified directory for .P7M files (digitally signed containers) and extract the embedded PDF documents. They identify the PDF header within the P7M file and save the extracted content as a new PDF file.

Available implementations:
- **PowerShell** (`Extract-P7M.ps1`) - Windows-native solution
- **Python** (`extract-p7m.py`) - Cross-platform solution

<p align="right">(<a href="#readme-top">back to top</a>)</p>



## Features

- Extracts PDF files from P7M containers
- Supports recursive directory scanning
- Provides progress indication during processing
- Offers detailed mode with tabular output
- Validates input directory paths
- Includes comprehensive error handling with colored output

<p align="right">(<a href="#readme-top">back to top</a>)</p>



## Getting Started

### Prerequisites

#### PowerShell Version
- Windows PowerShell 5.1 or later
- Execution policy allowing script execution (e.g., RemoteSigned)

#### Python Version
- Python 3.6 or later
- No additional dependencies required

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/mantamburini/p7m-extractor.git
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



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

---

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

---

### Output

#### PowerShell Version
- Without `-Detailed`: Displays colored "OK <filename>" (green) for successful extractions, warnings for files without PDFs, or red error messages for processing failures.
- With `-Detailed`: Outputs a table with columns: FileName, Status, OutputFile, Size. Exits early if no .p7m files are found.

#### Python Version
- Without `-d`: Displays "OK <filename>" for successful extractions, "NO PDF <filename>" for files without PDFs, or error messages for processing failures.
- With `-d`: Outputs a table with columns: FileName, Status, OutputFile, Size. Exits early if no .p7m files are found.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



## Roadmap

See the [open issues](https://github.com/mantamburini/p7m-extractor/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



## License

Distributed under the GPL-3.0 License. See `LICENSE` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



## Contact

Marcello Anselmi Tamburini

Project Link: [https://github.com/mantamburini/p7m-extractor](https://github.com/mantamburini/p7m-extractor)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
[contributors-shield]: https://img.shields.io/github/contributors/mantamburini/p7m-extractor.svg?style=for-the-badge
[contributors-url]: https://github.com/mantamburini/p7m-extractor/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/mantamburini/p7m-extractor.svg?style=for-the-badge
[forks-url]: https://github.com/mantamburini/p7m-extractor/network/members
[stars-shield]: https://img.shields.io/github/stars/mantamburini/p7m-extractor.svg?style=for-the-badge
[stars-url]: https://github.com/mantamburini/p7m-extractor/stargazers
[issues-shield]: https://img.shields.io/github/issues/mantamburini/p7m-extractor.svg?style=for-the-badge
[issues-url]: https://github.com/mantamburini/p7m-extractor/issues
[license-shield]: https://img.shields.io/github/license/mantamburini/p7m-extractor.svg?style=for-the-badge
[license-url]: https://github.com/mantamburini/p7m-extractor/blob/main/LICENSE
