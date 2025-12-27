```
▄▄▄▄▄▄         ▄▄                ▄▄                
███▀▀██▄       ██                ██                
███  ███ ▄█▀█▄ ████▄  ▀▀█▄ ▄█▀▀▀ ████▄ ▄█▀█▄ ████▄ 
███  ███ ██▄█▀ ██ ██ ▄█▀██ ▀███▄ ██ ██ ██▄█▀ ██ ▀▀ 
██████▀  ▀█▄▄▄ ██ ██ ▀█▄██ ▄▄▄█▀ ██ ██ ▀█▄▄▄ ██    
          
```

A lightweight, educational hash cracking tool built in Python for password security assessment and recovery operations.

![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)
![Status](https://img.shields.io/badge/status-educational-orange.svg)

## Overview

**Dehasher** is a Python-based hash cracking utility designed for cybersecurity professionals, auditors, and researchers. Leveraging Python's `hashlib` library, it provides a straightforward approach to password strength assessment and plaintext recovery through dictionary-based attacks.

This tool serves as both a practical security utility and an educational resource for understanding hash functions, password security, and offensive security tooling development.

## Presentation

Check out the presentation [here](https://github.com/pdoffl/Dehasher/blob/main/presentation/Dehasher-Presentation.pdf) to understand more about the Dehasher project. 

## Features

- **Password Strength Assessment**: Test hashes against known weak password databases to evaluate organizational password policies and identify vulnerable credentials requiring rotation.
- **Password Recovery**: Recover plaintext passwords from hash values using comprehensive wordlist-based attacks. Useful for legitimate password recovery scenarios and security audits.
- **Multi-Algorithm Support**: Supports all hash algorithms guaranteed by Python's `hashlib` module (MD5, SHA-1, SHA-224, SHA-256, SHA-384, SHA-512 and more)

## Installation

### Prerequisites
- Python 3.x
- Standard Python libraries (included with Python installation)

## Usage

### Basic Syntax

```bash
python3 dehasher.py -H <hash_value> -t <hash_type> -l <wordlist_path>
```

### Arguments

| Flag | Description | Required |
|------|-------------|----------|
| `-H` | Hash value to crack | Yes |
| `-t` | Hash algorithm type (e.g., md5, sha1, sha256) | Yes |
| `-l` | Path to password wordlist file | Yes |

### Examples

**Crack an MD5 hash:**
```bash
python3 dehasher.py -H d8611198ea8421180df8e80eab0f2da1 -t md5 -l rockyou.txt
```

**Crack a SHA-1 hash:**
```bash
python3 dehasher.py -H 5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8 -t sha1 -l common_passwords.txt
```

**Crack a SHA-256 hash:**
```bash
python3 dehasher.py -H 5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8 -t sha256 -l wordlist.txt
```

### Sample Output

**Successful crack:**
```
Perform hash cracking operations for "5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8" hash (sha1 hash) ...

[+] Hash Found - [ password ]
```

**Unsuccessful attempt:**
```
Perform hash cracking operations for "abc123def456..." hash (md5 hash) ...

[-] Hash not found
```

## How It Works

Dehasher employs a dictionary attack methodology:

1. It accepts target hash, algorithm type, and wordlist path.
2. Then it reads wordlist line-by-line and computes hash of each plaintext candidate using specified algorithm
3. Then it compares generated hash against target hash
4. If a match found, the plaintext is reported, or else, the script indicates failure

```python
# Simplified workflow
for password in wordlist:
    candidate_hash = hashlib.new(algorithm).update(password).hexdigest()
    if candidate_hash == target_hash:
        return password  # Match found!
```

## Use Cases

- **Security Auditing**: Assess organizational password strength policies, identify weak credentials in user databases and validate compliance with password complexity requirements
- **Penetration Testing**: Crack captured password hashes during authorized security assessments to demonstrate impact of weak password practices to clients
- **Educational Purpose**: Enables learning how hash function mechanic works and it properties, also helps in understanding password attack vectors and defenses

## Wordlists

Dehasher requires external wordlist files. Common options include:

- **RockYou.txt** - Over million passwords from real breaches
- [**SecLists**](https://github.com/danielmiessler/SecLists) - Curated lists for various scenarios
- [**CrackStation**](https://crackstation.net/crackstation-wordlist-password-cracking-dictionary.htm) - Massive 15GB wordlist
- **Custom lists** - Generate based on target organization

## Limitations

- Success relies on wordlist quality and comprehensiveness
- The script is single-threaded, i.e. sequential processing
- The script cannot handle salted hashes
- Large wordlists may impact performance on resource-limited systems

## Development Roadmap

#### Resume Functionality
- Need to implement a checkpoint system to resume interrupted cracking sessions from last attempted password.
- This would help eliminating redundant work after interruptions, will save time on large wordlists and will improve user experience for long-running jobs.

#### Rainbow Table Integration
- Pre-computing hash-to-plaintext mappings for instant lookups.
- This can dramatically reduce cracking time and enable rapid bulk hash analysis.

#### Multi-threading Support
- Parallelize hash computation across CPU cores.
- This would optimize cracking with reduced time-to-crack.

#### Progress Indicators
- Real-time progress bars and statistics to monitor cracking status.
- This will help in estimating the time elapsed/remaining.

## Technical Details

### Supported Algorithms

You can query supported algorithms programmatically in Python interpreter prompt:

```python
import hashlib
print(hashlib.algorithms_guaranteed)
# Output: {'sha1', 'sha224', 'sha256', 'sha384', 'sha512', 'md5', ...}
```

## Performance Considerations

**Typical performance metrics:**
- **MD5**: ~1-2 million hashes/second (single-threaded)
- **SHA-256**: ~500k-1M hashes/second (single-threaded)
- **SHA-512**: ~300k-800k hashes/second (single-threaded)

*Performance varies based on CPU, wordlist I/O, and Python version.*

## Security & Ethics

### Legal Disclaimer

**This tool is for authorized security testing only.**

- Only use on systems you own or have explicit written permission to test
- Cracking passwords without authorization is illegal under CFAA and similar laws
- Respect privacy and handle recovered credentials responsibly
- Use for educational purposes or legitimate security research

## Contributing

Contributions welcome! Areas for improvement:

- Rainbow table implementation
- Multi-threading support
- Progress indicators and statistics
- Rule-based wordlist generation
- GUI interface
- Additional hash algorithms
- Performance optimizations

## Troubleshooting

### Common Issues

**"Invalid hash type" error:**
- Check if the hash is supported by **hashlib** library.
```bash
# Check supported algorithms
python3 -c "import hashlib; print(hashlib.algorithms_guaranteed)"
```

**Slow performance:**
- Use smaller, targeted wordlists first
- Ensure wordlist is on fast storage (SSD)
- Consider implementing multi-threading (see Roadmap)

## Alternatives & Comparisons

| Tool | Speed | Features | Complexity |
|------|-------|----------|------------|
| **Dehasher** | Moderate | Basic | Low (Educational) |
| Hashcat | Very Fast | Advanced | High (Professional) |
| John the Ripper | Fast | Advanced | Medium-High |
| CrackStation | Instant | Web-based | N/A (Online service) |

Dehasher prioritizes **simplicity and education** over raw performance. For production security work, consider professional tools like Hashcat or John the Ripper.

## Credits

- **Institution**: Northeastern University  
- **Course**: CY5001 (Cyberspace Technology & Applications)
- **Instructor**: Dr. Jose Sierra
- **Date**: Fall 2023

This project demonstrates practical application of:
- Python programming for security tools
- Cryptographic hash functions
- Dictionary attack methodologies
- Secure coding practices
- Security tool development lifecycle

## Resources

**Learning Materials:**
- [Python hashlib Documentation](https://docs.python.org/3/library/hashlib.html)
- [OWASP Password Storage Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html)
- [How Rainbow Tables Work](https://kestas.kuliukas.com/RainbowTables/)

**Wordlist Sources:**
- [SecLists on GitHub](https://github.com/danielmiessler/SecLists)
- [CrackStation Wordlist](https://crackstation.net/crackstation-wordlist-password-cracking-dictionary.htm)
- [Weakpass.com](https://weakpass.com/)

## Acknowledgments

- Inspired by tools like Hashcat and John the Ripper
- Thanks to the Python cryptography community
- Built as part of Northeastern University's cybersecurity curriculum
