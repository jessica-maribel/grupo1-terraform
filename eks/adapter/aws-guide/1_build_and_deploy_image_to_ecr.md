
### adapter_service image

login

```
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 526832762947.dkr.ecr.us-east-1.amazonaws.com
```


Open the app directory

```
cd app
```

build

```
docker build -t adapter_service .
docker build --platform linux/arm64 -t adapter_service .
```

tag

```
docker tag adapter_service:latest 526832762947.dkr.ecr.us-east-1.amazonaws.com/adapter_service:latest
docker tag adapter_service:latest 526832762947.dkr.ecr.us-east-1.amazonaws.com/adapter_service_grupo1:latest
```

push

```
docker push 526832762947.dkr.ecr.us-east-1.amazonaws.com/adapter_service_grupo1:latest
```


### adapter_service-prometheus-adapter image


Open the prometheus directory

```
cd prometheus
```


build

```
docker build --platform linux/arm64 -t adapter_service-prometheus-adapter -f Dockerfile .
```

tag

```
docker tag adapter_service-prometheus-adapter:latest 526832762947.dkr.ecr.us-east-1.amazonaws.com/adapter_service_grupo1:prometheus-adapter-latest
```

push

```
docker push 526832762947.dkr.ecr.us-east-1.amazonaws.com/adapter_service_grupo1:prometheus-adapter-latest
```