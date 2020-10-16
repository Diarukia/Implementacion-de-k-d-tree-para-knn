from classes.main import _main_
import sys

if( __name__ == '__main__'):
	arguments = sys.argv
	arguments.pop(0)# 3 parametros [,,fila a comparar]
	_main_(arguments)