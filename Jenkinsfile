pipeline {
    agent any

    // environment block có thể bị bỏ qua nếu không dùng biến môi trường

    stages {
        stage('Clone Repo') {
            steps {
                sh 'rm -rf app || true'
                sh 'git clone https://github.com/congnam101/flask-mysql-app.git app'
            }
        }

        stage('Build Image') {
            steps {
                dir('app') {
                    sh 'docker build -t flask_mysql_app_web .'
                }
            }
        }

        stage('Stop Containers') {
            steps {
                dir('app') {
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

