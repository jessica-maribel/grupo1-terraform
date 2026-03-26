# ===============================
# GUIA DE COMANDOS - AWS / DOCKER / TERRAFORM / EKS
# ===============================

# -------- AWS AUTH --------

# Login con SSO (IMPORTANTE)
aws sso login --profile master

# Configurar credenciales manuales (opcional)
aws configure

# Ver identidad actual
aws sts get-caller-identity



# -------- AWS ECR --------

# Login a ECR
aws ecr get-login-password --region us-east-1 \
| docker login --username AWS --password-stdin <ACCOUNT_ID>.dkr.ecr.us-east-1.amazonaws.com

# Crear repositorio
aws ecr create-repository --repository-name adapter_service

# Listar repositorios
aws ecr describe-repositories


# -------- DOCKER --------

# Construir imagen
docker build -t adapter_service .

# Listar imágenes
docker images

# Etiquetar imagen
docker tag adapter_service:latest <ACCOUNT_ID>.dkr.ecr.us-east-1.amazonaws.com/adapter_service:latest

# Subir imagen a ECR
docker push <ACCOUNT_ID>.dkr.ecr.us-east-1.amazonaws.com/adapter_service:latest

# Ejecutar contenedor
docker run -p 8080:8080 adapter_service


# -------- TERRAFORM --------

# Inicializar proyecto
terraform init

# Validar configuración
terraform validate

# Formatear código
terraform fmt

# Planificar cambios
terraform plan

# Aplicar cambios
terraform apply

# Destruir infraestructura
terraform destroy

# Ver estado
terraform show

# Consola interactiva
terraform console


# -------- KUBERNETES / EKS --------

# Actualizar kubeconfig
aws eks update-kubeconfig --region us-east-1 --name <cluster-name>
aws eks update-kubeconfig --region us-east-1 --name master-dev-cluster --profile master

# Ver nodos
kubectl get nodes

# Ver pods
kubectl get pods

# Ver servicios
kubectl get svc

# Describir pod
kubectl describe pod <pod-name>

# Ver logs
kubectl logs <pod-name>

# Aplicar configuración
kubectl apply -f deployment.yaml

# Eliminar configuración
kubectl delete -f deployment.yaml


# -------- DEBUG / ERRORES --------

# Error de credenciales
aws configure

# Ver config de kubectl
kubectl config view

# Ver contexto actual
kubectl config current-context

# Exportar perfil AWS
export AWS_PROFILE=master

# Ver variables de entorno
env