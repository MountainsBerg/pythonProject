import ast

BAD_ATS = {
  ast.Attribute,
  ast.Subscript,
  ast.comprehension,
  ast.Delete,
  ast.Try,
  ast.For,
  ast.ExceptHandler,
  ast.With,
  ast.Import,
  ast.ImportFrom,
  ast.Assign,
  ast.AnnAssign,
  ast.Constant,
  ast.ClassDef,
  ast.AsyncFunctionDef,
}

BUILTINS = {
    "bool": bool,
    "set": set,
    "tuple": tuple,
    "round": round,
    "map": map,
    "len": len,
    "bytes": bytes,
    "dict": dict,
    "str": str,
    "all": all,
    "range": range,
    "enumerate": enumerate,
    "int": int,
    "zip": zip,
    "filter": filter,
    "list": list,
    "max": max,
    "float": float,
    "divmod": divmod,
    "unicode": str,
    "min": min,
    "range": range,
    "sum": sum,
    "abs": abs,
    "sorted": sorted,
    "repr": repr,
    "object": object,
    "isinstance": isinstance
}



def is_safe(code):
  if type(code) is str and "__" in code:
    return False

  for x in ast.walk(compile(code, "<QWB7th>", "exec", flags=ast.PyCF_ONLY_AST)):
    if type(x) in BAD_ATS:
      return False

  return True


if __name__ == "__main__":
  user_input = ""
  while True:
    line = input()
    if line == "":
      break
    user_input += line
    user_input += "\n"

  if is_safe(user_input) and len(user_input) < 1800:
    exec(user_input, {"__builtins__": BUILTINS}, {})