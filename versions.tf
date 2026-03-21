terraform {

  backend "s3" {
    bucket = "grupo1-terraform-state"
    key = "sis-distribuidos-avanzados/terraform.tfstate"
    region = "us-east-1"
  }
  
  required_version = ">= 1.5.1"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "4.10.0"
    }
  }
}
