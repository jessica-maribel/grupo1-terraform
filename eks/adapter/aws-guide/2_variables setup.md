### adapter_service terraform variables

open the infrastructure folder

```
cd infrastructure/
```

edit variables.tf file and put `default` property in the variables `kubernetes_host` and `kubernetes_ca_certificate`
You have to obtain the values from the eks cluster and put it in the variables.tf file

for instance
```
variable "kubernetes_host" {
  type        = string
  description = "EKS Cluster Endpoint"
  default = "https://XXXXXXXXXXXXXXXXXXXXXXXX.gr7.us-east-1.eks.amazonaws.com"
}
```
and
```

variable "kubernetes_ca_certificate" {
  type        = string
  description = "EKS Cluster CA Certificate"
  default ="XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
}

```

after you added the values for kubernetes then add the value for the grupo variable
for instance
```
variable "grupo" {
  type        = string
  description = "nombre del grupo, por ejemplo: grupo-1"
  default = "grupo-1"
}

```
