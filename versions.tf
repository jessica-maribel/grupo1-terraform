terraform {
  required_version = ">= 1.5.1"

  backend "s3" {
    bucket = "master-software-terraform-state"
    key    = "grupo1/ecr/terraform.tfstate"
    region = "us-east-1"
  }

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "4.10.0"
    }
  }
}