# Confluence Scanner

A Python-based vulnerability scanner designed to identify potential exposure to **CVE-2023-22515 (Atlassian Confluence)**.

## Prerequisites

* Python 3.8+
* Git
* Linux (Kali Linux recommended)

## Installation

Clone the repository:

```bash
git clone https://github.com/DavidMurma/confluence_scanner.git
```

Navigate to the project directory:

```bash
cd confluence_scanner
```

Create a virtual environment:

```bash
python3 -m venv venv
```

Activate the virtual environment:

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run a scan using the short URL option:

```bash
python scanner.py -u https://www.target.com
```

or

```bash
./scanner.py -u https://www.target.com
```

Run a scan using the long URL option:

```bash
python scanner.py --url https://www.target.com
```

or

```bash
./scanner.py --url https://www.target.com
```

## Help Menu

Display available options and usage information:

```bash
python scanner.py -h
```

or

```bash
./scanner.py -h
```

## Example

```bash
python scanner.py -u https://example.com
```

## Disclaimer

This tool is intended for educational purposes and authorized security testing only. Do not scan systems without proper authorization.

```
```
