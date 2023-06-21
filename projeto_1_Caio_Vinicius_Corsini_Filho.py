#----------------------------------------------------------------------------------------------------------------------------------------------
"""  Projeto 1       Caio Vinicius Corsini Filho    TIA: 32344430   Curso: Ciência da Computação    Universidade: Mackenzie    Turma: 01P11 """
#----------------------------------------------------------------------------------------------------------------------------------------------




#----------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------PARTE A---------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------

#Importar math para usar raiz quadrada na equação de pitágoras
import math as m

# Pede as coordenadas da origem para o usuário
origemx = int(input("Qual a coordenada x da origem do plano cartesiano: "))
origemy = int(input("Qual a coordenada y da origem do plano cartesiano: "))


""" Abaixo estão os anuncios das variáveis antes de serem usadas. A única não inicializada em zero é a "menor_distancia_total" para garantir que a 
distancia a ser calculada será menor do que está previamente designado para a variável. """

maior_distancia_total = 0
coordenada_x_da_maior_distancia = 0
coordenada_y_da_maior_distancia = 0
menor_distancia_total = 1000000
coordenada_x_da_menor_distancia = 0
coordenada_y_da_menor_distancia = 0
distancia_total_calculada = 0

# Declarando as variáveis que vão armazenar as quantidades de pontos em cada quadrante
pontos_no_quadrante_1 = 0
pontos_no_quadrante_2 = 0
pontos_no_quadrante_3 = 0
pontos_no_quadrante_4 = 0

#Pede quantidade de pontos para o usuário.
n_de_pontos = int(input("Quantos pontos você quer analisar: "))

#Este loop vai rodar uma vez para cada ponto que o usuário escolheu. Ele deverá designar as coordenadas uma de cada vez.
while n_de_pontos != 0:
  coordenada_x = int(input("Qual a coordenada x do ponto: "))
  coordenada_y = int(input("Qual a coordenada y do ponto: "))

  distancia_x = coordenada_x - origemx
  distancia_y = coordenada_y - origemy

  #Calculando a distância por meio da equação de Pitágoras, pois temos um triângulo retângulo => a^2 = b^2 + c^2
  distancia_total_calculada = m.sqrt((distancia_x**2) + (distancia_y**2))

  # Condição que observa qual a maior distância. Se o valor de alguma distância for maior do que a armazenada na variável, esta é atualizada com a nova distância.
  # Armazena também as coordenadas dos pontos de maior distância para poderem ser apresentadas depois.
  if distancia_total_calculada > maior_distancia_total:
    maior_distancia_total = distancia_total_calculada
    coordenada_x_da_maior_distancia = coordenada_x
    coordenada_y_da_maior_distancia = coordenada_y

  # Faz o mesmo, só que para a menor distância desta vez
  if distancia_total_calculada < menor_distancia_total:
    menor_distancia_total = distancia_total_calculada
    coordenada_x_da_menor_distancia = coordenada_x
    coordenada_y_da_menor_distancia = coordenada_y


  #Condições encadeadas para determinar o quadrante de cada um dos pontos escolhidos pelo usuário
  if coordenada_x == origemx or coordenada_y == origemy:
    coordenada_x = str(coordenada_x)
    coordenada_y = str(coordenada_y)
    print("Ponto (" + coordenada_x + "," + coordenada_y + ") esta sobre o eixo de coordenadas.")
  elif coordenada_x > origemx and coordenada_y > origemy:
    coordenada_x = str(coordenada_x)
    coordenada_y = str(coordenada_y)
    pontos_no_quadrante_1 = pontos_no_quadrante_1 + 1
    print("Ponto (" + coordenada_x + "," + coordenada_y + ") esta no 1o quadrante.")
  elif coordenada_x < origemx and coordenada_y > origemy:
    coordenada_x = str(coordenada_x)
    coordenada_y = str(coordenada_y)
    pontos_no_quadrante_2 = pontos_no_quadrante_2 + 1
    print("Ponto (" + coordenada_x + "," + coordenada_y + ") esta no 2o quadrante.")
  elif coordenada_x < origemx and coordenada_y < origemy:
    coordenada_x = str(coordenada_x)
    coordenada_y = str(coordenada_y)
    pontos_no_quadrante_3 = pontos_no_quadrante_3 + 1
    print("Ponto (" + coordenada_x + "," + coordenada_y + ") esta no 3o quadrante.")
  elif coordenada_x > origemx and coordenada_y < origemy:
    coordenada_x = str(coordenada_x)
    coordenada_y = str(coordenada_y)
    pontos_no_quadrante_4 = pontos_no_quadrante_4 + 1
    print("Ponto (" + coordenada_x + "," + coordenada_y + ") esta no 4o quadrante.")
  n_de_pontos = n_de_pontos - 1

