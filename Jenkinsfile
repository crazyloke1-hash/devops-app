pipeline {
    agent any

    stages {
        stage('Build Docker Image') {
            steps {
                bat 'docker build -t lokesh1926/expense-tracker-1:v1 .'
            }
        }

        stage('Push to DockerHub') {
            steps {
                bat 'docker push lokesh1926/expense-tracker-1:v1'
            }
        }
    }
}
