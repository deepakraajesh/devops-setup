# DevOps Setup

This repository contains a collection of scripts and configurations designed to streamline and automate CICD. It aims to provide a quick and efficient setup for various development and deployment workflows.

## Key Components

### Flask Application (`flask-python-app/`)

This directory contains the Python code for the Flask application. It's the application that will be containerized and deployed.

### Helm Charts (`helm-charts/`)

The `helm-charts` directory includes the Helm chart used to deploy the Flask application to Kubernetes. This chart defines the necessary Kubernetes resources, such as Deployments, Services, and Ingresses.

### Helm Repository (`docs/`)

The `docs` directory serves as a Helm repository, hosting the chart packages and the `index.yaml` file. This allows for easy distribution and installation of the Helm chart.

```
helm repo add deepakraajesh https://deepakraajesh.github.io/devops-setup/
```

### GitHub Actions CI (`.github/workflows/`)

GitHub Actions workflows are configured to automatically build and push Docker images to a container registry whenever changes are pushed to the application code.

### FluxCD GitOps (`gitops-flux/`)

FluxCD is used to implement GitOps, ensuring that the Kubernetes cluster state matches the configurations defined in this repository.

* Flux is bootstrapped in the cluster using Helm charts from:
    * **Flux Operator:** [Flux Operator helm artifact](https://artifacthub.io/packages/helm/flux-operator/flux-operator)
    * **Flux Instance:** [Flux Instance helm artifact](https://artifacthub.io/packages/helm/flux-instance/flux-instance)
* Configurations for development and production environments are managed separately within this directory.

## Directory Structure
```
devops-setup
├── flask-python-app
│   ├── app.py
│   ├── requirements.txt
│   ├── Dockerfile
│   └── tests
│       └── _test.py
├── helm-charts
│   ├── flask-app
│   │   ├── Chart.yaml
│   │   ├── values.yaml
│   │   └── templates
│   │       ├── deployment.yaml
│   │       ├── externalsecret.yaml
│   │       ├── hpa.yaml
│   │       ├── secrets.yaml
│   │       └── service.yaml
│   └── flux-bootstrap
│   │   └── flux-operator-values.yaml
├── docs
│   ├── index.yaml
│   └── flask-app-chart-*.tgz (Helm chart packages)
├── .github/workflows
│   └── build-flask-app.yaml (GitHub Actions workflow)
├── gitops-flux
│   ├── clusters
│   │   └── cluster 1 (minikube - You can add as many as clusters here)
│   │       ├── app-kustomization.yaml
│   │       ├── flux-components-kustomization.yaml
│   │       ├── infra-kustomization.yaml
│   │       └── observability-exporters-kustomization.yaml
│   └── gitops-configs
│       ├── apps
│       │   ├── base
│       │   │   ├── app-configs/
│       │   │   └── utils/
│       │   ├── dev
│       │   │   ├── app-configs
│       │   │   │   └── kustomization.yaml (patch from base)
│       │   │   └── utils
│       │   │       └── kustomization.yaml (patch from base)
│       │   └── prod
│       │   │   ├── app-configs
│       │   │   │   └── kustomization.yaml (patch from base)
│       │   │   └── utils
│       │   │       └── kustomization.yaml (patch from base)
│       ├── flux-components
│       └── infra
└── .gitignore
```

## Author

* Deepak Raajesh - [\[Github Profile\]](https://github.com/deepakraajesh)