#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs
import sys
import os
from wav_transcribe import wav_transcribe
sys.path.append("C:/Users/Daneel/GitHub/for-fun/top_words")
from top_words import top_words

WAV_PATH = "C:/Users/Daneel/Google Drive/Data Science/7D minuto decisivo"
candidatos = [ "sanchez", "iglesias", "rivera", "saenz" ]
num_partes = { "sanchez" : 7 ,
               "saenz" : 8 ,
               "rivera" : 7 ,
               "iglesias" : 9}
text_speech = { "sanchez" : "" ,
                "saenz" : "" ,
                "rivera" : "" ,
                "iglesias" : ""}

for candidato in candidatos:
    print "--- Discurso de " + candidato + ":"

    outfile = "minuto_decisivo_" + candidato + ".txt"
    if os.path.isfile(outfile):
        print "Cargando transcripcion de",outfile
        text_speech[candidato] = codecs.open(outfile, 'r', 'utf8').read()
    else:
        for num in range(1,num_partes[candidato]+1):
            WAV_FILE = WAV_PATH + "/" + "minuto_decisivo_" + candidato + "_" + str(num) + ".wav"
            text_speech[candidato] += " " + wav_transcribe(WAV_FILE,"es-ES")

        with codecs.open(outfile, 'w', 'utf8') as out:
            out.write("%s" % text_speech[candidato])

    print "Palabras más usadas:".decode('utf8')
    top_words(text_speech[candidato],lang="spanish")
