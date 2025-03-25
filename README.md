# Simple-Blockchain-Simulation

# Overview

This project is a basic blockchain simulation built using Python. It demonstrates fundamental concepts such as:

### Block Structure:
Each block contains an index, timestamp, list of transactions, previous block hash, and its own hash.

### Hashing Mechanism:
Uses SHA-256 to compute hashes for block integrity.

### Proof-of-Work (PoW):
Implements a simple PoW algorithm to add computational complexity.

### Dynamic Transactions: 
Allows dynamic input of transactions.

### Chain Validation:
Ensures chain integrity and detects tampering.

# Features

### Blockchain Class: 
Manages the chain and adds blocks.

### Dynamic Transaction Input: 
Users can add transactions via the terminal.

### Proof-of-Work:
Adjustable difficulty with iteration limits to prevent infinite loops.

### Chain Validation:
Automatically detects if any block is tampered with.

# Installation

### Clone the repository:

git clone : https://github.com/likithreddy77/Simple-Blockchain-Simulation.git

cd blockchain-simulation

### Run the script:

python blockchain_simulation.py

# Usage

## Add Transactions:

Enter comma-separated transactions when prompted.

Type 'exit' to stop adding blocks.

## View Blockchain:

The full chain will be printed before and after tampering.

### Tampering Demonstration:

The program will tamper with a block to show how chain validation detects it.

# Example Output:

Enter transactions (comma-separated) or 'exit' to stop: Alice pays Bob 50 BTC

Enter transactions (comma-separated) or 'exit' to stop: Bob pays Charlie 30 BTC

Enter transactions (comma-separated) or 'exit' to stop: exit

### Blockchain before tampering:
Block 1: Transactions: ['Alice pays Bob 50 BTC']

Block 2: Transactions: ['Bob pays Charlie 30 BTC']

Is the blockchain valid? True

### Blockchain after tampering:
Block 1: Transactions: ['Alice pays Bob 100 BTC']

Is the blockchain valid? False
