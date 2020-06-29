pipeline {
    agent {
        docker { image "test10:1"} 
    stages {
        stage('Build') {
            steps {
                sh 'docker run --tag zip:1 .'
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
