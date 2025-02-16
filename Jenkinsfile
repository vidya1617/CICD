pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "vidya1617/uploaddata:latest"
        AWS_REGION = "ap-southeast-1"
        S3_BUCKET = "your-s3-bucket-for-codedeploy"
        CODEDEPLOY_APP = "DockerApp"
        CODEDEPLOY_GROUP = "DockerDeployGroup"
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
                withDockerRegistry([credentialsId: "docker-hub-credentials", url: ""]) {
                    sh 'docker push $DOCKER_IMAGE'
                }
            }
        }

        stage('Upload Deployment Package') {
            steps {
                sh '''
                zip -r deploy.zip appspec.yml scripts/
                aws s3 cp deploy.zip s3://$S3_BUCKET/
                '''
            }
        }

        stage('Deploy with CodeDeploy') {
            steps {
                sh '''
                aws deploy create-deployment \
                    --application-name $CODEDEPLOY_APP \
                    --deployment-group-name $CODEDEPLOY_GROUP \
                    --s3-location bucket=$S3_BUCKET,key=deploy.zip,bundleType=zip
                '''
            }
        }
    }
}
