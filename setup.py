from setuptools import setup


setup(
    name="roku_remote",
    version="1.0.1",
    packages=["roku_remote"],
    package_data={
        'roku_remote': ['roku_remote/*.png']
    },
    include_package_data=True,
    url="https://github.com/rootVIII/roku_remote",
    license="MIT",
    author="rootVIII",
    description="Download Audio from your favorite YouTube videos",
    entry_points={
        "console_scripts": [
            "roku_remote=roku_remote.roku_remote:main"
        ]
    },
    data_files=[
        (
            'roku_remote', ['roku_remote/icon.png']
        )
    ]
)
