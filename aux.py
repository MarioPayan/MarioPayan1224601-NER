def encontrarsexo (self , tag):
    salida = "C"
    if tag != "":
        if tag[0] == "A":
            if tag[3] == "F":
                salida = "F"
            elif tag[3] == "M":
                salida = "M"
            elif tag[3] == "C":
                salida = "C"
            else:
                salida = "C"

        if tag[0] == "T":
            if tag[2] == "F":
                salida = "F"
            elif tag[2] == "M":
                salida = "M"
            elif tag[2] == "C":
                salida = "C"
            else:
                salida = "C"

        if tag[0] == "D":
            if tag[3] == "F":
                salida = "F"
            elif tag[3] == "M":
                salida = "M"
            elif tag[3] == "C":
                salida = "C"
            else:
                salida = "C"

        if tag[0] == "N":
            if tag[2] == "F":
                salida = "F"
            elif tag[2] == "M":
                salida = "M"
            elif tag[2] == "C":
                salida = "C"
            else:
                salida = "C"

        if tag[0] == "V":
            if tag[6] == "F":
                salida = "F"
            elif tag[6] == "M":
                salida = "M"
            elif tag[6] == "C":
                salida = "C"
            else:
                salida = "C"

        if tag[0] == "P":
            if tag[3] == "F":
                salida = "F"
            elif tag[3] == "M":
                salida = "M"
            elif tag[3] == "C":
                salida = "C"
            else:
                salida = "C"

        if tag[0] == "M":
            if tag[2] == "F":
                salida = "F"
            elif tag[2] == "M":
                salida = "M"
            elif tag[2] == "C":
                salida = "C"
            else:
                salida = "C"

        if tag[0] == "S":
            salida = "M"
    else:
        if tag == "":
            salida = ""

    return salida

def encontrarPersona (self , tag):
    salida = "indeterminado"
    if tag != "":
        if tag[0] == "D":
            if tag[2] == "3":
                salida = "tercera"
            elif tag[2] == "2":
                salida = "segunda"
            elif tag[2] == "1":
                salida = "perimera"
            else:
                salida = "indeterminado"

        if tag[0] == "V":
            if tag[4] == "3":
                salida = "tercera"
            elif tag[4] == "2":
                salida = "segunda"
            elif tag[4] == "1":
                salida = "perimera"
            else:
                salida = "indeterminado"

        if tag[0] == "P":
            if tag[2] == "3":
                salida = "tercera"
            elif tag[2] == "2":
                salida = "segunda"
            elif tag[2] == "1":
                salida = "perimera"
            else:
                salida = "indeterminado"
    else:
        if tag == "":
            salida = ""

    return salida

def encontrarNumero (self , tag):
    salida = "indeterminado"
    if tag != "":
        if tag[0] == "A":
            if tag[4] == "P":
                salida = "plural"
            elif tag[4] == "S":
                salida = "singular"
            else:
                salida = "invariable"

        if tag[0] == "T":
            if tag[3] == "P":
                salida = "plural"
            elif tag[3] == "S":
                salida = "singular"
            else:
                salida = "invariable"

        if tag[0] == "D":
            if tag[4] == "P":
                salida = "plural"
            elif tag[4] == "S":
                salida = "singular"
            else:
                salida = "invariable"

        if tag[0] == "N":
            if tag[3] == "P":
                salida = "plural"
            elif tag[3] == "S":
                salida = "singular"
            else:
                salida = "invariable"

        if tag[0] == "V":
            if tag[5] == "P":
                salida = "plural"
            elif tag[5] == "S":
                salida = "singular"
            else:
                salida = "invariable"

        if tag[0] == "P":
            if tag[4] == "P":
                salida = "plural"
            elif tag[4] == "S":
                salida = "singular"
            else:
                salida = "invariable"

        if tag[0] == "M":
            if tag[3] == "P":
                salida = "plural"
            elif tag[3] == "S":
                salida = "singular"
            else:
                salida = "invariable"
    else:
        if tag == "":
            salida = ""

    return salida

def encontrarTipo (self , tag):
    salida = "No_Es_Un_Sustantivo"
    if -1 < tag.find("NC"):
        return "Comun"
    if -1 < tag.find("NP"):
        return "Propio"
    if tag == "":
        return ""
    return salida