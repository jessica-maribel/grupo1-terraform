# Kubernetes Deployment
resource "kubernetes_deployment" "adapter_fastapi" {
  metadata {
    name      = "adapter-fastapi"
    namespace = var.grupo
  }

  spec {
    replicas = 1
    selector {
      match_labels = {
        app = "adapter-fastapi"
      }
    }

    template {
      metadata {
        labels = {
          app = "adapter-fastapi"
        }
      }

      spec {
        container {
          name = "adapter-fastapi"
          # image             = "${data.terraform_remote_state.base.outputs.repository_url}:latest"
          # image             = "${data.terraform_remote_state.base.outputs.ecr_repository_repository_url}:latest"
          image             = "${data.aws_ecr_repository.adapter_service.repository_url}:latest"
          image_pull_policy = "Always"

          port {
            container_port = 8000
          }

          env {
            name  = "SECRET_NAME"
            value = "db_credentials"
          }

          env {
            name  = "STORAGE_TYPE"
            value = "s3"
          }

          env {
            name  = "AWS_DEFAULT_REGION"
            value = var.aws_region
          }

          volume_mount {
            name       = "logs"
            mount_path = "/var/log/app"
          }
        }

        container {
          name              = "prometheus-adapter"
          # image             = "${data.terraform_remote_state.base.outputs.ecr_repositories.repository_url}:prometheus-adapter-latest"
          image = "${data.aws_ecr_repository.adapter_service.repository_url}:prometheus-adapter-latest"
          image_pull_policy = "Always"

          port {
            container_port = 9200
          }

          volume_mount {
            name       = "logs"
            mount_path = "/var/log/app"
          }
        }

        volume {
          name = "logs"
          empty_dir {}
        }
      }
    }
  }
  provider = kubernetes._internal
}

# Kubernetes Service
resource "kubernetes_service" "adapter_fastapi_service" {
  metadata {
    name      = "adapter-fastapi-service"
    namespace = var.grupo
  }

  spec {
    selector = {
      app = "adapter-fastapi"
    }

    type = "LoadBalancer"

    port {
      name        = "app"
      port        = 80
      target_port = 8000
    }

    port {
      name        = "metrics"
      port        = 9100
      target_port = 9200
    }
  }

  provider = kubernetes._internal
}