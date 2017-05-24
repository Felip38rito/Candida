#!/usr/bin/python3

''' Interface principal do Candida '''
from arguments import parse_arguments

# processo a entrada e o help
cli_arguments = parse_arguments()
print("*** Candida ***")

if cli_arguments.a != None:
  print("* Procurando por '%s' *" % cli_arguments.a)
else:
  print("Use -a to say what software you want to remove")
  print("Use -h for help")
  

