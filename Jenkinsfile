pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                docker run -d zip:1
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
