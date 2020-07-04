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
                sh "python3 /tmp/zip_job.py"
                sh "ls -l"
            }
        }
        stage('Publish') {
            steps { 
                  
               sh 'curl -fL https://getcli.jfrog.io | sh'
               sh 'curl -u super-user:Qw12865! -T a_1.2.0.zip "http://localhost:8081/artifactory/binary-storage/a_1.2.0.zip'
            }
        }
    }
}
