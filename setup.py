import os
from setuptools import find_packages, setup
from django_simplenote import version


# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

# stamp the package prior to installation
version.stamp_directory(os.path.join(os.getcwd(), 'django_simplenote'))

setup(
    name='django-simplenote',
    version=version.get_version(),
    packages=find_packages(),
    include_package_data=True,
    package_data={'django_simplenote': ['VERSION_STAMP']},
    description='A reusable Django app for simple notes.',
    long_description="A reusable Django app for simple notes.",
    install_requires=['Django>=2',],
    url='https://github.com/gregschmit/django-simplenote',
    author='Gregory N. Schmit',
    author_email='gschmi4@uic.edu',
    license='MIT',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 2.0',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
    ],
)
