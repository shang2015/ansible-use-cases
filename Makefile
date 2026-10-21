.PHONY: data resources pages build serve check pdfs
data:
	python3 scripts/extract_content.py
resources:
	python3 scripts/resource_index.py
	python3 scripts/check_groups.py
pdfs:
	python3 scripts/build_pdfs.py
pages:
	python3 scripts/build_pages.py
build: pages
	mkdocs build --strict
serve: pages
	mkdocs serve
check: build
