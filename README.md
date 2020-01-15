## Instructions

1. Install Python 3 from the [Official Python page](https://www.python.org/downloads/);
2. Git clone the project and cd to it: `git clone https://github.com/SerhiiAksiutin/serhii-jitterbit-interview.git && cd serhii-jitterbit-interview`;
3. Create virtual environment by running `python3 -m venv venv`;
4. Activate your environment and verify the location by executing `source venv/bin/activate && which python`;
5. Install Selenium using `pip install -U selenium`;
6. Install WebDriver manager by `pip install webdrivermanager`;
7. Get webdrivers by `webdrivermanager firefox chrome --linkpath /usr/local/bin`;
8. To execute tests run `python tests/tests.py`.