from shovel import task
from subprocess import call

@task
def docs():
    call(["pdflatex",
          "-output-directory=docs",
          "-shell-escape",
          "docs/gramz.tex"])

@task
def test():
    call(["nosetests"])
