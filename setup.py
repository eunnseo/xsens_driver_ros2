from setuptools import setup

package_name = 'ichthus_xsens_driver'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='eunseo',
    maintainer_email='eunseo.choi.d@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'ichthus_xsens_driver = ichthus_xsens_driver.ichthus_xsens_driver:main'
        ],
    },
)
