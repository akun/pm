MAKE = make
DOC_DIR = docs
SLIDE_DIR = slides
ONEPIECE_DIR = pm/onepiece

.PHONY: all install test html slide ui clean

all:
	make install
	make html
	make slide
	make test

install:
	pip install -r requirements.txt
	cd $(ONEPIECE_DIR) && pip install -e .[test]

test:
	cd $(ONEPIECE_DIR) && tox

html:
	cd $(DOC_DIR) && $(MAKE) html

slide:
	cd $(SLIDE_DIR) && $(MAKE) slides

ui:
	cd $(DOC_DIR) && python -m SimpleHTTPServer

clean:
	cd $(DOC_DIR) && $(MAKE) clean
	cd $(SLIDE_DIR) && $(MAKE) clean
	cd $(ONEPIECE_DIR) && rm -rf *.egg-info .tox
	find $(ONEPIECE_DIR) -name '*.pyc' | xargs rm -f
	find $(ONEPIECE_DIR) -name '__pycache__' | xargs rm -rf
