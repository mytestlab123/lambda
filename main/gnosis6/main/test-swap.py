from oneinch_py import OneInchSwap, TransactionHelper

# rpc_url = "https://polygon-rpc.com"
# public_key = ""
# private_key = "" #remember to protect your private key. Using environmental variables is recommended. 
# chain = 'polygon'

chain = 'gnosis'
public_key = '0x4cb7CF54e6b198fbFB9A16Dbe999e01cB72b5D19'
private_key = '0e9caa956c3e6cc7bc18b2e8274a38a648d294cb5fce3b3f6f37b22af66ea371'
rpc_url = "https://gnosischain-rpc.gateway.pokt.network"

exchange = OneInchSwap(public_key, chain=chain) # initialise the OneInchSwap object as "exchange"
helper = TransactionHelper(rpc_url, public_key, private_key, chain=chain) # initialise the TransactionHelper object as "helper"

approve_tx = exchange.get_approve("USDC") # get approval transaction
built = helper.build_tx(approve_tx) # prepare the transaction for signing, gas price defaults to fast.
signed = helper.sign_tx(built) # sign the transaction using your private key
approval_result = helper.broadcast_tx(signed) #broadcast the transaction to the network and wait for the receipt. 

print(approval_result)

swap_tx = exchange.get_swap("USDC", "WETH", 0.001, 0.5) # get the swap transaction
result = helper.build_tx(swap_tx) # prepare the transaction for signing, gas price defaults to fast.
result = helper.sign_tx(result) # sign the transaction using your private key
swap_result = helper.broadcast_tx(result) #broadcast the transaction to the network and wait for the receipt. 


print(swap_result)