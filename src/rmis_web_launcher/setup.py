from setuptools import setup

package_name = 'rmis_web_launcher'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name, ['launch/web_launcher_launch.py']),   
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='EnesIsaoglu',
    maintainer_email='enesisaogluu@gmail.com',
    description='A package to launch the web server and open the browser',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'web_launcher = rmis_web_launcher.web_launcher:main',
        ],
    },
    
)