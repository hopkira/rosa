from setuptools import find_packages, setup

package_name = 'rosa_py_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='hopkira',
    maintainer_email='hopkira@googlemail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
           'screen_node = rosa_py_pkg.screen_node:main',
           'state_machine_node = rosa_py_pkg.state_machine_node:main'
        ],
    },
)
