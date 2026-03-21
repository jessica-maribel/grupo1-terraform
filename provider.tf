provider "aws" {
  region  = "us-east-1"
  profile = "master"
}

data "aws_region" "current" {}