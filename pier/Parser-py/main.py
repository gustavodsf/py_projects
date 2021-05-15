#! /usr/bin/env python
# -*- coding: utf-8 -*-
import Parser
import sys

'''
### Passar os seguintes arqumentos
### dict => para montar o dicionário
### db   => para montar o banco de dados 
'''

if __name__ == "__main__":
	if len(sys.argv) == 2:
		Parser.Parser(sys.argv[1])
	else:
		print("..:: Erro tem que passar como parâmetro dict|db ::..")