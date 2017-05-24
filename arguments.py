''' Parseador de argumentos da linha de comando '''
import argparse

parser = argparse.ArgumentParser(description="Candida Interface")
parser.add_argument("-a", help="Application to search", type=str)

def parse_arguments():
  ''' Executa o parseamento '''
  args = parser.parse_args()
  return args
