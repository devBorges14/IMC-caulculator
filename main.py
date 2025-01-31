import customtkinter

# Criar e configurar janela
customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green
janela = customtkinter.CTk()  # Criando a janela
janela.geometry("500x600")  # Tamanho da janela 
janela.title("Calculadora de IMC")  # Título da janela

# Adicionando componentes
titulo = customtkinter.CTkLabel(janela, text="Calculadora de IMC", font=("Helvetica", 28, "bold"), text_color="white")  # Titulo mais elegante
titulo.pack(padx=10, pady=20)

# Entrada de Peso
input_peso = customtkinter.CTkEntry(janela, placeholder_text="Digite o seu peso", width=300, height=40, font=("Arial", 16), border_width=2, corner_radius=10)
input_peso.pack(padx=10, pady=10)

texto_em_quilos = customtkinter.CTkLabel(janela, text="(em quilos)", font=("Arial", 12), text_color="white")
texto_em_quilos.pack(pady=5)

# Entrada de Altura
input_altura = customtkinter.CTkEntry(janela, placeholder_text="Digite a sua altura", width=300, height=40, font=("Arial", 16), border_width=2, corner_radius=10)
input_altura.pack(padx=10, pady=10)

texto_em_centimetros = customtkinter.CTkLabel(janela, text="(em centímetros)", font=("Arial", 12), text_color="white")
texto_em_centimetros.pack(pady=5)

# Função para calcular IMC
def calcular_imc():
    try:
        peso = float(input_peso.get())
        altura = float(input_altura.get()) / 100  # Convertemos a altura para metros
    except ValueError:
        # Caso o usuário não tenha inserido um valor válido
        texto_resultado.configure(text="Por favor, insira valores válidos para peso e altura.", text_color="red")
        return

    # Calculando o IMC
    imc = peso / (altura ** 2)
    
    # Definindo a categoria do IMC
    if imc < 18.5:
        resultado = "Abaixo do peso"
    elif imc < 25:
        resultado = "Peso normal"
    elif imc < 30:
        resultado = "Sobrepeso"
    elif imc < 40:
        resultado = "Obesidade"
    else:
        resultado = "Obesidade grave"

    # Exibir o resultado
    texto_resultado.configure(text=f"De acordo com seu peso: {peso}kg\n e sua altura: {altura*100}cm,\n você está: {resultado}", text_color="white")

# Botão para calcular
botao_converter = customtkinter.CTkButton(janela, text="Calcular", command=calcular_imc, width=300, height=50, font=("Arial", 18), corner_radius=10, fg_color="#4CAF50", hover_color="#45a049")
botao_converter.pack(pady=20)

# Texto para exibir o resultado
texto_resultado = customtkinter.CTkLabel(janela, text="", font=("Arial", 16), text_color="white")
texto_resultado.pack(padx=10, pady=10)

# Rodar Janela
janela.mainloop()
