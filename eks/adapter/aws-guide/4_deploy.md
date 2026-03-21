### adapter_service terraform deploy

After you configured the variables and data terraform state reference you are ready to deploy the service to kubernetes

```
terraform apply
```

after terraform deploy the resources you will see in the console an url, copy it since it's the load balance dns where the service is exposed