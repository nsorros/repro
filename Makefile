VIRTUALENV := venv

virtualenv:
	@if [ -d $(VIRTUALENV) ]; then rm -rf $(VIRTUALENV); fi
	python3 -m venv $(VIRTUALENV)
	$(VIRTUALENV)/bin/pip install --upgrade pip
	$(VIRTUALENV)/bin/pip install -r requirements.txt
        
