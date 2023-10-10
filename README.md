# Functionality

***Tracking input data messages for a specific Ethereum address.***
    
***Tracking input data messages for a specific Ethereum block.ty***

# Installation

Clone the repository:

`git clone https://codeberg.org/0x5FE/EthereumTransactionDecoder.git`


Navigate to the project directory:

`cd EthereumTransactionDecoder`


Create a virtual environment (recommended):

`python3 -m venv venv`


Activate the virtual environment:

    On Linux/macOS:

    bash

source venv/bin/activate

`On Windows (PowerShell):`

powershell

    .\venv\Scripts\Activate

Install the required Python packages:


`pip install -r requirements.txt`


Create a config.json file in the project directory and add your Ethereum node URL:

json

{
    "ethereum_node_url": "https://mainnet.infura.io/v3/your_infura_project_id",
    "log_file_path": "eth_tracker.log"
}


Replace "https://mainnet.infura.io/v3/your_infura_project_id" with your Ethereum node URL.


# Usage

Track input data messages for a specific Ethereum address:


`python ethereumdecoder.py --address 0xYourEthereumAddress`

***Replace 0xYourEthereumAddress with the Ethereum address you want to track.***


Track input data messages for a specific Ethereum block:

`python ethereumdecoder.py --block 1234567`


***Replace 1234567 with the block number you want to track.***

# Error Handling
The script includes error handling for various scenarios, such as connection errors, invalid addresses, and block not found errors.

# Logging
The script logs information and errors to a log file specified in the config.json file. You can find the log file in the project directory.
