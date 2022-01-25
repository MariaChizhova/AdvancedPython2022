import networkx as nx
import ast
from AstGraphGenerator import AstGraphGenerator
import os


def create_plot(code, dirname, filename):
    if not os.path.exists(dirname):
        os.mkdir(dirname)
    v = AstGraphGenerator()
    ast_object = ast.parse(code)
    v.visit(ast_object)
    nx.drawing.nx_pydot.to_pydot(v.graph).write_png(os.path.join(dirname, filename))


if __name__ == '__main__':
    code = """def get_fib(n):
           fib = [0] * n
           fib[0] = fib[1] = 1
           for i in range(2, n):
               fib[i] = fib[i - 1] + fib[i - 2]
           return fib"""
    create_plot(code, 'artifacts', 'graph.png')
