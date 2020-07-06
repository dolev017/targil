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
                  
             //  sh 'curl -fL https://getcli.jfrog.io | sh'
             //  sh 'curl -u super-user:Qw12856! -T a_1.2.0.zip http://172.17.0.1:8081/artifactory/binary-storage/a_1.2.0.zip'
             //  sh 'curl -u super-user:Qw12856! -T b_1.2.0.zip http://172.17.0.1:8081/artifactory/binary-storage/b_1.2.0.zip'
             //  sh 'curl -u super-user:Qw12856! -T c_1.2.0.zip http://172.17.0.1:8081/artifactory/binary-storage/c_1.2.0.zip'
             //  sh 'curl -u super-user:Qw12856! -T d_1.2.0.zip http://172.17.0.1:8081/artifactory/binary-storage/d_1.2.0.zip'
            }
        }
    }
    post { 
        always { 
            cleanWs()
        }
    }
}
