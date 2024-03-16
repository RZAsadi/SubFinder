# Subdomain Enumeration Tool

This Python script is designed to enumerate subdomains for a given domain using various services. It leverages the sublist3r library along with requests, BeautifulSoup, and multiprocessing to efficiently gather subdomain information.

## Features

- **Multi-Service Support**: Utilizes sublist3r and crt.sh services to collect subdomains.
- **Parallel Processing**: Employs multiprocessing for faster execution.
- **Output to File**: Saves the obtained subdomains in a text file for further analysis.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/RZAsadi/SubFinder.git
```

2. Navigate to the directory containing the script:

```bash
cd SubFinder
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

1. Run the script:

```bash
python main.py
```

3. Enter the domain name when prompted.

4. Wait for the script to finish. The subdomains will be saved to a file named `<domain>.txt`.

## Example

```bash
python main.py
```

```
Enter Domain Name: example.com

↳ Loading(OOOO)
<================RESULT================>
subdomain1.example.com
subdomain2.example.com
...
```

## Note

- Ensure proper permissions for multiprocessing on your system.
- Use responsibly and ethically. Unauthorized scanning of systems may violate terms of service and laws.

## Contributors

- [Reza Asadi](https://github.com/RZAsadi)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.