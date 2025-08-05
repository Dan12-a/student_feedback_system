pipeline {
    agent any

    environment {
        IMAGE_NAME = 'student-feedback-app'
        CONTAINER_NAME = 'student-feedback-container'
    }

    stages {
        stage('Build') {
            steps {
                echo '🚧 Building Docker image...'
                sh 'docker build -t $IMAGE_NAME .'
            }
        }

        stage('Stop Old Container') {
            steps {
                echo '🧹 Stopping and removing old container (if any)...'
                sh '''
                    docker stop $CONTAINER_NAME || true
                    docker rm $CONTAINER_NAME || true
                '''
            }
        }

        stage('Run') {
            steps {
                echo '🚀 Running the new container...'
                sh 'docker run -d --name $CONTAINER_NAME -p 5000:5000 $IMAGE_NAME'
            }
        }
    }
}
