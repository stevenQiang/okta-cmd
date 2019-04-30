from setuptools import setup, find_packages

setup(
    name = "okta-cmd",
    version = "0.0.1",
    keywords = ("pip", "okta", "cli", "cmd", "steven"),
    description = "okta cli",
    long_description = "cusmom okta cli",
    license = "MIT Licence",

    url = "https://github.com/stevenQiang/okta-cmd",
    author = "steven",
    author_email = "qianggao7@gmail.com",

    packages = find_packages(),
    include_package_data = True,
    install_requires = ["requests"],
    platforms = "any",

    scripts = [],
    entry_points = {
        'console_scripts': [
            'okta-cmd=oktacmd.main:main'
        ]
    }
)
