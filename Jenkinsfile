pipeline {
    agent {
      docker {
         image 'zip:1'
         label 'zip-job-docker'
}
}
    stages {
        stage('build') {
            steps {
                sh 'make'
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
