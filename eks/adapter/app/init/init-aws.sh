#!/bin/bash
echo "🟢 Creando bucket S3 local..."
awslocal s3 mb s3://my-local-bucket

echo "📁 Creando y subiendo archivo JSON de ejemplo..."
echo '{"001": "Jane", "002": "Mario", "003": "Andres", "004": "David"}' > example.json
awslocal s3 cp example.json s3://my-local-bucket/

echo "📁 Creando archivo CSV de ejemplo..."
echo -e "id,name\n1,Alice\n2,Bob" > example.csv
awslocal s3 cp example.csv s3://my-local-bucket/

echo "🔑 Creando secreto db_password con URL de conexión a PostgreSQL..."
awslocal secretsmanager create-secret \
  --name db_credentials \
  --secret-string '{"JWT_TOKEN":"fds454rGHTDS4545s4a6f45gr5g454dDFR","OKTA_API_TOKEN":"d48e5#@yrgklo4kjhhbg41g45"}'

echo "✅ Inicialización completada."