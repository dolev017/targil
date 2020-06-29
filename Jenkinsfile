pipeline {
    agent {
    label {
        filename 'Dockerfile'
        dir 'build'
        label 'zip-job-docker'
        registryUrl 'https://github.com/dolev017/targil.git'
          }
      }
    stages {
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
