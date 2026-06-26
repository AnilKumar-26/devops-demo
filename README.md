# DevOps Demo — Anil Kumar

A production-style DevOps pipeline built from scratch.

## What this does
- Python app containerized with Docker
- CI pipeline via GitHub Actions — builds and smoke tests on every push
- Deployed to Kubernetes (k3s) with 2 replicas and zero-downtime rolling updates

## Stack
- Docker
- GitHub Actions
- Kubernetes (k3s)

## Run locally
```bash
docker build -t devops-demo:v1 .
docker run -p 8080:8080 devops-demo:v1
curl http://localhost:8080
```

## Deploy to Kubernetes
```bash
kubectl apply -f deployment.yaml
kubectl get pods
```
