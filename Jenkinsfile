pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'docker build -t crazyloke1-hash/devops-app:v1 .'
            }
        }

        stage('Push') {
            steps {
                sh 'docker push crazyloke1-hash/devops-app:v1'
            }
        }
    }
} 
