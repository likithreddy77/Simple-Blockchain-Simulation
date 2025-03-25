import hashlib
import time

class Block:
    def __init__(self, index, transactions, previous_hash):
        self.index = index
        self.timestamp = time.time()
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.compute_hash()

    def compute_hash(self):
        block_string = f"{self.index}{self.timestamp}{self.transactions}{self.previous_hash}{self.nonce}"
        return hashlib.sha256(block_string.encode()).hexdigest()

    def proof_of_work(self, difficulty, max_iterations=1000000):
        iterations = 0
        while not self.hash.startswith('0' * difficulty):
            if iterations >= max_iterations:
                print("Proof of work failed: Reached maximum iterations.")
                return False
            self.nonce += 1
            self.hash = self.compute_hash()
            iterations += 1
        return True

class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_genesis_block()
        self.difficulty = 4

    def create_genesis_block(self):
        genesis_block = Block(0, "Genesis Block", "0")
        self.chain.append(genesis_block)

    def add_block(self, transactions):
        previous_hash = self.chain[-1].hash
        new_block = Block(len(self.chain), transactions, previous_hash)
        if new_block.proof_of_work(self.difficulty):
            self.chain.append(new_block)

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]

            if current.hash != current.compute_hash():
                return False

            if current.previous_hash != previous.hash:
                return False

        return True

    def tamper_with_block(self, index, new_transactions):
        if 0 <= index < len(self.chain):
            self.chain[index].transactions = new_transactions
            self.chain[index].hash = self.chain[index].compute_hash()

    def print_chain(self):
        for block in self.chain:
            print(f"Block {block.index}:")
            print(f"Timestamp: {block.timestamp}")
            print(f"Transactions: {block.transactions}")
            print(f"Previous Hash: {block.previous_hash}")
            print(f"Hash: {block.hash}")
            print("-" * 50)

if __name__ == "__main__":
    blockchain = Blockchain()

    while True:
        transactions = input("Enter transactions (comma-separated) or 'exit' to stop: ")
        if transactions.lower() == 'exit':
            break
        blockchain.add_block(transactions.split(','))

    print("Blockchain before tampering:")
    blockchain.print_chain()

    print("\nIs the blockchain valid?", blockchain.is_chain_valid())

    blockchain.tamper_with_block(1, ["Alice pays Bob 100 BTC"])

    print("\nBlockchain after tampering:")
    blockchain.print_chain()

    print("\nIs the blockchain valid?", blockchain.is_chain_valid())
