import os
import re
import setuptools

# if anything wrong with setuptools, try
# python -m pip install --user --upgrade twine

# readme.md = github readme.md, 這裡可接受 markdown寫法
# 如果沒有的話，需要自己打出介紹此專案的檔案，再讓程式知道

with open("README.md", "r") as fh:
    long_description = fh.read()

def get_version(package):
    """
    Return package version as listed in `__version__` in `init.py`.
    """
    init_py = open(os.path.join('src', package, '__init__.py')).read()
    return re.search("__version__ = ['\"]([^'\"]+)['\"]", init_py).group(1)

wd_version = get_version('WeatherData')

setuptools.setup(
    name="WeatherData",
    version=wd_version,
    author="CloudyBay",
    author_email="cibi@cloudybay.com.tw",
    description="Get weather data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cloudybay/weatherdata-sdk",
    keywords=['weather', 'forecast', 'observation', 'taiwan'],
    install_requires=['pytz', 'requests', 'urllib3'],
    packages=["WeatherData"],
    package_dir={"": "src"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)