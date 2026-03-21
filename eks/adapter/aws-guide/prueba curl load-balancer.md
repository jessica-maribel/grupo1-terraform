## Prueba

```
curl -X POST -H "Content-Type: application/json" \
  "http://a0838383651754fdfb6087fa7f72875f-640056007.us-east-1.elb.amazonaws.com/parse-file/" \
  -d '{"bucket": "adapter-bucket-ups-sandbox", "key": "example.json"}'
```

```
curl -X POST -H "Content-Type: application/json" \
  "http://ae560bfa3da734e10b2ef44e72983d64-1369166502.us-east-1.elb.amazonaws.com/parse-file/" \
  -d '{"bucket": "adapter-bucket-ups-sandbox", "key": "example.csv"}'
```