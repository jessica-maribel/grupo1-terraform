## K8S Design Patterns Examples

## Execution

### Docker Compose
```
docker-compose up --build
```

### Lambda function

json
```
curl -X POST -H "Content-Type: application/json" \
  "http://localhost:8000/parse-file/" \
  -d '{"bucket": "my-local-bucket", "key": "example.json"}'
```
csv

```
curl -X POST -H "Content-Type: application/json" \
  "http://localhost:8000/parse-file/" \
  -d '{"bucket": "my-local-bucket", "key": "example.csv"}'

```


open in your browser this url to view the promethus adapter

```
http://localhost:9200
```



curl -X POST -H "Content-Type: application/json" \
  "http://a7e937fb777444c4181716ba6731ee0f-409380331.us-east-1.elb.amazonaws.com/parse-file/" \
  -d '{"bucket": "adapter-bucket-ups-sandbox", "key": "example.json"}'
```


http://a7e937fb777444c4181716ba6731ee0f-409380331.us-east-1.elb.amazonaws.com/parse-file