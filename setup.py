import os
from setuptools import find_packages, setup
from typing import List


def get_requirements() -> List[str]:
    try:
        pkg_dir = os.path.dirname(os.path.realpath(__file__))
        required_dir = os.path.join(pkg_dir, "requirements.txt")
        with open(required_dir) as f:
            required = f.read().splitlines()
    except Exception as e:
        required = []
    finally:
        return required


package_name = 'fastapi_ros'


setup(
    name=package_name,
    version='1.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=get_requirements(),
    zip_safe=True,
    maintainer='Batbold N.',
    maintainer_email='bxtbold@protonmail.com',
    description='The ROS2 package with a FastAPI backend server',
    license='bxtbold@protonmail.com',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'main = fastapi_ros.main:main'
        ],
    },
)
