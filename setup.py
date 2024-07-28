from setuptools import setup, find_packages

setup(
    name='lgrep',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'lgrep=src.main',
        ],
    },
    install_requires=[
        # Add any dependencies your package needs here
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.10',
)