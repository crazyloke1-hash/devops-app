pipeline {
    agent any

    stages {

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t lokesh1926/expense-tracker-1:v1 .'
            }
        }

        stage('Docker Login') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'docker-cred', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
                    powershell '''
                    $env:PASSWORD | docker login -u $env:USERNAME --password-stdin
                    '''
                }
            }
        }

        stage('Push to DockerHub') {
            steps {
                bat 'docker push lokesh1926/expense-tracker-1:v1'
            }
        }
    }
}