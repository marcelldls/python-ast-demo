import ast
from dependancy import passthrough

env = {'passthrough': passthrough}

expression = ast.parse(open('expression.py').read(), mode="eval")

# print(ast.dump(expression, indent=2))

for node in ast.walk(expression):
    if isinstance(node, ast.Call):
        expr = ast.Expression(body=node)
        ast.fix_missing_locations(expr)
        res = eval(compile(expr, filename="<ast>", mode="eval"), env)
        print(f"{type(node).__name__} at line {node.lineno}, col {node.col_offset}: {res}")

print(eval(compile(expression, filename="<ast>", mode="eval"), env))
