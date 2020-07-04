pipeline {
    agent {
    // Equivalent to "docker build -f Dockerfile.build --build-arg version=1.0.2 ./build/
    dockerfile {
        filename 'Dockerfile'
        }
    }    
    stages {
        stage('Build') {
            steps {
                dir("tmp") {
                    sh "python3 zip_job.py"
                }
            }
        }
    }
}
