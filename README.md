# AES-128 Implementation in Python

This repository contains my Python implementation of AES-128 for a computer security assignment. The project covers both encryption and decryption for a single 16-byte block and includes tests using standard AES test data.

## What this project includes

- AES-128 block encryption
- AES-128 block decryption
- Key expansion for 128-bit keys
- Separate functions for the main AES steps
- Unit tests and a known-answer test vector
- A small command-line script for quick testing

## Folder Structure

- `aes/operations.py`  
  Contains the main AES transformations:
  - SubBytes
  - ShiftRows
  - MixColumns
  - AddRoundKey  
  It also includes the inverse operations used during decryption.

- `aes/key_schedule.py`  
  Implements the AES-128 key expansion process.

- `aes/core.py`  
  Contains the overall encryption and decryption flow for one block.

- `aes/utils.py`  
  Helper functions for:
  - hex conversion
  - byte/state conversion
  - small utility operations

- `main.py`  
  A simple script for running encryption or decryption from the terminal.

- `tests/`  
  Contains test files for the AES core logic, key schedule, and standard test vectors.

## Requirements

- Python 3.x

This project does not use any external libraries.

## How to run

### Encrypt a block

    python main.py encrypt 00112233445566778899aabbccddeeff 000102030405060708090a0b0c0d0e0f

### Decrypt a block

    python main.py decrypt 69c4e0d86a7b0430d8cdb78070b4c55a 000102030405060708090a0b0c0d0e0f

## How to run the tests

    python -m unittest discover tests

## Example test vector used

- Plaintext: `00112233445566778899aabbccddeeff`
- Key: `000102030405060708090a0b0c0d0e0f`
- Ciphertext: `69c4e0d86a7b0430d8cdb78070b4c55a`

## Limitations

This implementation is limited to AES-128 and works on a single 16-byte block at a time. It does not include block modes such as CBC or CTR, and it is mainly intended for learning how AES works internally rather than for real-world secure deployment.