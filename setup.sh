echo "rm -rf old dist"
rm -rf dist
echo "run: python setup.py sdist bdist_wheel"
python setup.py sdist bdist_wheel
echo "run: test pypi"
twine upload --repository-url https://test.pypi.org/legacy/ dist/*
echo "run: upload!"
twine upload dist/*