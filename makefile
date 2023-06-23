init:
	pip install -r requirements.txt
	python -m spacy download en_core_web_md
	python -m spacy_entity_linker "download_knowledge_base"
	pip install --upgrade build
	pip install --upgrade twine

test:
	pytest -v -s tests

build:
	rm -rf dist/
	python -m build
	python -m twine upload --repository pypi dist/*
	
requirements:
	pipreqs --savepath=requirements.in && pip-compile
	rm requirements.in
