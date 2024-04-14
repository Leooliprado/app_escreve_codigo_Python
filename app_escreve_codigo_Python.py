# app escreve codigo Python.19º projeto.linguagem utilizada Python

# criado por: Leonardo de Oliveira Prado
# Instagram: arduino2.0tecnologico

# Data de inicio do projeto 21/12/2023
# Data de término do projeto  22/12/2023

#************inclusão das bibliotecas
import flet
import pyautogui
import time
#************variável
TempoEspera = 2
#************app flet
def main(pagina):
    pagina.title ="app escreve codigo Python"
    pagina.window_always_on_top = True  # nao fecha o app quando é clicado fora
    pagina.window_resizable = False  # nao abre janala grandez
    pagina.window_width = 350  # dimensao app
    pagina.window_height = 450  # dimensao app
    pagina.bgcolor = "#69696969"  # cor de fundo (cinza escuro)
# ************faça isso se o botão "void setup(){" for clicado
    def print1(evento):
        time.sleep(TempoEspera)  # delay de 1 segundo
        pyautogui.write("print()")#escreve
        pyautogui.keyDown("enter")  # pressiona o enter
        pyautogui.keyUp("enter")  # solte o enter

    def while_True(evento):
        time.sleep(TempoEspera)  # delay de 1 segundo
        pyautogui.write("while True:")
        pyautogui.keyDown("enter")  # pressiona o enter
        pyautogui.keyUp("enter")  # solte o enter

    def from_import(evento):
        time.sleep(TempoEspera)  # delay de 1 segundo
        pyautogui.write("from import ")
        pyautogui.keyDown("enter")  # pressiona o enter
        pyautogui.keyUp("enter")  # solte o enter

    def import1(eveto):
        time.sleep(TempoEspera)  # delay de 1 segundo
        pyautogui.write("import ")
        pyautogui.keyDown("enter")  # pressiona o enter
        pyautogui.keyUp("enter")  # solte o enter

    def int1(evento):
        time.sleep(TempoEspera)  # delay de 1 segundo
        pyautogui.write("int(x)")
        pyautogui.keyDown("enter")  # pressiona o enter
        pyautogui.keyUp("enter")  # solte o enter

    def float1 (evento):
        time.sleep(TempoEspera)  # delay de 1 segundo
        pyautogui.write("float(y)")
        pyautogui.keyDown("enter")  # pressiona o enter
        pyautogui.keyUp("enter")  # solte o enter

    def True1(evento):
        time.sleep(TempoEspera)
        pyautogui.write("True")

    def False1(evento):
        time.sleep(TempoEspera)
        pyautogui.write("False")

    def def1(evento):
        time.sleep(TempoEspera)
        pyautogui.write("def ():")
        pyautogui.keyDown("enter")  # pressiona o enter
        pyautogui.keyUp("enter")  # solte o enter

    def if1(evento):
        time.sleep(TempoEspera)
        pyautogui.write(" if ():")
        pyautogui.keyDown("enter")  # pressiona o enter
        pyautogui.keyUp("enter")  # solte o enter


    def elseif(evento):
        time.sleep(TempoEspera)
        pyautogui.write(" elif ():")
        pyautogui.keyDown("enter")  # pressiona o enter
        pyautogui.keyUp("enter")  # solte o enter


    def else1(evento):
        time.sleep(TempoEspera)
        pyautogui.write("else:")
        pyautogui.keyDown("enter")  # pressiona o enter
        pyautogui.keyUp("enter")  # solte o enter


    def comentario_titulo(evento):
        time.sleep(TempoEspera)
        pyautogui.write("# yyyy yx xxxxxx.xº projeto.linguagem utilizada Python")
        pyautogui.keyDown("enter")  # pressiona o enter
        pyautogui.keyUp("enter")  # solte o enter
        pyautogui.keyDown("enter")  # pressiona o enter
        pyautogui.keyUp("enter")  # solte o enter
        pyautogui.write("# criado por: Leonardo de Oliveira Prado")
        pyautogui.keyDown("enter")  # pressiona o enter
        pyautogui.keyUp("enter")  # solte o enter
        pyautogui.write("# Instagram: arduino2.0tecnologico")
        pyautogui.keyDown("enter")  # pressiona o enter
        pyautogui.keyUp("enter")  # solte o enter
        pyautogui.keyDown("enter")  # pressiona o enter
        pyautogui.keyUp("enter")  # solte o enter
        pyautogui.write("# Data de inicio do projeto xx/xx/xxxx")
        pyautogui.keyDown("enter")  # pressiona o enter
        pyautogui.keyUp("enter")  # solte o enter
        pyautogui.write("# Data de término do projeto  yy/yy/yyyy")
        pyautogui.keyDown("enter")  # pressiona o enter
        pyautogui.keyUp("enter")  # solte o enter
        pyautogui.keyDown("enter")  # pressiona o enter
        pyautogui.keyUp("enter")  # solte o enter

    def comentario_explicado(evento):
        time.sleep(TempoEspera)
        pyautogui.write("#**************")
        pyautogui.keyDown("enter")  # pressiona o enter
        pyautogui.keyUp("enter")  # solte o enter


