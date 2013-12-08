all:
	@echo "My program does not require compiling."
test:
	python -b scanner.py input.txt
testrec:
	python -b recTest.py input.txt
fulltest:
	python -b test.py input.txt
clean:
	@rm -f *.pyc
