#! /usr/bin/env python
# -*- coding: utf-8 -*-
import  ReadFile

class CsvParser:

	def parserForNltk(self,path):
		words = ""
		read = ReadFile.ReadFile()
		lines = read.readCsvFile(path)
		line = lines.readline()
		while line:
		    if "Código" in line:
		    	line = lines.readline()
		    	while "Destino" not in line:
		    		line = line.replace("\n","")
		    		words = words +" "+ line 
		    		line = lines.readline()
		    line = lines.readline()
		lines.close()
		return words
