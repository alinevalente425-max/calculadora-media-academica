import customtkinter as ctk
#CONFIGURAR O MODO
ctk.set_appearance_mode('dark')
#Criando tela inicial
app = ctk.CTk()
#pra adicioanar titulo
app.title('Calculadora de media')
#definindo tamanho da tela
app.geometry('300x300')
#O programa entra em estado de espera, reagindo aos cliques e movimentos do mouse.
#criando campos
#label - caixa de texto
#campo_nota1 = ctk.CTkLabel(app, text='Nota 1?')
#Espaço
#label_nota1.pack(pady=10)
def media_nota():
  try:

    N1 = float(caixa_nota1.get().replace(',', '.'))
    N2 = float(caixa_nota2.get().replace(',', '.'))
    N3 = float(caixa_nota3.get().replace(',', '.'))
    media = (N1+N2+N3)/3
    if media>=6:
        label = ctk.CTkLabel(app, text='Aprovado')
        label.pack(pady=10)
        label1 = ctk.CTkLabel(app, text= media)
        label1.pack()
    else:
        label2 = ctk.CTkLabel(app, text='Reprovado')
        label2.pack(pady=10)
        label3 = ctk.CTkLabel(app, text= media)
        label3.pack()
  except:

    label9 = ctk.CTkLabel(app, text='Preencha os campos apenas com números!')
    label9.pack()

#entry - campo

caixa_nota1 = ctk.CTkEntry(app, placeholder_text='Digite nota 1:')
caixa_nota1.pack(pady=10)
caixa_nota2 = ctk.CTkEntry(app, placeholder_text='Digite nota 2:')
caixa_nota2.pack(pady=10)
caixa_nota3 = ctk.CTkEntry(app, placeholder_text='Digite nota 3:')
caixa_nota3.pack(pady=10)
botao_calcular = ctk.CTkButton(app, text='Calcular', command=media_nota)
botao_calcular.pack(pady=10)

app.mainloop()







