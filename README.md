# Variant960
The Variant960 analysis monsieur fables (https://github.com/fjscabral) and I did.

run the part 1 first, it will generate several files
python main.py

You can also change the lines in the part 1\main.py

file_name="n"+str(j).zfill(3)+".pgn"
 for i in range(960):
        j=j+1
        if j == 64:
            j=0
            file_name="n"+str(i).zfill(3)+".pgn"
to look like 

file_name="unique.pgn"
 for i in range(960):
//delete the ones below

in order to generate a unique pgn
or simply do the command on linux:

cat *.pgn > unique.pgn

or copy paste all into one single pgn

part 2

copy the template.tex file and name it final.tex
edit the first parts to your taste:
Name of the document,
Name of the author,
etc etc

after executing the script with the simple 'python main.py' 
you will need to add \end{document} at the end of the final.tex file generated

packages required for latex on ubuntu:
tex-common/focal,focal,now 6.13 all [installed,automatic]
tex-gyre/focal,focal,now 20180621-3 all [installed,automatic]
texinfo/focal,now 6.7.0.dfsg.2-5 amd64 [installed]
texlive-base/focal,focal,now 2019.20200218-1 all [installed]
texlive-binaries/focal,now 2019.20190605.51237-3build2 amd64 [installed,automatic]
texlive-fonts-recommended/focal,focal,now 2019.20200218-1 all [installed,automatic]
texlive-games/focal,focal,now 2019.202000218-1 all [installed]
texlive-latex-base/focal,focal,now 2019.20200218-1 all [installed,automatic]
texlive-latex-extra/focal,focal,now 2019.202000218-1 all [installed]
texlive-latex-recommended/focal,focal,now 2019.20200218-1 all [installed,automatic]
texlive-pictures/focal,focal,now 2019.20200218-1 all [installed,automatic]
texlive-plain-generic/focal,focal,now 2019.202000218-1 all [installed,automatic]
texlive/focal,focal,now 2019.20200218-1 all [installed]


after the final.tex file is generated

run the command:
texi2pdf final.tex

Some versions might require the command to be executed 2 or 3 times (for the correct index)
