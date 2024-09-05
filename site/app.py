import libs.DataBase as db 
import os






def carregar_frases():
    with open("{}/frases_start.csv".format(os.getcwd()), 'r') as arquivo:
        for (key,linha) in enumerate(arquivo):
            if(key > 0):
                linha_separada =linha.strip().split(",")
                db.insert_frase(linha_separada[0],linha_separada[1],linha_separada[2])



if __name__ == "__main__":
    db.create_table()
    carregar_frases()


