pipeline {
    agent any
    stages {
        stage('Testing the Flask App') {
            steps {
                bat 'conda activate jenkins'
                bat 'pip install -r requirements.txt'
                bat 'pytest -v'
            }
        }
        stage('Build Docker Image') {
            steps {
                bat 'docker build -t fashion_mnist .'
            }
        }
        stage('Kill Previous Docker Image') {
            steps {
               bat 'docker stop fmn || true'
               bat 'docker rm fmn || true'
            }
        }
	    stage('Run New Docker Image') {
            steps {
               bat 'docker run -d -p 5000:5000 --name=fmn fashion_mnist'
            }
        }
    }
} 