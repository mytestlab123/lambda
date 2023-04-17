from oneinch_py import OneInchSwap, TransactionHelper
import json
from decouple import config

# pip install python-decouple 1inch.py==1.8.2 requests==2.28.1 web3<6.0
investment_token = "xDAI"
# investment_token = "WXDAI"
# investment_token = "USDC"
token = "ELK"
# token = "USDC"
amount = 0.002
chain = 'gnosis'
public_key = config('public_key')
private_key = config('private_key')
rpc_url = "https://gnosischain-rpc.gateway.pokt.network"


def ApproveToken (token):
  print ("Approving token: ", token)
  # print ("Amount: ", amount)
  approve_tx = exchange.get_approve(token) # get approval transaction
  built = helper.build_tx(approve_tx) # prepare the transaction for signing, gas price defaults to fast.
  signed = helper.sign_tx(built) # sign the transaction using your private key
  approval_result = helper.broadcast_tx(signed) #broadcast the transaction to the network and wait for the receipt. 

def GetBalance ():
  result = helper.get_ERC20_balance(exchange._token_to_address(investment_token))
  if result == 0:
    print ("You don't have any tokens to swap.")
    exit ()
  print ("\n","Token: ", investment_token, "Balance: ", result, "\n")
  return result


exchange = OneInchSwap(public_key, chain=chain) # initialise the OneInchSwap object as "exchange"
helper = TransactionHelper(rpc_url, public_key, private_key, chain=chain) # initialise the TransactionHelper object as "helper"

# GetBalance()

get_allowance = exchange.get_allowance(investment_token, public_key)
print ("Allowance: ", get_allowance)
loads = json.loads(json.dumps(get_allowance))
print ("Allowance: ", loads.get("allowance"))
print (type(loads.get("allowance")))

if loads.get("allowance") == '0':
    print ("You need to approve the token first.")
    ApproveToken (investment_token, amount)

swap_tx = exchange.get_swap(investment_token, token, amount , 0.5) # get the swap transaction
# swap_tx = exchange.get_swap(investment_token, token, 0.02, 0.5) # get the swap transaction
result = helper.build_tx(swap_tx) # prepare the transaction for signing, gas price defaults to fast.
result = helper.sign_tx(result) # sign the transaction using your private key
swap_result = helper.broadcast_tx(result) #broadcast the transaction to the network and wait for the receipt. 

# GetBalance()

print ("\n","Token: ", investment_token, "Balance: ", helper.get_ERC20_balance(exchange._token_to_address(investment_token)), "\n")
print ("\n","Token: ", investment_token, "Balance: ", helper.get_ERC20_balance(exchange._token_to_address("0xe91D153E0b41518A2Ce8Dd3D7944Fa863463a97d")), "\n")

# result = helper.get_ERC20_balance(exchange._token_to_address(investment_token))
# print ("\n","Token: ", investment_token, "Balance: ", result, "\n")
# result = helper.get_ERC20_balance(exchange._token_to_address(token))
# print ("\n","Token: ", investment_token, "Balance: ", result, "\n")


# print(swap_result)