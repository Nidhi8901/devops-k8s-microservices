# DevOps Kubernetes Microservices Project

## 📌 Project Overview
This project demonstrates a complete DevOps workflow using a microservices-based architecture deployed on Kubernetes.

The application consists of:
- Frontend service
- Backend service
- Kubernetes orchestration
- Auto-scaling and ingress routing

## 🛠 Tech Stack
- Docker
- Kubernetes (K8s)
- Nginx Ingress Controller
- ConfigMaps & Secrets
- Horizontal Pod Autoscaler (HPA)
- Git & GitHub

## 🏗 Architecture
- Frontend communicates with Backend via Kubernetes Service
- Backend exposes REST API (`/products`)
- Ingress routes external traffic to Frontend
- HPA scales backend pods based on CPU usage

## 📂 Kubernetes Components
- Deployments (Frontend & Backend)
- Services (ClusterIP, NodePort)
- ConfigMaps & Secrets
- Ingress (Nginx)
- Horizontal Pod Autoscaler

## 🚀 How to Run
```bash
kubectl apply -f k8s/

