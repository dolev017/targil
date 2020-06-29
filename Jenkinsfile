pipeline {
    agent any 
#       docker {
#            image 'test10:1'
#            label 'zip-job-docker'
#              }
    stages {
        stage('Build') {
            steps {
                echo 'Building..'
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
