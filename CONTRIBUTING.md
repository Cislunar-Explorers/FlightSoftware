# Contributing

## Getting Started

Create a virtual Python environment and install all the necessary dependencies. Make sure you run this from the root of the repository!

```bash
python -m venv venv
source venv/bin/activate
pip install -e ."[rpi, dev]" # or just [dev]
```

You can exit this environment by running `deactivate`. To re-enter an existing environment, all you need is `source venv/bin/activate`.  

*Note: Some problems have been known to occur if your [pip](https://pypi.org/project/pip/) is not updated. Follow the warning prompt your terminal gives if this happens.*