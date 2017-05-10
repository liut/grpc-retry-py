.SILENT :
.PHONY : build clean upload

build:
	python setup.py sdist bdist_wheel

clean:
	@find . -name '*.pyc' -type f -delete
	@find . -name '__pycache__' -type d -delete
	@find . -type d -empty -delete
	rm -rf build dist *.egg-info

upload:
	devpi use guihua/edge
	devpi upload dist/*
