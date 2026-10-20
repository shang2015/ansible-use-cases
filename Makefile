.PHONY: data pages build serve check
data:
	python3 scripts/extract_content.py
pages:
	python3 scripts/build_pages.py
build: pages
	mkdocs build --strict
serve: pages
	mkdocs serve
check: build
