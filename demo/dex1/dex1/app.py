from oneinch_py import OneInchSwap, TransactionHelper
import requests
import json
import csv
import time
import sys
import os
from web3 import Web3

def lambda_handler(event, context):
    rpc_url = "https://polygon-mainnet.infura.io/v3/d162e1d2d54e4fd5b07a78b9b9176728"
    referrerAddress="0xbd0B3cB386314a7d4c314825727Aa4CCE2FA5e1b"
    chain = 'polygon'
    final_body = json.dumps(json.loads(event['body']),indent=4)
    print ("final_body ==>", final_body)
    print ("===============")
    body_dict = json.loads(event['body'])
    event = body_dict
    print ("body_dict ==>", event)
    # print (event_dict)
    # print (event_dict['message'])
    # print (event_dict['portfolio'])
    # print (event_dict['total_investment_amount'])
    # print (event_dict['public_key'])
    # print (event_dict['private_key'])
    # print (event_dict['destReceiver'])

    # final_event = json.dumps(event,indent=4)
    # print ("final_event ==>", final_event)

    message = event['message']
    print (message)
    portfolio  = event['portfolio']
    print(portfolio)
    total_investment_amount = float(event['total_investment_amount'])
    print (total_investment_amount)
    public_key = event['public_key']
    print (public_key)
    private_key = event['private_key']
    print (private_key)
    destReceiver = event['destReceiver']
    print (destReceiver)
    file = open(portfolio)
    exchange = OneInchSwap(public_key, chain=chain) # initialise the OneInchSwap object as "exchange"
    helper = TransactionHelper(rpc_url, public_key, private_key, chain=chain) # initialise the TransactionHelper object as "helper"

    row_count = sum(1 for row in file) - 1
    print("Total coins (Portfolio Size): ",row_count)
    print("Total Investment Ammount: ",total_investment_amount)
    investment_amount = total_investment_amount / row_count
    print("Investment Ammount per coin: ", investment_amount)
    print("Investment Ammount per coin calculated as: Total investment amount / Portfolio size")
    file.close()


    file = open(portfolio)
    csvreader = csv.reader(file)
    header = []
    header = next(csvreader)
    rows = []
    i = 0
    print("Buying coins started ...")
    print("Please wait ...")
    for row in csvreader:
        swap_tx = exchange.get_swap("USDC", row[0], investment_amount, 0.5, destReceiver=destReceiver, referrerAddress=referrerAddress, fee=3) # get the swap transaction
        result = helper.build_tx(swap_tx,'high') # prepare the transaction for signing, gas price defaults to fast.
        print("\n\n")
        print ("swap_tx:", swap_tx)
        print (type(swap_tx))
        print("\n\n")
        print ("result:", result)
        print (type(result))
        print("\n\n")
        result = helper.sign_tx(result) # sign the transaction using your private key
        swap_result = helper.broadcast_tx(result) #broadcast the transaction to the network and wait for the receipt. 
        # web3.eth.waitForTransactionReceipt(swap_result)

        # print("\n\n")
        # print (type(swap_result))
        # print("swap_result:", swap_result)
        print("\n\n")
        rows.append(row)
        i = i + 1
        print(i, " of ", row_count, " coins bought", row[0], " worth $", investment_amount)
        time.sleep (5)
        # sleep for 5 seconds to avoid rate limit
        time.sleep (5)

    print("All coins bought")
    print(rows)
    print("\n\n")
    print("Check Recever: https://polygonscan.com/address/"+destReceiver+"#tokentxns")
    print("Check Sender: https://polygonscan.com/address/"+public_key)
    file.close()
    return {
        "isBase64Encoded": "false",
        "statusCode": 200,
        # "body": "successful",
        # "body": '{"message": "hello world"}',
        "body": final_body,
        "headers": {
            "content-type": "application/json"
        }
    }