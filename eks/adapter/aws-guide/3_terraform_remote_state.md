### adapter_service terraform remote state

## ECR setup

Since we deployed ECR resource from other project we need to read the repository_url by using terraform `data` resource.
Edit the file `provider.tf` and put the correct values in this section

```
data "terraform_remote_state" "base" {
  backend = "s3"
  config = {
    bucket = "master-software-terraform-state"
    key    = "sis-distribuidos-avanzados/terraform.tfstate"
    region = "us-east-1"
  }
}
```


then in the `main.tf` file in the lines `27` and `57` make reference to the output variable that contains the ecr repository_url
```
data.terraform_remote_state.base.outputs.ecr_repositories.adapter_service.repository_url
```