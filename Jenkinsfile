pipeline {
    agent any  // Exécuter sur n'importe quel agent

    environment {
        VENV = 'venv'  // Nom du virtualenv
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/ton-utilisateur/ton-repo.git'
            }
        }

        stage('Setup Python Environment') {
            steps {
                sh 'python3 -m venv $VENV'
                sh 'source $VENV/bin/activate'
                sh 'pip install --upgrade pip'
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'source $VENV/bin/activate && pytest tests/ --junitxml=report.xml'
            }
        }

        stage('Lint Code') {
            steps {
                sh 'source $VENV/bin/activate && flake8 src/'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t coaching2-app .'
            }
        }

        stage('Deploy Locally') {
            steps {
                sh 'docker run -d -p 8000:8000 coaching2-app'
            }
        }
    }

    post {
        always {
            junit 'report.xml'  // Générer les rapports de test
        }
        success {
            echo "Déploiement réussi 🎉"
        }
        failure {
            echo "Échec du pipeline ❌"
        }
    }
}
