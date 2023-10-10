import json
import logging
from web3 import Web3
from web3.exceptions import ConnectionError, InvalidAddress, BlockNotFound

with open('config.json', 'r') as config_file:
    config = json.load(config_file)

ethereum_node_url = config.get('ethereum_node_url', '')
log_file_path = config.get('log_file_path', 'eth_tracker.log')

logging.basicConfig(filename=log_file_path, level=logging.INFO)

def setup_web3(node_url):
    try:
        web3 = Web3(Web3.HTTPProvider(node_url))
        if not web3.isConnected():
            raise ConnectionError("Failed to connect to the Ethereum node.")
        return web3
    except ConnectionError as ce:
        logging.error(ce)
        raise

def track_and_decode_transactions(address=None, block_number=None):
    try:
        web3 = setup_web3(ethereum_node_url)

        if address:
            if not Web3.isAddress(address):
                raise InvalidAddress("Invalid Ethereum address format.")

            transactions = web3.eth.get_transactions_by_address(address)
        elif block_number:
            block = web3.eth.get_block(block_number)
            if block is None:
                raise BlockNotFound(f"Block {block_number} not found.")
            transactions = block.transactions
        else:
            raise ValueError("Please provide either an address or a block number.")

        for tx_hash in transactions:
            tx = web3.eth.get_transaction(tx_hash)
            input_data = tx.input

            decoded_data = web3.eth.abi.decode_function_input(input_data)

            logging.info(f"Transaction Hash: {tx_hash.hex()}")
            logging.info(f"From: {tx['from']}")
            logging.info(f"To: {tx['to']}")
            logging.info(f"Input Data: {input_data.hex()}")
            logging.info(f"Decoded Data: {decoded_data}\n")

    except ConnectionError:
        logging.error("Error: Unable to connect to the Ethereum node. Check your node URL.")
    except InvalidAddress as e:
        logging.error(f"Error: {e}")
    except BlockNotFound as e:
        logging.error(f"Error: {e}")
    except ValueError as ve:
        logging.error(f"Error: {ve}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {str(e)}")

address = '0xYourEthereumAddress'
track_and_decode_transactions(address=address)
