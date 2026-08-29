SRC = superpatterns-notes.md
PDF = $(SRC:.md=.pdf)

.PHONY: pdf check clean

pdf: $(PDF)

$(PDF): $(SRC) references.bib defaults.yaml
	pandoc -d defaults.yaml $(SRC) -o $(PDF)

# Show overfull boxes (lines/equations wider than the text width) so they can be fixed.
check: $(SRC) references.bib defaults.yaml
	pandoc -s -d defaults.yaml $(SRC) -o build.tex
	@xelatex -interaction=nonstopmode build.tex > /dev/null 2>&1 || true
	@xelatex -interaction=nonstopmode build.tex > /dev/null 2>&1 || true
	@grep -n "Overfull \\\\hbox" build.log | sed 's/(.*//' || echo "no overfull boxes"
	@grep -c "Overfull \\\\hbox" build.log || true

clean:
	rm -f build.* pg-*.png $(PDF)
