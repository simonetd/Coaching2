pipeline {
    agent any

    environment {
        PYPI_USERNAME = credentials('pypi-username')  // Identifiants PyPI
        PYPI_PASSWORD = credentials('pypi-token')     // Token API PyPI
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest tests/ --junitxml=results.xml'
            }
        }

        stage('Build Package') {
            steps {
                sh '''
                python setup.py sdist bdist_wheel
                '''
            }
        }

        stage('Publish to PyPI') {
            steps {
                sh '''
                python -m pip install twine
                twine upload --repository pypi dist/* \
                    -u ${PYPI_USERNAME} -p ${PYPI_PASSWORD}
                '''
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: '**/results.xml', fingerprint: true
        }
        success {
            echo 'Package publié avec succès sur PyPI.'
        }
        failure {
            echo 'Échec du pipeline.'
        }
    }
}
