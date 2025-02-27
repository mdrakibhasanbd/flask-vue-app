pipeline {
    agent any

    environment {
        DOCKER_COMPOSE_PATH = "/var/lib/jenkins/workspace/flask-vue-app/docker-compose.yml"
    }

    stages {
        stage('Checkout Code') {
            steps {
                git 'https://github.com/mdrakibhasanbd/flask-vue-app.git'
            }
        }

        stage('Build and Push Docker Images') {
            steps {
                script {
                    sh 'docker-compose build'
                }
            }
        }

        stage('Deploy Application') {
            steps {
                script {
                    sh 'docker-compose down'
                    sh 'docker-compose up -d'
                }
            }
        }
    }

    post {
        success {
            echo 'Deployment successful!'
        }
        failure {
            echo 'Deployment failed!'
        }
    }
}
