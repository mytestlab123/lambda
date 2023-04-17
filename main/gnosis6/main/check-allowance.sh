#!/bin/bash

# List all tokens on 1inch for given blockchain
# Usage: ./list.sh
# URL: https://docs.1inch.io/docs/aggregation-protocol/api/swagger/
# Code for [chainid](https://github.com/RichardAtCT/1inch_wrapper/blob/daa2473a434a6dda4f6a2b0c8bfd4315b44024e9/oneinch_py/main.py#L21)
# List of more [chains](https://chainlist.org/)
#     chains = {
    #     "ethereum": '1',
    #     "binance": '56',
    #     "polygon": "137",
    #     "optimism": "10",
    #     "arbitrum": "42161",
    #     "gnosis": "100",
    #     "avalanche": "43114",
    #     "fantom": "250"
    # }

#export chain_id=100; curl -s https://api.1inch.io/v5.0/${chain_id}/tokens | jq '.tokens[]' | grep "symbol" | cut -d '"' -f 4 | sort

# export chain_id=100; curl -s https://api.1inch.io/v5.0/${chain_id}/tokens | jq '.tokens[]' | grep "symbol" | cut -d '"' -f 4 | sort | grep -vi REALTOKEN
export WETH="0x6A023CCd1ff6F2045C3309768eAd9E68F978f6e1"
export USDT="0x4ecaba5870353805a9f068101a40e0f32ed605c6"
export USDC="0xddafbb505ad214d7b80b1f830fccc89b60fb7a83"
export BUSD="0xdd96B45877d0E8361a4DDb732da741e97f3191Ff"
export walletAddress="0x4cb7CF54e6b198fbFB9A16Dbe999e01cB72b5D19"
export tokenAddress=${WETH}
# export tokenAddress=${USDT}
# export tokenAddress=${USDC}
echo ${tokenAddress}
echo WETH
curl -s -X 'GET' "https://api.1inch.io/v5.0/100/approve/allowance?tokenAddress=${tokenAddress}&walletAddress=${walletAddress}" -H 'accept: */*' | jq .



# List all tokens on 1inch for given blockchain and 
# List of liquidity sources that are available for routing in the 1inch Aggregation protocol

#curl  https://api.1inch.io/v5.0/100/liquidity-sources 
#curl -s  https://api.1inch.io/v5.0/100/presets | jq .