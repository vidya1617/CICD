pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "vidya1617/uploaddata:latest"  
        DOCKER_CREDENTIALS = 'docker-hub-credentials' 
        EC2_USER = "ec2-user"
        EC2_HOST = "13.212.85.157"  
        EC2_KEY = "C:/terraform/vidya.pem"  
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/vidya1617/CICD.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $DOCKER_IMAGE .'
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withDockerRegistry([credentialsId: DOCKER_CREDENTIALS, url: ""]) {
                    sh 'docker push $DOCKER_IMAGE'
                }
            }
        }

        stage('Deploy to EC2') {
            steps {
                sh '''
                ssh -o StrictHostKeyChecking=no -i $EC2_KEY $EC2_USER@$EC2_HOST << EOF
                docker pull $DOCKER_IMAGE
                docker stop mycontainer || true
                docker rm mycontainer || true
                docker run -d --name mycontainer -p 80:5000 $DOCKER_IMAGE
                EOF
                '''
            }
        }
    }
}
