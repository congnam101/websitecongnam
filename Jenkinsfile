pipeline {
    agent any

    stages {
        stage('Clone Repo') {
            steps {
                echo '🌀 Cloning flask-mysql-app repository...'
                sh 'rm -rf app || true'
                sh 'git clone https://github.com/congnam101/flask-mysql-app.git app'
            }
        }

        stage('Build Image') {
            steps {
                dir('app') {
                    echo '🐳 Building Docker image...'
                    sh 'docker build -t flask_mysql_app_web .'
                }
            }
        }

        stage('Stop Containers') {
            steps {
                dir('app') {
                    echo '🛑 Stopping existing containers (if any)...'
                    sh '''
                        docker-compose down || true
                        docker rm -f flask_web_jenkins || true
                        docker rm -f flask_db_jenkins || true
                    '''
                }
            }
        }

        stage('Start Containers') {
            steps {
                dir('app') {
                    echo '🚀 Starting containers...'
                    sh 'docker-compose up -d'
                }
            }
        }
    }

    post {
        success {
            echo '✅ Deployment Successful!'
            cleanWs()
        }
        failure {
            echo '❌ Deployment Failed.'
            cleanWs()
        }
        always {
            echo '🧹 Cleaning up workspace...'
        }
    }
}

