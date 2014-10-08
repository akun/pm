MAKE = make
DOC_DIR = docs
SLIDE_DIR = slides

all:
	make html
	make slide

html:
	cd $(DOC_DIR) && $(MAKE) html

slide:
	cd $(SLIDE_DIR) && $(MAKE) slides

ui:
	cd $(DOC_DIR) && python -m SimpleHTTPServer

clean:
	cd $(DOC_DIR) && $(MAKE) clean
	cd $(SLIDE_DIR) && $(MAKE) clean
