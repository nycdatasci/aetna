# Fill in ellipsis (and delete the #'s):
# @outputSchema("...")
# def to_hours(hours):
#   return ...

@outputSchema("facilities:chararray")
def concat(str):
  return str+str

@outputSchema("euros:double")
def cvtToEuros(dollars):
  return dollars * 0.91
