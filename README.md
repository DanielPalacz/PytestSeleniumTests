# PytestSeleniumTests
***
***
### A. Requirements
python 3.8 version (tested with: Python 3.8.10)
Unix-like OS (tested with Ubuntu 20.04.2 LTS)
Google Chrome browser (tested with older version)
***

### B. Environment setup
* clone repository:
* - git@github.com:DanielPalacz/PytestSeleniumTests.git
* create virtual env
* - python3 -m venv local_env
* - source local_env/bin/activate
* - pip install -r requirements.txt
* download chromedriver binary and copy to local_env/bin/ directory
***

### C. Test execution
* From the repository directory:
* - pytest -s -vv tests/ --html=report.html --self-contained-html
