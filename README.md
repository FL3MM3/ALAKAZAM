# ALAKAZAM - Hash Analyzer

ALAKAZAM is a Python program that analyzes a hash and determines its type among a list of supported hash algorithms including MD5, SHA-1, SHA-256, SHA-512, SHA3-224, and SHA3-384. It provides functionality to analyze a single hash, as well as hashes stored in a file.

## Installation

To install and run the program, follow these steps:

1. **Clone the repository:**
    
    bashCopy code
    
    `git clone https://github.com/FL3MM3/alakazam.git`
    
2. **Navigate to the project directory:**
    
    bashCopy code
    
    `cd alakazam`
    
3. **Install dependencies (Colorama):**
    
    Copy code
    
    `pip install colorama`
    
4. **Run the program:**
    
    cssCopy code
    
    `python alakazam.py [options]`
    

## Usage

The program supports the following command-line options:

- `-h <hash>`: Analyze a single hash.
- `-f <path/to/file>`: Analyze hashes stored in a file separated by ';'.
- `-help`: Display the help message.

Example usage:

- Analyze a single hash:
    
    phpCopy code
    
    `python alakazam.py -h <hash_value>`
    
- Analyze hashes from a file:
    
    bashCopy code
    
    `python alakazam.py -f <path/to/file>`
    
- Display the help message:
    
    bashCopy code
    
    `python alakazam.py -help`
    

## Author

This program is authored by [flem](https://github.com/FL3MM3).

For any issues or suggestions, please open an issue on GitHub.