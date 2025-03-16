pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/furkankorkmazuseinsider/deneme2.git'
            }
        }

        stage('Run Selenium Tests') {
            steps {
                sh 'python3 tests/test_insider_careers.py'
            }
        }
    }
}

