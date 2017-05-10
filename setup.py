
from setuptools import setup


setup(
    name='grpc-retry',
    version='0.1.0',
    author='liut',
    author_email='liutao@licaigc.com',
    url='https://git.lcgc.work/platform/grpc-retry',
    description='Retry call of gRPC stub.',
    py_modules=['grpc_retry'],
    install_requires=[
        'grpcio',
        'python-decouple',
    ],
    classifiers=[
        'Framework :: Flask',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
    ],
)