# Converte os valores das coordenadas para string apra poderem ser impressas depois sem haverem espaços
coordenada_x_da_maior_distancia = str(coordenada_x_da_maior_distancia)
coordenada_y_da_maior_distancia = str(coordenada_y_da_maior_distancia)

coordenada_x_da_menor_distancia = str(coordenada_x_da_menor_distancia)
coordenada_y_da_menor_distancia = str(coordenada_y_da_menor_distancia)

# Apresenta os resultados para o usuário
print("Ponto (" + coordenada_x_da_menor_distancia + "," + coordenada_y_da_menor_distancia + ") eh o mais proximo, distancia = %.2f" %menor_distancia_total)
print("Ponto (" + coordenada_x_da_maior_distancia + "," + coordenada_y_da_maior_distancia + ") eh o mais distante, distancia = %.2f" %maior_distancia_total)
print("Existe(m)", pontos_no_quadrante_1, "ponto(s) no primeiro quadrante;", pontos_no_quadrante_2, "ponto(s) no segundo quadrante;", pontos_no_quadrante_3, "ponto(s) no terceiro quadrante e", pontos_no_quadrante_4, "ponto(s) no quarto quadrante;")





#----------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------PARTE B---------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------

#Declarando as variáveis que indicam as coordenadas dos pontos de origem e final da caminhada do robô
x_final = 0
y_final = 0

"""Declarando as variáveis booleanas para passo cima e passo lado. Basiamente, como será visto nas condições encadeadas abaixo, o robô só vai poder caminhar
para cima se a variável passo_cima estiver em 1 (True) e a passo_lado 0 (False) e vice-versa. Passo_cima já começa como True pois o primeiro passo do robô sempre
será para cima"""
passo_cima = 1
passo_lado = 0

#Pedindo as coordenadas de origem para o usuário
origem_x_robo = int(input("Digite a coordenada X do ponto de origem A do robô: "))
origem_y_robo = int(input("Digite a coordenada Y do ponto de origem A do robô: "))

#coordenadas finais commeçam com as mesmas coordenadas da origem. São alteradas conforme o robô caminha.
x_final = origem_x_robo
y_final = origem_y_robo

#Pede para o usuário quanto tempo de caminhada, o que corresponde ao número de passos pois a velocidade é de um "bloco" por segundo
quantos_passos = int(input("Digite por quanto tempo o robô irá caminhar: "))


"""Condições encadeadas para calcular os passos do robô. Quando já deu um passo para cima, a variável passo_cima é desativada enquanto a passo_lado é ativada.
Para garantir que o robô não vai dar passos a mais no sentido errado. Variáveis x_final e y_final são atualizadas constantemente."""

"""A única situação em que o robô, ao andar para o lado, só andaria um único passo, é caso estivesse apenas um passo sobrando para andar, o que foi
  considerado nesta última condição"""
while quantos_passos > 0:
  if passo_cima == 1 and passo_lado == 0 and quantos_passos >=1:
    y_final = y_final + 1
    passo_lado = 1
    passo_cima = 0
    quantos_passos = quantos_passos - 1
  elif passo_cima == 0 and passo_lado == 1 and quantos_passos >= 2:
    x_final = x_final + 2
    passo_lado = 0
    passo_cima = 1
    quantos_passos = quantos_passos - 2
  elif passo_cima == 0 and passo_lado == 1 and quantos_passos == 1:
    x_final = x_final + 1
    passo_lado = 0
    passo_cima = 1
    quantos_passos = quantos_passos - 1

# Converte os valores das coordenadas para string apra poderem ser impressas depois sem haverem espaços
x_final = str(x_final)
y_final = str(y_final)

# Imprime os resultados para o usuário
print("Resposta: ao final da caminhada o robô estará no ponto (" + x_final + "," + y_final + ") do plano cartesiano.")