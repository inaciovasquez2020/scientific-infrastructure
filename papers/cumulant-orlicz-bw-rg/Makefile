PDF=main.pdf
TEX=main.tex

all: $(PDF)

$(PDF): $(TEX)
	pdflatex -interaction=nonstopmode main.tex
	pdflatex -interaction=nonstopmode main.tex

clean:
	rm -f *.aux *.log *.out *.toc *.pdf
