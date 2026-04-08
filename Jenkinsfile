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
                withCredentials([usernamePassword(credentialsId: 'docker-cred', usernameVariable: 'lokesh1926', passwordVariable: 'pB/?pzj5:t&J%FT')]) {
                    bat 'docker login -u lokesh1926 -p pB/?pzj5:t&J%FT'
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
