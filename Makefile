all: presentation-1.pdf presentation-2.pdf

.SUFFIXES: .tex .pdf

.tex.pdf:
	pdflatex $? && pdflatex $?
