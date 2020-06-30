pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                sh 'docker run -d zip:1'
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
