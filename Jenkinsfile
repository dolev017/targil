pipeline {
<<<<<<< HEAD
    agent {
        docker { image "test10:1"} 
=======
    agent any 
>>>>>>> 296db92d21812ae8b39134be4f83428287fdb2ce
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
