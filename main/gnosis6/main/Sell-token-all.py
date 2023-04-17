from oneinch_py import OneInchSwap, TransactionHelper
import json
from decouple import config

investment_token = "ELK"
token_address = "0xeEeEEb57642040bE42185f49C52F7E9B38f8eeeE"
# investment_token = "GNO"
# token_address = "0x9C58BAcC331c9aa871AFD802DB6379a98e80CEdb"
# investment_token = "xDAI"
token = "ELK"
token = "xDAI"
# amount = 10000000
chain = 'gnosis'
public_key = config('public_key')
private_key = config('private_key')
rpc_url = "https://gnosischain-rpc.gateway.pokt.network"


def ApproveToken ():
  print ("Approving token: ", investment_token)
  approve_tx = exchange.get_approve(investment_token) # get approval transaction
  built = helper.build_tx(approve_tx) # prepare the transaction for signing, gas price defaults to fast.
  signed = helper.sign_tx(built) # sign the transaction using your private key
  approval_result = helper.broadcast_tx(signed) #broadcast the transaction to the network and wait for the receipt. 

exchange = OneInchSwap(public_key, chain=chain) # initialise the OneInchSwap object as "exchange"
helper = TransactionHelper(rpc_url, public_key, private_key, chain=chain) # initialise the TransactionHelper object as "helper"

result = helper.get_ERC20_balance(token_address)
print ("Token: ", investment_token, "Balance: ", result)
amount = result


get_allowance = exchange.get_allowance(investment_token, public_key)
print ("Allowance: ", get_allowance)
loads = json.loads(json.dumps(get_allowance))
print ("Allowance: ", loads.get("allowance"))
print (type(loads.get("allowance")))

if loads.get("allowance") == '0':
    print ("You need to approve the token first.")
    ApproveToken ()

# exit ()

print ("Result: ", result)
print (type (result))

if result == 0:
    print ("You don't have any tokens to swap.")
    print ("Balaance is Zero.")
    print ("Exiting...")
    exit ()

swap_tx = exchange.get_swap(investment_token, token, amount, 2) # get the swap transaction
result = helper.build_tx(swap_tx) # prepare the transaction for signing, gas price defaults to fast.
result = helper.sign_tx(result) # sign the transaction using your private key
swap_result = helper.broadcast_tx(result) #broadcast the transaction to the network and wait for the receipt. 


# print(swap_result)