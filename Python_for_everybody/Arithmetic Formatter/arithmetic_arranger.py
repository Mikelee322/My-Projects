import re #RegEx for error handling
def arithmetic_arranger(problems):
  if len(problems) >5:
    return "Error:To many problems."
    
  arranged_problems = ""

  for index, value in enumerate(problems):
    #["45", "+", "9"]
    operation = value.split("")
    
    if operation[1] not in "+-":
      return "Error: Operator must be '+' or '-'."

    if len(operation[0]) > 4 or len(operation[2]) > 4:
      return "len(operator[0]) > 4"

    try:
      value_1 = int(operation[0])
      value_2 = int(operation[2])
    except ValueError:
      return "Error: Numbers must only contain digits."

    pilot_problem = f"""
    {value_1}
    {operation[1]} {value_2}
    ----
    """

    arranged_problems += pilot_problem
    
    return arranged_problems