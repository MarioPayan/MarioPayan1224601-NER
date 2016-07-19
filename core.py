#!/usr/bin/env python
# -*- coding: utf-8 -*-
# converting a unknown formatting file in utf-8

import subprocess
import os, sys
import  re, os, shlex,getopt
import codecs
import json
import freeling

from aux import encontrarsexo
from aux import encontrarPersona
from aux import encontrarNumero
from aux import encontrarTipo

from apt.package import unicode

FREELINGDIR = '/usr/local'
DATA = FREELINGDIR + '/share/freeling/'
LANGUAGE = 'es'
freeling.util_init_locale('default')
option = freeling.maco_options(LANGUAGE)
option.set_data_files( "", DATA + "common/punct.dat", DATA + LANGUAGE + "/dicc.src", DATA + LANGUAGE + "/afixos.dat", "", DATA + LANGUAGE + "/locucions.dat", DATA + LANGUAGE + "/np.dat", DATA + LANGUAGE + "/quantities.dat", DATA + LANGUAGE + "/probabilitats.dat")
morfo = freeling.maco(option)
tokenizer = freeling.tokenizer(DATA + LANGUAGE + '/tokenizer.dat')
splitter = freeling.splitter(DATA + LANGUAGE + '/splitter.dat')
sid = splitter.open_session()
tagger = freeling.hmm_tagger(DATA + LANGUAGE + '/tagger.dat', True, 2)
parser = freeling.chart_parser(DATA + LANGUAGE + '/chunker/grammar-chunk.dat')
morfo.set_active_options(False, True, True, True, True, True, False, True, True, True, True, True )


