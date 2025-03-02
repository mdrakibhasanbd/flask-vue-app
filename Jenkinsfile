pipeline {
    agent any

    environment {
        PYTHON = '/usr/bin/python3'
        NODE = '/usr/bin/node'
        DOCKER_COMPOSE_PATH = '/var/lib/jenkins/workspace/flask-vue-app/docker-compose.yml'
    }

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/mdrakibhasanbd/flask-vue-app.git'
            }
        }

        stage('Setup Python Environment') {
            steps {
                script {
                    // Create the virtual environment
                    sh 'python3 -m venv venv'
                    
                    // Ensure bump2version is in requirements.txt and install dependencies
                    sh '''echo "bump2version" >> requirements.txt
                         . venv/bin/activate && pip install -r requirements.txt'''
                }
            }
        }

        stage('Versioning Flask') {
            steps {
                script {
                    // Use bump2version to increment patch version automatically
                    sh '. venv/bin/activate && bump2version patch --new-version $(python setup.py --version) --no-tag --no-commit'
                }
            }
        }

        stage('Setup Node Environment') {
            steps {
                script {
                    // Install Node.js dependencies
                    sh 'npm install'
                }
            }
        }

        stage('Versioning Vue') {
            steps {
                script {
                    // Run Vue.js versioning (e.g., through a custom npm script)
                    sh 'npm run release'
                }
            }
        }

        stage('Build and Push Docker Images') {
            steps {
                script {
                    // Build Docker images using docker-compose
                    sh "docker-compose -f ${DOCKER_COMPOSE_PATH} build"
                    // Optionally push Docker images to a registry if needed
                    // sh "docker-compose -f ${DOCKER_COMPOSE_PATH} push"
                }
            }
        }

        stage('Deploy Application') {
            steps {
                script {
                    // Take down any existing containers and bring them back up with docker-compose
                    sh "docker-compose -f ${DOCKER_COMPOSE_PATH} down"
                    sh "docker-compose -f ${DOCKER_COMPOSE_PATH} up -d"
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
