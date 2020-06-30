pipeline {
    agent {
      docker {
         image 'zip:1'
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
