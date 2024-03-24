from setuptools import find_packages, setup

# Declaring variables for setup functions
PROJECT_NAME = "Face DeskAttendance Authenticator"
VERSION = "0.0.1"
AUTHOR = "Amarnatha Gowda T"
DESRCIPTION = "This is a Face Authenticator Project with marking the attendance using the Face Authentications"


setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESRCIPTION,
    packages=find_packages(),
)
