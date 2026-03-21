output "ecr_repository_arn" {
  description = "ARN del repositorio ECR grupo1"
  value       = aws_ecr_repository.adapter_service.arn
}

output "ecr_repository_registry_id" {
  description = "Registry ID del repositorio ECR grupo1"
  value       = aws_ecr_repository.adapter_service.registry_id
}

output "ecr_repository_repository_url" {
  value       = aws_ecr_repository.adapter_service.repository_url      
}