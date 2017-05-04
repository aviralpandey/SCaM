all: presentation-1.pdf presentation-2.pdf presentation-3.pdf

.SUFFIXES: .tex .pdf

.tex.pdf:
	pdflatex $? && pdflatex $?
