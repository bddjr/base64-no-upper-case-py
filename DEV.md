## Windows

require python >= 3.12

test:
```
py test.py
```

build:
```
py -m build
```

publish to TestPyPI:
```
py -m twine upload --repository testpypi dist/*
```

publish to PyPI:
```
py -m twine upload dist/*
```

## Other

Replace `py` to `python3` .
