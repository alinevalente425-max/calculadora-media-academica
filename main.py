import customtkinter as ctk
#CONFIGURAR O MODO
ctk.set_appearance_mode('dark')
#Criando tela inicial
app = ctk.CTk()
#pra adicioanar titulo
app.title('Calculadora de media')
#definindo tamanho da tela
app.geometry('300x300')
#criando campos
label = ctk.CTkLabel(app, text="")
label1 = ctk.CTkLabel(app, text="")

def media_nota():
  try:

    N1 = float(caixa_nota1.get().replace(',', '.'))
    N2 = float(caixa_nota2.get().replace(',', '.'))
    N3 = float(caixa_nota3.get().replace(',', '.'))
    media = (N1+N2+N3)/3
    if media>=6:
     label1.configure(text=f"Média: {media:.2f}")   
     label1.pack(pady=10)
     label.configure(text="Aprovado")
     label.pack()
    else:
      label1.configure(text=f"Média: {media: .2f}")
      label1.pack(pady=10)
      label.configure(text="Reprovado")
      label.pack()
  except:
    label.configure(text="Por favor, utilize apenas números nos campos")
    label.pack()
    label1.configure(text="")
    label1.pack()

#entry - campo

caixa_nota1 = ctk.CTkEntry(app, placeholder_text='Digite nota 1:')
caixa_nota1.pack(pady=10)
caixa_nota2 = ctk.CTkEntry(app, placeholder_text='Digite nota 2:')
caixa_nota2.pack(pady=10)
caixa_nota3 = ctk.CTkEntry(app, placeholder_text='Digite nota 3:')
caixa_nota3.pack(pady=10)
#Botão
botao_calcular = ctk.CTkButton(app, text='Calcular', command=media_nota)
botao_calcular.pack()

#O programa entra em estado de espera, reagindo aos cliques e movimentos do mouse.
app.mainloop()