class analizar():

    def run (self):
        resumen = []
        print ("\n--------------------------------------------------------------------------------\n")
        #-----------------------------------------------------------------------------------------------
        print ("Los Datos Obtenidos (precision, recall , FB1) por el MODELO BASE son los siguientes: \n")
        process = subprocess.Popen('perl conlleval.pl -r -o NOEXIST < ' + "modelo_base/salida.txt", shell=True, stdout=subprocess.PIPE)
        for line in process.stdout:
            line = line.rstrip()
            line = str(line).replace("b","",1)
            if line[1] == "a":
                resumen.append(line[1:-1])
            print (line[1:-1])
        print ("\n--------------------------------------------------------------------------------\n")

        print ("Datos obtenidos (precision, recall , FB1) por el MODELO 1 \n")
        process = subprocess.Popen('perl conlleval.pl -r -o NOEXIST < ' + "modelo1/salida.txt", shell=True, stdout=subprocess.PIPE)
        for line in process.stdout:
            line = line.rstrip()
            line = str(line).replace("b","",1)
            if line[1] == "a":
                resumen.append(line[1:-1])
            print (line[1:-1])
        print ("\n--------------------------------------------------------------------------------\n")

        print ("Datos obtenidos (precision, recall , FB1) por el MODELO 2 \n")
        process = subprocess.Popen('perl conlleval.pl -r -o NOEXIST < ' + "modelo2/salida.txt", shell=True, stdout=subprocess.PIPE)
        for line in process.stdout:
            line = line.rstrip()
            line = str(line).replace("b","",1)
            if line[1] == "a":
                resumen.append(line[1:-1])
            print (line[1:-1])
        print ("\n--------------------------------------------------------------------------------")

        print ("Datos obtenidos (precision, recall , FB1) por el MODELO 3 \n")
        process = subprocess.Popen('perl conlleval.pl -r -o NOEXIST < ' + "modelo3/salida.txt", shell=True, stdout=subprocess.PIPE)
        for line in process.stdout:
            line = line.rstrip()
            line = str(line).replace("b","",1)
            if line[1] == "a":
                resumen.append(line[1:-1])
            print (line[1:-1])
        print ("\n--------------------------------------------------------------------------------")

        print ("Datos obtenidos (precision, recall , FB1) por el MODELO 4 \n")
        process = subprocess.Popen('perl conlleval.pl -r -o NOEXIST < ' + "modelo4/salida.txt", shell=True, stdout=subprocess.PIPE)
        for line in process.stdout:
            line = line.rstrip()
            line = str(line).replace("b","",1)
            if line[1] == "a":
                resumen.append(line[1:-1])
            print (line[1:-1])
        print ("\n--------------------------------------------------------------------------------")

        print ("Datos obtenidos (precision, recall , FB1) por el MODELO 5 \n")
        process = subprocess.Popen('perl conlleval.pl -r -o NOEXIST < ' + "modelo5/salida.txt", shell=True, stdout=subprocess.PIPE)
        for line in process.stdout:
            line = line.rstrip()
            line = str(line).replace("b","",1)
            if line[1] == "a":
                resumen.append(line[1:-1])
            print (line[1:-1])
        print ("\n--------------------------------------------------------------------------------")

        print("Resumen:")
        resumenArreglado = ["    Modelo - Precision - Recall - F-score"]
        for line in resumen:
            line = line.split(" ")
            line_fixed = " -   " + line[2][:-1] + "  - " + line[5][:-1] + " -  " + line[8][:-1]
            resumenArreglado.append(line_fixed)

        resumenArreglado[1] = "   modeloB" + resumenArreglado[1]
        resumenArreglado[2] = "   modelo1" + resumenArreglado[2]
        resumenArreglado[3] = "   modelo2" + resumenArreglado[3]
        resumenArreglado[4] = "   modelo3" + resumenArreglado[4]
        resumenArreglado[5] = "   modelo4" + resumenArreglado[5]
        resumenArreglado[6] = "   modelo5" + resumenArreglado[6]

        for line in resumenArreglado:
            print(line)

    def modelo1 (self, fileIn, archivoEntradaModificado):
        fichero =  open(fileIn, 'r+', encoding='latin-1')
        modelo =  open(archivoEntradaModificado, 'w+')
        for line in fichero:
            line = line.replace("\n", "")
            line = line.split(" ")
            s = " "
            if len(line) > 1:
                mayus = 1 if str(line[0][0]).isupper() else 0 
                lineOut = str(line[0]) + s + str(line[1]) + s + str(mayus) + s + str(line[2])
                modelo.write(lineOut + "\n")
                print (str(lineOut))
        fichero.close()
        modelo.close()

    def modelo2 (self, archivoEntrada, archivoEntradaModificado, ArchivoTagger):
        fichero = open(archivoEntrada, 'r+', encoding='latin-1')
        modelo = open(archivoEntradaModificado, 'w+')
        tager = open(ArchivoTagger , 'r+', encoding='latin-1')
        tagArray = []

        for line_tager in tager:
            line_tager = line_tager.replace("\n", "")
            line_tager = line_tager.split()
            if len(line_tager) > 1:
                tagArray.append(line_tager[1]) 
        count = 0
        for line in fichero:  
            line = line.replace("\n", "")
            line = line.split(" ")
            s = " "
            tipo = self.encontrarTipo(tagArray[count])
            lineOut = line[0] + s + line[1] + s + line[2] + s + tipo + s + line[3]
            modelo.write(lineOut + "\n")
            count += 1
            print (str(lineOut))
        fichero.close()
        modelo.close()

    def modelo3 (self, archivoEntrada, archivoEntradaModificado, ArchivoTagger):
        fichero = open(archivoEntrada, 'r+', encoding='latin-1')
        modelo = open(archivoEntradaModificado, 'w+')
        tager = open(ArchivoTagger , 'r+', encoding='latin-1')
        tagArray = []

        for line_tager in tager:
            line_tager = line_tager.replace("\n", "")
            line_tager = line_tager.split()
            if len(line_tager) > 1:
                tagArray.append(line_tager[1]) 
        count = 0
        for line in fichero:  
            line = line.replace("\n", "")
            line = line.split(" ")
            s = " "
            sexo = self.encontrarsexo(tagArray[count])
            lineOut = line[0] + s + line[1] + s + line[2] + s + line[3] + s + sexo + s + line[4]
            modelo.write(lineOut + "\n")
            count += 1
            print (str(lineOut))
        fichero.close()
        modelo.close()

    def modelo4 (self, archivoEntrada, archivoEntradaModificado, ArchivoTagger):
        fichero = open(archivoEntrada, 'r+', encoding='latin-1')
        modelo = open(archivoEntradaModificado, 'w+')
        tager = open(ArchivoTagger , 'r+', encoding='latin-1')
        tagArray = []

        for line_tager in tager:
            line_tager = line_tager.replace("\n", "")
            line_tager = line_tager.split()
            if len(line_tager) > 1:
                tagArray.append(line_tager[1]) 
        count = 0
        for line in fichero:  
            line = line.replace("\n", "")
            line = line.split(" ")
            s = " "
            numero = self.encontrarNumero(tagArray[count])
            lineOut = line[0] + s + line[1] + s + line[2] + s + line[3] + s + line[4] + s + numero + line[5]
            modelo.write(lineOut + "\n")
            count += 1
            print (str(lineOut))
        fichero.close()
        modelo.close()

    def modelo5 (self, archivoEntrada, archivoEntradaModificado, ArchivoTagger):
        fichero = open(archivoEntrada, 'r+', encoding='latin-1')
        modelo = open(archivoEntradaModificado, 'w+')
        tager = open(ArchivoTagger , 'r+', encoding='latin-1')
        tagArray = []

        for line_tager in tager:
            line_tager = line_tager.replace("\n", "")
            line_tager = line_tager.split()
            if len(line_tager) > 1:
                tagArray.append(line_tager[1]) 
        count = 0
        for line in fichero:  
            line = line.replace("\n", "")
            line = line.split(" ")
            s = " "
            persona = self.encontrarPersona(tagArray[count])
            lineOut = line[0] + s + line[1] + s + line[2] + s + line[3] + s + line[4] + s + line[5] + persona + line[6]
            modelo.write(lineOut + "\n")
            count += 1
            print (str(lineOut))
        fichero.close()
        modelo.close()

analizador = analizar()
analizador.run()