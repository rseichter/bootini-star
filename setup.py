from setuptools import setup

setup(
    name='Bootini-Star',
    version='0.0.1',
    description="Inspect EVE mail and skill queues in a web browser. Inspired by CCP's discontinued EVE Gate app.",
    author='Ralph Seichter',
    author_email='bootinistar@seichter.de',
    license='MIT',
    packages=['bootini_star', 'swagger_client'],
    include_package_data=True,
    #   install_requires=[
    #       'Flask >= 0.12.2',
    #       'Flask-Login >= 0.4.1',
    #       'Flask-Migrate >= 2.1.1',
    #       'Flask-WTF >= 0.14.2',
    #       'SQLAlchemy >= 1.2.6'
    #   ],
    classifiers=[  # Optional
        'License :: OSI Approved :: MIT License',
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3.6',
    ],
    project_urls={  # Optional
        'Source': 'https://rseichter@bitbucket.org/rseichter/bootini-star.git',
    },
)
