# PROJECT_CHAT_BOT
# AI-Driven Chatbot Platform with Full DevOps Pipeline

A scalable chatbot platform integrating **Amazon Lex (V2)** for AI/NLP, **Terraform** for infrastructure automation, and **Kubernetes (EKS)** for deployment.  
This project follows a full **DevOps pipeline** using GitHub Actions and GitOps (Argo CD).

---

## Project Goals
- Build a production-grade chatbot using AWS Lex for natural language understanding.  
- Automate infrastructure with Terraform (VPC, EKS, IAM, ECR).  
- Deploy services on Kubernetes with GitOps workflows.  
- Implement CI/CD with GitHub Actions + Argo CD.  
- Enable observability with CloudWatch, Prometheus, Grafana.  

---

## Tech Stack
- **AI**: Amazon Lex V2 (chatbot engine)  
- **Infra as Code**: Terraform (with remote state in S3 + DynamoDB lock)  
- **Runtime**: Kubernetes (AWS EKS) with NGINX Ingress  
- **CI/CD**: GitHub Actions, Docker, Amazon ECR, Argo CD  
- **Observability**: AWS CloudWatch, Prometheus, Grafana  
- **Languages**: Python / Node.js for webhook services  

---

## Branching Strategy
- **main** → Protected branch, always stable/release-ready.  
- **dev** → Integration branch where features are merged.  
- **feature/*** → Short-lived branches for individual tasks.  
- **hotfix/*** → For urgent fixes in `main`, merged back into both `main` and `dev`.  

**Rules**  
- Use pull requests (PRs) for all merges.  
- Require at least 1 reviewer + CI checks before merge.  
- Use [Conventional Commits](https://www.conventionalcommits.org/) (e.g., `feat: add terraform backend`).  

---

## Initial Repo Structure
