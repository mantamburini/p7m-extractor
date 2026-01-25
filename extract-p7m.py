import os
import argparse
import sys

def find_pdf_offset(bytes_data):
    magic = b'%PDF-'
    offset = 0
    while True:
        offset = bytes_data.find(magic, offset)
        if offset == -1:
            return -1
        # Check if it's the start of the PDF
        # In this simple case, we assume the first occurrence is it
        return offset

def extract_pdf_from_p7m(p7m_path, detailed=False):
    try:
        with open(p7m_path, 'rb') as f:
            bytes_data = f.read()
        
        offset = find_pdf_offset(bytes_data)
        if offset == -1:
            if not detailed:
                print(f"NO PDF in {os.path.basename(p7m_path)}")
            return {
                'FileName': os.path.basename(p7m_path),
                'Status': 'No PDF found',
                'OutputFile': None,
                'Size': None
            }
        
        pdf_path = os.path.splitext(p7m_path)[0] + '.pdf'
        with open(pdf_path, 'wb') as f:
            f.write(bytes_data[offset:])
        
        size = os.path.getsize(pdf_path)
        
        if not detailed:
            print(f"OK {os.path.basename(p7m_path)}")
        
        return {
            'FileName': os.path.basename(p7m_path),
            'Status': 'Extracted',
            'OutputFile': pdf_path,
            'Size': size
        }
    except Exception as e:
        if not detailed:
            print(f"ERROR processing {os.path.basename(p7m_path)}: {str(e)}")
        return {
            'FileName': os.path.basename(p7m_path),
            'Status': f'Error: {str(e)}',
            'OutputFile': None,
            'Size': None
        }

def main():
    parser = argparse.ArgumentParser(
        description='Extracts PDF files from P7M containers.',
        epilog='Version: 0.3.0\nAuthor: Marcello Anselmi Tamburini'
    )
    parser.add_argument('path', nargs='?', default=os.getcwd(),
                        help='The directory path to scan for .p7m files. Defaults to the current working directory.')
    parser.add_argument('-r', '--recurse', action='store_true',
                        help='If specified, recursively scans subdirectories for .p7m files.')
    parser.add_argument('-d', '--detailed', action='store_true',
                        help='If specified, provides detailed processing information in tabular format.')
    
    args = parser.parse_args()
    
    if not os.path.isdir(args.path):
        print(f"Error: '{args.path}' is not a valid directory.", file=sys.stderr)
        sys.exit(1)
    
    files = []
    if args.recurse:
        for root, _, filenames in os.walk(args.path):
            for filename in filenames:
                if filename.lower().endswith('.p7m'):
                    files.append(os.path.join(root, filename))
    else:
        for filename in os.listdir(args.path):
            if filename.lower().endswith('.p7m'):
                files.append(os.path.join(args.path, filename))
    
    total_files = len(files)
    if total_files == 0:
        print("No .p7m files found in the specified path.", file=sys.stderr)
        sys.exit(0)
    
    results = []
    for i, file_path in enumerate(files, 1):
        if not args.detailed:
            print(f"Processing {os.path.basename(file_path)} ({i}/{total_files})")
        result = extract_pdf_from_p7m(file_path, args.detailed)
        results.append(result)
    
    if args.detailed:
        # Simple table print
        print("{:<30} {:<15} {:<50} {:<10}".format('FileName', 'Status', 'OutputFile', 'Size'))
        print('-' * 105)
        for res in results:
            output_file = res['OutputFile'] or ''
            size = res['Size'] if res['Size'] is not None else ''
            print("{:<30} {:<15} {:<50} {:<10}".format(res['FileName'], res['Status'], output_file, size))

if __name__ == '__main__':
    main()