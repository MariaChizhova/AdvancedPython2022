from astgraphplot.main import create_plot
import os


def fill_missing_values(cols: int):
    return lambda lst, length=cols: map(lambda l: l + [''] * (length - len(l)), lst)


def generate_latex_table(table):
    cols = max(map(len, table))
    x = '{|' + cols * 'c|' + '}'
    begin = [f"\\begin{{tabular}}{x}"]
    table = ["\\hline\n",
             '\\\\ \\hline\n'.join(map(lambda row: '&'.join(map(str, row)), fill_missing_values(cols)(table))),
             "\\\\ \\hline"]
    end = ["\\end{tabular}"]
    return ['\n'.join(begin + table + end), '\n']


def generate_latex_image(path):
    return [f"\\includegraphics[width=\\textwidth]{{{path}}}"]


def generate_latex(table, path) -> str:
    preamble = ["\\documentclass{article}", "\\usepackage[english]{babel}", "\\usepackage{graphicx}",
                "\\begin{document}"]
    table = generate_latex_table(table)
    image = generate_latex_image(path)
    end = ["\\end{document}"]
    return '\n'.join(preamble + table + image + end)


if __name__ == '__main__':
    data = [["Advanced", "Python"], [16, 2, 2022], [1, 2, 3, 4, 5]]
    create_plot("artifacts", "graph.png")
    file = open("artifacts/hw2.tex", "w")
    file.write(generate_latex(data, "artifacts/graph.png"))
    file.close()
    os.system("pdflatex -halt-on-error -output-directory artifacts artifacts/hw2.tex")
    os.remove("artifacts/hw2.aux")
    os.remove("artifacts/hw2.log")
    os.remove("artifacts/graph.png")
