pipeline {
    agent any

    environment {
        DOCKER_COMPOSE_PATH = "/var/lib/jenkins/workspace/flask-vue-app/docker-compose.yml"
        PYTHON = '/usr/bin/python3'
        NODE = '/usr/bin/node'
    }

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', credentialsId: 'your-credentials-id', url: 'https://github.com/mdrakibhasanbd/flask-vue-app.git'
            }
        }

        stage('Setup Dependencies') {
            steps {
                sh 'pip install --upgrade bump2version'
                sh 'npm install'
            }
        }

        stage('Versioning Flask') {
            steps {
                sh 'bump2version patch'
            }
        }

        stage('Versioning Vue') {
            steps {
                sh 'npm run release'
            }
        }

        stage('Push Version Changes') {
            steps {
                script {
                    sh '''
                    git config user.email "jenkins@yourdomain.com"
                    git config user.name "Jenkins CI"
                    git add .
                    git commit -m "Automated version bump"
                    git push --follow-tags
                    '''
                }
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