# **************intes que queremos na página com nomes e ********cores botao*******cores letra
    print1= flet.ElevatedButton("print( ) ", bgcolor="#0000FF", color="#000000", on_click=print1)
    while_True = flet.ElevatedButton("while True:", bgcolor="#0000FF", color="#000000", on_click=while_True)
    from_import = flet.ElevatedButton("from import", bgcolor="#4B0082", color="#000000", on_click=from_import)
    import1 =flet.ElevatedButton("import", bgcolor="#4B0082", color="#000000", on_click=import1)
    int1 =flet.ElevatedButton("int(x)", bgcolor="#FF8C00", color="#000000", on_click=int1)
    float1 = flet.ElevatedButton("float(y)", bgcolor="#FF8C00", color="#000000", on_click=float1)
    True1 = flet.ElevatedButton("True", bgcolor="#008000", color="#000000", on_click=True1)
    False1 = flet.ElevatedButton("False", bgcolor="#FF0000", color="#000000", on_click=False1)
    def1 = flet.ElevatedButton("def ():", bgcolor="#DC143C", color="#000000", on_click=def1)
    if1 = flet.ElevatedButton(" if ():", bgcolor="#DC143C", color="#000000", on_click=if1 )
    elseif=flet.ElevatedButton("elif ():", bgcolor="#663399", color="#000000", on_click=elseif )
    else1=flet.ElevatedButton("else:", bgcolor="#663399", color="#000000", on_click=else1)
    comentario_titulo=flet.ElevatedButton("#comentário titulo",bgcolor="#A9A9A9", color="#000000",on_click=comentario_titulo)
    comentario_explicado=flet.ElevatedButton("#comentário",bgcolor="#A9A9A9", color="#000000",on_click=comentario_explicado)
# **************adicinar os intens na página
    pagina.add(flet.Row([print1,while_True], alignment=flet.MainAxisAlignment.CENTER))
    pagina.add(flet.Row([from_import,import1],alignment=flet.MainAxisAlignment.CENTER))
    pagina.add(flet.Row([int1,float1], alignment=flet.MainAxisAlignment.CENTER))
    pagina.add(flet.Row([False1,True1], alignment=flet.MainAxisAlignment.CENTER))
    pagina.add(flet.Row([def1,if1],alignment=flet.MainAxisAlignment.CENTER))
    pagina.add(flet.Row([elseif, else1],alignment=flet.MainAxisAlignment.CENTER))
    pagina.add(flet.Row([comentario_titulo,comentario_explicado],alignment=flet.MainAxisAlignment.CENTER))


#**************forma de visualização do aplicativo (visualização app)
flet.app(target=main)
#**************forma de visualização do aplicativo (visualização web "navegador")
#flet.app(target=main,view=flet.WEB_BROWSER)
