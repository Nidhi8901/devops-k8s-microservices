# DevOps Kubernetes Microservices Project

## Project Overview
This project demonstrates a complete DevOps workflow for a **microservices-based application** using Docker and Kubernetes.

- **Frontend:** Nginx web application serving product pages  
- **Backend:** API serving product data  
- **Database:** Simulated via backend environment variables (Secrets)  
- **Kubernetes:** Deployments, Services, ConfigMaps, Secrets, Ingress, HPA  
- **CI/CD & DevOps:** Dockerized microservices, kind cluster for local Kubernetes, HPA for backend scaling  

## Architecture
                  +----------------+
                  |    Ingress     |
                  +--------+-------+
                           |
         +-----------------+-----------------+
         |                                   |
 +-------v-------+                   +-------v-------+
 |   Frontend    |                   |    Backend    |
 |  Deployment   |                   |  Deployment   |
 +---------------+                   +---------------+
         |                                   |
         +-----------------+-----------------+
                           |
                         Database
 



### Explanation:

1. **Ingress:** Handles incoming traffic and routes requests to frontend services.
2. **Frontend Deployment:** Nginx or web application serving the UI for products.
3. **Backend Deployment:** API service providing product data, connected to secrets/configs for DB credentials.
4. **Database:** Simulated via environment variables or can be extended to a real DB.



### Prerequisites
- Docker Desktop (with Kubernetes enabled)  
- kubectl CLI  
- kind (Kubernetes in Docker)  
- Git  

## Project Setup

### Clone the Repository
```bash
git clone <your-github-repo-url>
cd devops-k8s-microservices


###Build Docker Images

# Frontend
docker build -t devops-k8s-microservices-frontend ./frontend

# Backend
docker build -t devops-k8s-microservices-backend ./backend


###Load Images into Kind Cluster

kind load docker-image devops-k8s-microservices-frontend:latest --name devops-cluster
kind load docker-image devops-k8s-microservices-backend:latest --name devops-clusterLoad Images into Kind Cluster
kind load docker-image devops-k8s-microservices-frontend:latest --name devops-cluster
kind load docker-image devops-k8s-microservices-backend:latest --name devops-cluster


###Deploy to Kubernetes

#Apply ConfigMaps, Secrets, Deployments, Services, and Ingress

kubectl apply -f k8s/frontend-configmap.yaml
kubectl apply -f k8s/backend-secrets.yaml
kubectl apply -f k8s/backend-deployment.yaml
kubectl apply -f k8s/backend-service.yaml
kubectl apply -f k8s/frontend-deployment.yaml
kubectl apply -f k8s/frontend-service.yaml
kubectl apply -f k8s/frontend-ingress.yaml
kubectl apply -f k8s/backend-hpa.yaml

###Verify Deployments

kubectl get pods
kubectl get svc
kubectl get ingress
kubectl get hpa

###Access Application

Frontend URL: http://localhost:<NodePort>
or via Ingress: http://frontend.localhost:(update hosts file if needed)
Backend URL: http://backend:5000/products (inside cluster or via frontend pod)

###Testing

Test backend from frontend pod:

kubectl exec -it <frontend-pod-name> -- curl http://backend:5000/products

Test frontend NodePort:

curl http://localhost:<NodePort>/products

###Features

- Microservices Architecture: Frontend and backend separated with Kubernetes services
- Config Management: ConfigMaps for frontend configuration, Secrets for backend credentials
- Scalability: Horizontal Pod Autoscaler (HPA) applied on backend
- Ingress Routing: Nginx Ingress Controller for external access
- Dockerized Services: Easy build, deploy, and portability


###Project structure 

devops-k8s-microservices/
├── frontend/
│   └── Dockerfile
├── backend/
│   └── Dockerfile
├── k8s/
│   ├── frontend-configmap.yaml
│   ├── frontend-deployment.yaml
│   ├── frontend-service.yaml
│   ├── frontend-ingress.yaml
│   ├── backend-deployment.yaml
│   ├── backend-service.yaml
│   ├── backend-secrets.yaml
│   └── backend-hpa.yaml
├── docker-compose.yml
└── README.md


###Notes

- For local testing, update /etc/hosts or C:\Windows\System32\drivers\etc\hosts to resolve frontend.local.
- NodePort may vary; check with kubectl get svc frontend.
- HPA automatically scales backend pods based on CPU usage.
- All services are dockerized and can be deployed to any Kubernetes cluster.
