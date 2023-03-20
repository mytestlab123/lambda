# Run


* Invoke function using Json file, with all details.
```bash
export url="https://w6nw4wez4zag4cpyal5iiwb6l40etvug.lambda-url.ap-southeast-1.on.aws/"
curl -X POST ${url} --header 'Content-Type: application/json' -d @/tmp/event.json
```



* Run on local using python-lambda-local module.
```bash
pip install python-lambda-local
python-lambda-local -f lambda_handler app.py event.json
```

* Invoke function using data as JSON format.

```bash
export url="https://w6nw4wez4zag4cpyal5iiwb6l40etvug.lambda-url.ap-southeast-1.on.aws/"
curl -X POST ${url} \
  --header 'Content-Type: application/json' \
  --data-raw '{
  "message": "Namaste",
  "portfolio": "bear.csv",
  "public_key": "0x4cb7CF54e6b198fbFB9A16Dbe999e01cB72b5D19",
  "private_key": "0XXXXXXXXXXXXXXX",
  "total_investment_amount": 0.02,
  "destReceiver": "0xBc63219a3a5453dB9CcD7096c6009c1Ed4e69b45"
}'
```

* Invoke using `aws lambda invoke` command.

```bash
aws lambda invoke --function-name ${fun} --payload file://events/event2.json outputfile.txt  --cli-binary-format raw-in-base64-out
{
    "StatusCode": 200,
    "ExecutedVersion": "$LATEST"
}
```

* Invoke using `sam local invoke`

```bash
sam local invoke HelloWorldFunction -e /tmp/event.json --debug
```
