from setuptools import setup, find_packages


if __name__ == '__main__':
    setup(
        name='orcplug',
        version='0.0.1',

        packages=find_packages(),

        entry_points={'orc.plugin': [
            'api_handler = orcplug:api_handler',
            'custom_logger = orcplug:custom_logger',
        ]},

        install_requires=['orc>=0.1.0']
    )
