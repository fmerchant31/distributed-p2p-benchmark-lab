# Distributed P2P Benchmark Lab

This project simulates a simple P2P node network on Kubernetes with monitoring and autoscaling.

## Features
- Kubernetes deployment of mock nodes using `http-echo`
- ClusterIP service to expose nodes internally
- HPA for horizontal scaling
- Prometheus + Grafana setup
- Python script to generate synthetic traffic
- CI workflow to lint YAML configs

## Run Locally (minikube/kind)

```bash
kubectl apply -f k8s/namespace.yaml
kubectl apply -f k8s/
kubectl apply -f monitoring/
