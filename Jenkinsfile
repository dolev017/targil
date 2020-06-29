pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'docker run -d --name zip_targil zip:1'
            }
        }
        stage('Publish') {
            steps {
                echo 'Testing..'
            }
        }
        stage('E-mail') {
            steps {
                echo 'Deploying....'
            }
        }
        stage('Clean') {
            steps {
                echo 'Clean'
            }
        }
    }
}
