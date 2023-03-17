# Run

* Run on local
```bash
pip install python-lambda-local
python-lambda-local -f lambda_handler app.py event.json
```

* Invoke

```bash
curl -X POST \
  'https://ubpb6ijr5yvgggzmzxcfluyiha0ggumt.lambda-url.ap-southeast-1.on.aws/' \
  --header 'Content-Type: application/json' \
  --data-raw '{
  "key1": "value1",
  "key2": "value2",
  "key3": "value3"
}'
```


```bash
curl -X POST \
  'https://ubpb6ijr5yvgggzmzxcfluyiha0ggumt.lambda-url.ap-southeast-1.on.aws/' \
  --header 'Content-Type: application/json' -d @/tmp/event.json
```

* Lambda Invoke
```bash
aws lambda invoke --function-name ${fun} --payload file://events/event2.json outputfile.txt  --cli-binary-format raw-in-base64-out
{
    "StatusCode": 200,
    "ExecutedVersion": "$LATEST"
}
```