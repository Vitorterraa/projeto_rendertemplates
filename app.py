from flask import Flask, render_template, request, redirect
import random
from data import lista_configuracao as listas

app = Flask(__name__)
         
         
#lista de cores para alterar o fundo do site

                                                        
#Aqui ir para todas as minhas rotas

@app.route("/")

def principal():
    cor_de_fundo = random.choice(listas.lista_cores)
    curiosidade = random.choice(listas.lista_curiosidades)
    foto = random.choice(listas.lista_fotos)
    return render_template("principal.html", cor_de_fundo_html = cor_de_fundo, curiosidade_html = curiosidade, foto_html = foto)
    
    
@app.route("/sobre", methods=["GET"])


def pagina_sobre():
    cor_de_fundo = random.choice(listas.lista_cores)
    return render_template("sobre.html", cor_de_fundo_html = cor_de_fundo)
    

@app.route("/cadastro")

def paginaCadastro():
    return render_template("cadastro.html", frases = listas.lista_curiosidades)



@app.route("/post/cadastrarfrase", methods = ["POST"])
def post_cadastrarfrase():
    frase_vinda_do_html = request.form.get("frase")
    listas.lista_curiosidades.append(frase_vinda_do_html)
    redirect("/cadastro")
    return "Frase cadastrada"

@app.route("/cadastroCores")

def paginaCores():
    return render_template("cadastro-cores.html", cores = listas.lista_cores)


@app.route("/post/cadastrarCores", methods = ["POST"])
def post_cadastrarcores():
    cor_vinda_do_html = request.form.get("cores")
    listas.lista_cores.append(cor_vinda_do_html)
    return redirect("/cadastroCores")
    

@app.route("/cores/delete/<indice_cor>", methods = ["GET"])
def delete_cores(indice_cor):

    indice_cor = int(indice_cor)

    listas.lista_cores.pop(indice_cor)

    return redirect ("/cadastroCores")

app.run(debug=True)
                                                                            
                                                                                  
                                                                                                                                                      
                                                                                  
                                                                                  
                                                                                  
                                                                                  