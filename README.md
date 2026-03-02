# GKE Deployment Workflow with Docker and HPA Testing 
This guide outlines the steps to build, push, and deploy Docker services to Google Kubernetes Engine (GKE), configure Horizontal Pod Autoscaling (HPA), and test using load generation.

## 1. Clone the Repository
```bash
git clone https://github.com/arvindgupta-cloud/new-1.git
cd new-1
```

## 2. Create a Docker Artifact Repository
Create a Google Artifact Registry repository to store Docker images:

```bash
gcloud artifacts repositories create my-repo \
    --location=asia-south1 \
    --repository-format=docker
```

## 3. Set Environment Variables
```bash
export PROJECT_ID=qwiklabs-gcp-04-88cc01b8252e
export REGION=asia-south1
```

## 4. Build and Push Docker Images
Build and push Docker images for all services:

**Shop Service**
```bash
docker build -t $REGION-docker.pkg.dev/$PROJECT_ID/my-repo/shop-service:latest ./shop-service
docker push $REGION-docker.pkg.dev/$PROJECT_ID/my-repo/shop-service:latest
```

**About Service**
```bash
docker build -t $REGION-docker.pkg.dev/$PROJECT_ID/my-repo/about-service:latest ./about-service
docker push $REGION-docker.pkg.dev/$PROJECT_ID/my-repo/about-service:latest
```

**Home Service**
```bash
docker build -t $REGION-docker.pkg.dev/$PROJECT_ID/my-repo/home-service:latest ./home-service
docker push $REGION-docker.pkg.dev/$PROJECT_ID/my-repo/home-service:latest
```

**Contact Service**
```bash
docker build -t $REGION-docker.pkg.dev/$PROJECT_ID/my-repo/contact-service:latest ./contact-service
docker push $REGION-docker.pkg.dev/$PROJECT_ID/my-repo/contact-service:latest
```

## 5. Create GKE Cluster
```bash
gcloud container clusters create my-gke-cluster \
    --location=us-central1-a
```

## 6. Deploy Services to GKE
Apply all Kubernetes manifests:
```bash
kubectl apply -f all-services.yaml
```

Apply Horizontal Pod Autoscaler (HPA) configuration for the home service:
```bash
kubectl apply -f horizontal_scaling_home.yml
```

## 7. Install Load Testing Tool (hey)
```bash
sudo apt-get install hey
```

**8. Test Horizontal Scaling**
Send load to the Home Service endpoint:

```bash
hey -z 1m -c 10 http://34.36.61.45/home
```

Check the HPA status:
```bash
kubectl describe hpa home-service-hpa
```

## 9. Verify Pods
List all pods in the cluster:
```bash
kubectl get pods
```

This workflow covers:
- Docker image building and pushing
- GKE cluster creation
- Deploying multiple microservices
- Horizontal Pod Autoscaling setup and testing


# Keep Learning  
