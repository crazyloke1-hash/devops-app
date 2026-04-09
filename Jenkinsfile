pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "lokesh1926/expense-tracker-1:v1"
    }

    stages {

        stage('Checkout Code') {
            steps {
                git 'https://github.com/crazyloke1-hash/devops-app.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat "docker build -t %DOCKER_IMAGE% ."
            }
        }

        stage('Docker Login') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'docker-cred',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {
                    bat '''
                    docker logout
                    echo %DOCKER_PASS% | docker login -u %DOCKER_USER% --password-stdin
                    '''
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                bat "docker push %DOCKER_IMAGE%"
            }
        }
    }

    post {
        success {
            echo "✅ Pipeline SUCCESS - Image pushed!"
        }
        failure {
            echo "❌ Pipeline FAILED - Check logs"
        }
    }
}