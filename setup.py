from setuptools import setup, find_packages

setup(
    name='your-package-name',          # Nom du package sur PyPI
    version='0.1.0',                   # Version initiale
    description='Une description courte de votre package',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Votre nom',
    author_email='votre-email@example.com',
    url='https://github.com/votre-utilisateur/votre-repo',
    packages=find_packages(where='src'),   # Détecte les packages dans 'src'
    package_dir={'': 'src'},
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=[
        # Dépendances du projet (listées dans requirements.txt)
    ],
)
