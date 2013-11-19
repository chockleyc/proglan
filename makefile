all:
	@echo "My program does not require compiling."
test:
	python -b scanner.py input.txt
clean:
	@rm -f *.pyc
