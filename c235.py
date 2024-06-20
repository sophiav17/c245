from web3 import Web3

infura_url = 'https://mainnet.infura.io/v3/1e64e76cbf9e4b1ca262a150e0b42849'
web3 = Web3(Web3.HTTPProvider(infura_url))
gas_prices = web3.eth.gas_price

safe_low_gas_price = int(gas_prices * 0.9)
average_gas_price = int(gas_prices * 1.0)
fast_gas_price = int(gas_prices * 1.1)
fastest_gas_price = int(gas_prices * 1.2)

safe_low_gas_price_gwei = web3.from_wei(safe_low_gas_price, 'gwei')
average_gas_price_gwei = web3.from_wei(average_gas_price, 'gwei')
fast_gas_price_gwei = web3.from_wei(fast_gas_price, 'gwei')
fastest_gas_price_gwei = web3.from_wei(fastest_gas_price, 'gwei')

print('Safe Low Gas Price (Gwei)', safe_low_gas_price_gwei)
print('Average Gas Price (Gwei)', average_gas_price_gwei)
print('Fast Gas Price (Gwei)', fast_gas_price_gwei)
print('Fastest Gas Price (Gwei)', fastest_gas_price_gwei)

gas_price = web3.eth.gas_price
print("Gas Price in Gwei", gas_price)