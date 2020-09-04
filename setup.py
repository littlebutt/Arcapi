from setuptools import setup, find_packages


packages = find_packages(include=('Arcapi', 'Arcapi.*'))

setup(
    name='Arcapi',
    version='1.0',
    author='littlebutt',
    license='MIT License',
    description='An API for Arc Prober.',
    packages=packages,
    package_data={
        '': ['*.pyi'],
    },
    install_requires=['websockets>=8.1', 'websocket-client>=0.57.0','brotli>=1.0.9'],
    python_requires='>=3.7',
    platforms='any'
)
