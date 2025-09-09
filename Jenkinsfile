pipeline {
    agent any

    tools {
        sonarQubeScanner 'sonar-scanner'   // must match the name you gave in Jenkins Tools
    }

    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/CHINNA-SAMY2/PROJECT_CHAT_BOT.git', branch: 'main'
            }
        }

        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('SonarQube') {   // must match the name you gave in Jenkins System config
                    sh 'sonar-scanner'
                }
            }
        }

        stage('Quality Gate') {
            steps {
                timeout(time: 1, unit: 'HOURS') {
                    waitForQualityGate abortPipeline: true
                }
            }
        }
    }
}
