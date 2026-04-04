pipeline {
    agent any

    stages {
        stage('Check Docker') {
            steps {
                bat 'docker --version'
            }
        }

        stage('Build') {
            steps {
                bat 'docker build -t crazyloke1-hash/devops-app:v1 .'
            }
        }

        stage('Push') {
            steps {
                bat 'docker push crazyloke1-hash/devops-app:v1'
            }
        }
    }
}