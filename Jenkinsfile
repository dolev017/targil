pipeline {
    agent {
    // Equivalent to "docker build -f Dockerfile.build --build-arg version=1.0.2 ./build/
    dockerfile {
        filename 'Dockerfile'
        dir '/home/dolev/targil'
        label 'zip-job-docker'
        additionalBuildArgs  '--build-arg version=1.0.2'
        args '-v /tmp:/tmp'
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
