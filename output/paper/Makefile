SRC = superpatterns-notes.md
PDF = $(SRC:.md=.pdf)

.PHONY: all pdf check clean frontier-note alon-preprint

all: pdf frontier-note alon-preprint

pdf: $(PDF)

# Standalone preprint on quadratic universality and Alon's conjecture.
quadratic-preprint:
	mkdir -p ../pdf
	$(MAKE) SRC=quadratic-universality.md PDF=../pdf/quadratic-universality.pdf check
	pandoc -d defaults.yaml quadratic-universality.md -o ../pdf/quadratic-universality.pdf
	pandoc quadratic-universality.md --from=markdown --to=markdown_strict+tex_math_dollars+pipe_tables+fenced_code_blocks --wrap=none --standalone --template=reader.md.template --citeproc --bibliography=references.bib --csl=springer-basic-brackets.csl --metadata=link-citations:false --lua-filter=reader.lua -o ../pdf/quadratic-universality.md

alon-preprint: quadratic-preprint

# Standalone mathematical note, plus Markdown with resolved citations.
frontier-note:
	mkdir -p ../pdf
	$(MAKE) SRC=repeated-21-frontier.md PDF=../pdf/repeated-21-frontier.pdf check
	pandoc -d defaults.yaml repeated-21-frontier.md -o ../pdf/repeated-21-frontier.pdf
	pandoc repeated-21-frontier.md --from=markdown --to=markdown_strict+tex_math_dollars+pipe_tables+fenced_code_blocks --wrap=none --standalone --template=reader.md.template --citeproc --bibliography=references.bib --csl=springer-basic-brackets.csl --metadata=link-citations:false --lua-filter=reader.lua -o ../pdf/repeated-21-frontier.md

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
