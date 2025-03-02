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
                    
                    // Ensure bump2version is installed and install dependencies
                    sh 'echo "bump2version" >> requirements.txt'
                    sh '. venv/bin/activate && pip install -r requirements.txt'
                }
            }
        }

        stage('Versioning Flask') {
            steps {
                script {
                    // Versioning Flask without committing or tagging
                    sh '''
                    . venv/bin/activate
                    bump2version patch --new-version 1.0.1 --no-tag --no-commit
                    '''
                }
            }
        }

        stage('Commit and Push Version Changes') {
            steps {
                script {
                    // If you want to commit and push manually after versioning
                    sh '''
                    git add .
                    git commit -m "Bump version to 1.0.1"
                    git push origin main
                    '''
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

        stage('Deploy Application') {
            steps {
                script {
                    // Take down any existing containers and bring them back up with docker-compose
                    sh 'docker-compose -f ${DOCKER_COMPOSE_PATH} down'
                    sh 'docker-compose -f ${DOCKER_COMPOSE_PATH} up -d'
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
