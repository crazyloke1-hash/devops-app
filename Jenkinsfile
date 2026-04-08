pipeline {
    agent any

    stages {

        stage('Build Image') {
            steps {
                bat 'docker build -t lokesh1926/expense-tracker-1:v1 .'
            }
        }

        stage('Login to DockerHub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'docker-cred', usernameVariable: 'USER', passwordVariable: 'PASS')]) {
                    bat 'echo %PASS% | docker login -u %USER% --password-stdin'
                }
            }
        }

        stage('Push Image') {
            steps {
                bat 'docker push lokesh1926/expense-tracker-1:v1'
            }
        }
    }
}