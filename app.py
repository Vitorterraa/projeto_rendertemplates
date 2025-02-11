from flask import Flask, render_template, request, redirect
import random

app = Flask(__name__)
         
         
#lista de cores para alterar o fundo do site

lista_cores = ["red",
               "blue",
               "green",
               "yellow",
               "pink",
               "purple"]

   
lista_curiosidades = [
    "Quase jogou no Real Madrid quando era criança",
    "Primeiro jogador a marcar gols em competições diferentes no mesmo ano",
    "Tem uma grande paixão por pôquer",
    "Seu nome foi inspirado no pai",
    "Fez um gol mais rápido que muitos jogadores da história"
]

lista_fotos = [
    "neymar1.webp",
    "neymar2.jpg",
    "neymar3.jfif",
    "neymar4.jfif",
    "neymar5.jpg"
]    

                                                        
#Aqui ir para todas as minhas rotas

@app.route("/")

def principal():
    cor_de_fundo = random.choice(lista_cores)
    curiosidade = random.choice(lista_curiosidades)
    foto = random.choice(lista_fotos)
    return render_template("principal.html", cor_de_fundo_html = cor_de_fundo, curiosidade_html = curiosidade, foto_html = foto)
    
    
@app.route("/sobre", methods=["GET"])


def pagina_sobre():
    cor_de_fundo = random.choice(lista_cores)
    return render_template("sobre.html", cor_de_fundo_html = cor_de_fundo)
    

@app.route("/cadastro")

def paginaCadastro():
    return render_template("cadastro.html", frases = lista_curiosidades)



@app.route("/post/cadastrarfrase", methods = ["POST"])
def post_cadastrarfrase():
    frase_vinda_do_html = request.form.get("frase")
    lista_curiosidades.append(frase_vinda_do_html)
    redirect("/cadastro")
    return "Frase cadastrada"











@app.route("/cadastroCores")

def paginaCores():
    return render_template("cadastro-cores.html", cores = lista_cores)


@app.route("/post/cadastrarCores", methods = ["POST"])
def post_cadastrarcores():
    cor_vinda_do_html = request.form.get("cores")
    lista_cores.append(cor_vinda_do_html)
    return redirect("/cadastroCores")
    





app.run(debug=True)
                                                                            
                                                                                  
                                                                                                                                                      
                                                                                  
                                                                                  
                                                                                  
                                                                                  