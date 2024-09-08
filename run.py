class Scanner:
    def __init__(self, input_stream):
        self._input_stream = input_stream

    def scan(self):
        pass


class Parser:
    def __init__(self):
        pass

    def parse(self, scanner, builder):
        pass


class ProgramNodeBuilder:
    def __init__(self):
        self._node = None

    def new_variable(self, variable_name):
        return ProgramNode()

    def new_assignment(self, variable, expression):
        return ProgramNode()

    def new_return_statement(self, value):
        return ProgramNode()

    def new_condition(self, condition, true_part, false_part):
        return ProgramNode()

    def get_root_node(self):
        return self._node


class ProgramNode:
    def __init__(self):
        self._children = []

    def get_source_position(self, line, index):
        pass

    def add(self, node):
        self._children.append(node)

    def remove(self, node):
        self._children.remove(node) 

    def traverse(self, code_generator):
        code_generator.visit(self)
        for child in self._children:
            child.traverse(code_generator)


class CodeGenerator:
    def __init__(self, output_stream):
        self._output = output_stream

    def visit(self, node):
        pass 


class ExpressionNode(ProgramNode):
    def traverse(self, code_generator):
        code_generator.visit(self)
        for child in self._children:
            child.traverse(code_generator)


class Compiler:
    def __init__(self):
        pass

    def compile(self, input_stream, output_stream):
        scanner = Scanner(input_stream)
        builder = ProgramNodeBuilder()
        parser = Parser()

        parser.parse(scanner, builder)
        generator = CodeGenerator(output_stream)

        parse_tree = builder.get_root_node()
        parse_tree.traverse(generator)
