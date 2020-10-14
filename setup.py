from setuptools import setup

setup(
    name='snapshot',
    version='0.1',
    author="Robert Millington",
    author_email="rob@warp17.com",
    description="Snapshot is a tool to manage AWS EC2 snapshots",
    license="GPLv3+",
    packages=['shotty'],
    url="https://github.com/GlobalRLM/snapshot",
    install_requires=[
        'click',
        'boto3'
    ],
    entry_points='''
        [console_scripts]
        shotty=shotty.shotty:cli
    ''',
)
