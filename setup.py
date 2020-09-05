from setuptools import setup, find_packages


packages = find_packages(include=('Arcapi', 'Arcapi.*'))

setup(
    name='Arc_api',
    version='1.0',
    author='littlebutt',
    author_email='luogan199686@gmail.com',
    license='MIT License',
    url="https://github.com/littlebutt/Arcapi",
    description='An API for Arc Prober.',
    packages=packages,
    install_requires=['websockets>=8.1', 'websocket-client>=0.57.0','brotli>=1.0.9'],
    python_requires='>=3.7',
    platforms='any'
)
