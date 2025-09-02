# 🚀 PROJECT_CHAT_BOT CI/CD Pipeline

## ✅ Features
- Jenkins Pipeline (GitHub Webhook triggered)
- Build & Test (Maven + JUnit)
- Code Quality & Security: SonarQube
- Vulnerability Scanning: Trivy
- Future: Deployment on EC2/Docker/K8s

## 🔧 Setup Steps
1. Install Jenkins, SonarQube, Trivy (see setup guide)
2. Add Jenkinsfile in repo
3. Configure Jenkins job with SCM
4. Setup GitHub webhook
5. Trigger build by pushing code

## 📸 Screenshots
- ![Pipeline Success](screenshots/pipeline_success.png)
- ![Test Results](screenshots/test_results.png)
- ![SonarQube Report](screenshots/sonarqube_report.png)
- ![Trivy Scan](screenshots/trivy_scan.png)
