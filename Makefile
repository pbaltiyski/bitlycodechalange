.PHONY: all run clean requirements

all: run

run:
	@python3 bcc.py

clean:
	@echo "Cleaning up..."
	@rm -f decodes_preprocessed.json
	@rm -f result.json

requirements:
	@echo "Installing Python dependencies..."
	@pip3 install -r requirements.txt
