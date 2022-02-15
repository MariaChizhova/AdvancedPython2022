import networkx as nx


class AstGraphGenerator(object):
    def __init__(self):
        self.graph = nx.DiGraph()
        self.count = 0

    def visit(self, node):
        method = '_visit_' + node.__class__.__name__
        visitor = getattr(self, method)
        return visitor(node)

    def add_edges(self, node_from, nodes):
        for node_to in nodes:
            self.graph.add_edge(node_from, node_to)

    def _visit_arguments(self, node):
        self.graph.add_node(node, shape='box', label='arguments', fillcolor='aqua', style='filled')
        for arg in node.args:
            self.graph.add_node(arg, shape='box', label=f'Arg {arg.arg}', fillcolor='yellow', style='filled')
            self.add_edges(node, [arg])
        return [node]

    def _visit_Constant(self, node):
        self.graph.add_node(node, shape='box', label=f'Constant {node.value}', fillcolor='purple', style='filled')
        return [node]

    def _visit_For(self, node):
        self.graph.add_node(node, shape='box', label='For', fillcolor='pink', style='filled')
        self.add_edges(node, self.visit(node.target))
        self.add_edges(node, self.visit(node.iter))
        for body in node.body:
            self.add_edges(node, self.visit(body))
        return [node]

    def _visit_BinOp(self, node):
        self.graph.add_node(node, shape='box', label='BinOp', fillcolor='cyan', style='filled')
        self.add_edges(node, self.visit(node.left))
        self.add_edges(node, self.visit(node.right))
        self.count += 1
        self.graph.add_node(str(node.op) + str(self.count), shape='box', label=f'{type(node.op).__name__}',
                            fillcolor='blue', style='filled')
        self.add_edges(node, [str(node.op) + str(self.count)])
        return [node]

    def _visit_Assign(self, node):
        self.graph.add_node(node, shape='box', label='Assign', fillcolor='orange', style='filled')
        for target in node.targets:
            self.add_edges(node, self.visit(target))
        self.add_edges(node, self.visit(node.value))
        return [node]

    def _visit_Return(self, node):
        self.graph.add_node(node, shape='box', label='Return', fillcolor='red', style='filled')
        self.add_edges(node, self.visit(node.value))
        return [node]

    def _visit_FunctionDef(self, node):
        self.graph.add_node(node, shape='box', label=f'Function {node.name}', fillcolor='salmon', style='filled')
        self.add_edges(node, self.visit(node.args))
        for body in node.body:
            self.add_edges(node, self.visit(body))
        return [node]

    def _visit_List(self, node):
        self.graph.add_node(node, shape='box', label='List', fillcolor='lightblue', style='filled')
        for elt in node.elts:
            self.add_edges(node, self.visit(elt))
        return [node]

    def _visit_Subscript(self, node):
        self.graph.add_node(node, shape='box', label='Subscript', fillcolor='lightgreen', style='filled')
        self.add_edges(node, self.visit(node.value))
        self.add_edges(node, self.visit(node.slice))
        return [node]

    def _visit_Call(self, node):
        self.graph.add_node(node, shape='box', label='Call', fillcolor='lightyellow', style='filled')
        self.add_edges(node, self.visit(node.func))
        for arg in node.args:
            self.add_edges(node, self.visit(arg))
        return [node]

    def _visit_Name(self, node):
        self.graph.add_node(node, shape='box', label=f'Name {node.id}', fillcolor='violet', style='filled')
        return [node]

    def _visit_Module(self, node):
        self.graph.add_node(node, shape='box', label='Module', fillcolor='gray', style='filled')
        self.add_edges(node, self.visit(node.body[0]))
        return [node]
