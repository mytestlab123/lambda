# Run

* [video](https://www.youtube.com/watch?v=7u1p5dieIh8)

* Build & Deploy

```
sam build
sam deploy --guided

```


* Get list of all employees

```
curl -s -X GET \
>   'https://kwx6ge5llf.execute-api.ap-southeast-1.amazonaws.com/nonprod/employee?start=0&end=2' \
>   --header 'Accept: */*' \
>   --header 'User-Agent: Thunder Client (https://www.thunderclient.com)' | jq .
{
  "message": "[{\"name\":\"bob\",\"empolyee_id\":1},{\"name\":\"jeff\",\"empolyee_id\":2}]"
}
```

* Add new employee

```
curl -X POST \
>   'https://kwx6ge5llf.execute-api.ap-southeast-1.amazonaws.com/nonprod/employee' \
>   --header 'Accept: */*' \
>   --header 'User-Agent: Thunder Client (https://www.thunderclient.com)' \
>   --header 'Content-Type: application/json' \
>   --data-raw '{
>   "name": "Sparsh Karpe",
>   "empolyee_id": 6
> }' | jq .
{
  "message": "[{\"name\":\"bob\",\"empolyee_id\":1},{\"name\":\"jeff\",\"empolyee_id\":2},{\"name\":\"fred\",\"empolyee_id\":3},{\"name\":\"joe\",\"empolyee_id\":4},{\"name\":\"Sparsh Karpe\",\"empolyee_id\":6}]"
}
```
