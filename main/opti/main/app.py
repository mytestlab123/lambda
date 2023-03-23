from oneinch_py import OneInchSwap, TransactionHelper
import json, csv, random, wget
import time, sys, requests
from web3 import Web3
from os import system


def lambda_handler(event, context):
    # rpc_url = "https://optimism-mainnet.infura.io/v3/031bbd7a436b427881ed1b80f9bceb9e"
    rpc_url = "https://optimism-mainnet.infura.io/v3/d162e1d2d54e4fd5b07a78b9b9176728"
    # rpc_url = "https://arbitrum-mainnet.infura.io/v3/d162e1d2d54e4fd5b07a78b9b9176728"
    # rpc_url = "https://polygon-mainnet.infura.io/v3/d162e1d2d54e4fd5b07a78b9b9176728"
    # referrerAddress="0xbd0B3cB386314a7d4c314825727Aa4CCE2FA5e1b"
    referrerAddress=""
    print ("event ==>", event)
    final_body = json.dumps(json.loads(event['body']),indent=4)
    print ("final_body ==>", final_body)
    print ("===============")
    body_dict = json.loads(event['body'])
    event = body_dict
    print ("body_dict ==>", event)
    print ("===============")

    message = event['message']
    print ("message ==>", message)
    chain = event['chain']
    print ("chain ==>", chain)
    URL = event['portfolio']
    portfolio = "/tmp/portfolio_"+str(random.randint(1,100000))+".csv"
    response = wget.download(URL, portfolio)
    print ("\n Portfolio File Name ==>", portfolio)
    system("cat "+portfolio)
    print ("\n\n")
    file = open(portfolio)
    # Open csv file from URL and read it into a list
    # portfolio  = event['portfolio']
    # print(portfolio)

    total_investment_amount = float(event['total_investment_amount'])
    print ("total_investment_amount ==>", total_investment_amount)
    public_key = event['public_key']
    print ("public_key ==>", public_key)
    private_key = event['private_key']
    # print (private_key)
    destReceiver = event['destReceiver']
    print ("destReceiver ==>", destReceiver)
    file = open(portfolio)
    # Open csv file from URL and read it into a list
    # csvreader = csv.reader(file)
    # header = []
    # header = next(csvreader)
    # rows = []
    # for row in csvreader:
    #     rows.append(row)
    # print (header)
    # print (rows)
    exchange = OneInchSwap(public_key, chain=chain) # initialise the OneInchSwap object as "exchange"
    helper = TransactionHelper(rpc_url, public_key, private_key, chain=chain) # initialise the TransactionHelper object as "helper"

    row_count = sum(1 for row in file) - 1
    print("Total coins (Portfolio Size): ",row_count)
    print("Total Investment Ammount: ",total_investment_amount)
    investment_amount = total_investment_amount / row_count
    print("Investment Ammount per coin: ", investment_amount)
    print("Investment Ammount per coin calculated as: Total investment amount / Portfolio size")
    file.close()
    print ("investment_amount ==>", investment_amount)


    file = open(portfolio)
    csvreader = csv.reader(file)
    header = []
    header = next(csvreader)
    rows = []
    i = 0
    print("Buying coins started ...")
    print("Please wait ...")
    for row in csvreader:
        print("\n\n")
        print("\n",i+1, " ==> ", row[0]) 
        swap_tx = exchange.get_swap("USDC", row[0], investment_amount, 1, destReceiver=destReceiver) # get the swap transaction
        result = helper.build_tx(swap_tx,'low') # prepare the transaction for signing, gas price defaults to fast.
        # result = helper.build_tx(swap_tx,'high') # prepare the transaction for signing, gas price defaults to fast.
        print("\n\n")
        # print ("swap_tx:", swap_tx)
        # print ("swap_tx.keys ==>", swap_tx.keys())
        # print (type(swap_tx))
        # print("\n\n")
        # print ("result:", result)
        # print (type(result))
        # print("\n\n")
        result = helper.sign_tx(result) # sign the transaction using your private key
        swap_result = helper.broadcast_tx(result) #broadcast the transaction to the network and wait for the receipt. 
        # print("\n\n")
        # print (type(swap_result))
        # print("swap_result:", swap_result)
        # print("\n\n")
        # web3.eth.waitForTransactionReceipt(swap_result)
        # print ("result.keys ==>", result.keys())
        # print("\n\n")
        # print ("swap_result.keys ==>", swap_result.keys())
        # print("\n\n")
        # print (swap_result['transactionHash'])

        rows.append(row)
        i = i + 1
        print(i, " of ", row_count, " coins bought", row[0], " worth $", investment_amount,"successful ✅ \n\n")
        time.sleep (5)
        # sleep for 5 seconds to avoid rate limit
        time.sleep (5)

    print("All coins bought")
    print(rows)
    print("\n\n")
    # print("Check Recever: https://optimistic.etherscan.io/address/"+destReceiver+"#tokentxns")
    print("Check Sender: https://optimistic.etherscan.io/address/"+public_key)
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