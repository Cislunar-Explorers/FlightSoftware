"""This file specifies dependencies and other metadata for the virtual environment (venv)."""

from distutils.core import setup

INSTALL_REQUIRES = [
    "Adafruit-Blinka",
    "adafruit-circuitpython-busdevice",
    "adafruit-circuitpython-ds3231",
    "adafruit-circuitpython-fxas21002c",
    "adafruit-circuitpython-fxos8700",
    "ADS1115",
    "bitstring",
    "numba",
    "numpy",
    "pigpio",
    "psutil",
    "python-dotenv",
    "sqlalchemy",
    "uptime",
]

PI_INSTALL_REQUIRES = [
    "adafruit-circuitpython-bno055",
    "board",
    "busio",
    "picamera",
    "vcgencmd",
]

DEV_REQUIRES = ["pytest"]

DOCS_REQUIRE = ["sphinx", "sphinx-rtd-theme"]

EXTRAS = {"rpi": PI_INSTALL_REQUIRES, "dev": DEV_REQUIRES + DOCS_REQUIRE}

setup(
    name="cislunar-fsw",
    version="0.1",
    author="SSDS",
    author_email="cornellcislunarexplorers@gmail.com",
    description="Flight software for the Cislunar Explorers mission",
    python_requires=">=3.8",
    install_requires=INSTALL_REQUIRES,
    extras_require=EXTRAS,
    package_dir={"": "src"},
)
