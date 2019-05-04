#!/usr/bin/env python
# coding: utf-8

# # lista 1 - COMP1 - UFRJ
# 
# http://jacarepagua.dcc.ufrj.br/~ladybug/aulas-python1/aula1_pratica_b.pdf
# ###### lista resolvida por Guilherme "Shakz" Paiva.
# 
# 

# # Faça uma função que:

# ## 1. Calcule a área de um retângulo dados seus dois lados. Teste pelo menos para os seguintes pares de entrada:
# 
# • 5 e 7; resposta esperada é 35
# 
# • 15 e 2; resposta esperada é 30
# 
# • 500 e 700; resposta esperada é 350000
# 
# • 5 e 0; resposta esperada é 0

# In[1]:


def area_do_retangulo(lado1,lado2):
    return lado1 * lado2


# In[2]:


area_do_retangulo(5,7)


# In[3]:


area_do_retangulo(15,2)


# In[4]:


area_do_retangulo(500,700)


# In[5]:


area_do_retangulo(5,0)


# ## 2. Calcule a área da coroa circular (anel) formada por dois círculos de raios r1 e r2 (r1 > r2 e P i = 3.14).Teste pelo menos para os seguintes pares de entrada:
#     
# • 2 e 1; resposta esperada é 9.42
# 
# • 15 e 5; resposta esperada é 628
# 
# • 100 e 0; resposta esperada é 31400

# In[7]:


# area da coroa circular é dada pela fórmula: A = πR2 - πr2
def area_da_coroa_circular(raio1,raio2):
    pi = 3.14
    return (pi * raio1 ** 2) - (pi * raio2 ** 2)


# In[8]:


area_da_coroa_circular(2,1)


# In[9]:


area_da_coroa_circular(15,5)


# In[10]:


area_da_coroa_circular(100,0)


# ## 3. Calcule o resultado e o resto da divisão de dois números inteiros (a função deve retornar os dois valores no mesmo comando return).

# In[11]:


def resto_divisao(a,b):
    return a % b, a/b


# In[13]:


resto_divisao(4,2)


# ## 4. Calcule a ordenada de uma função de segundo grau dados os parâmetros a, b, c e a abscissa.

# In[14]:


def valor_da_ordenada(a,b,c,x):
    return a*x**2 + b*x + c


# In[17]:


valor_da_ordenada(1,1,1,1)


# ## 5. Dado o valor da conta de um restaurante, calcule a gorjeta do garçom, considerando 10% do valor da conta.

# In[20]:


def valor_da_gorjeta(valor_da_conta):
    return valor_da_conta * 0.1


# In[21]:


valor_da_gorjeta(100)


# ## 6. Calcule a média de dois números. Teste pelo menos para os seguintes pares de entrada:
# 
# • - 5 e 7
# 
# • 2 e -2
# 
# • 5 e 5
# 
# • 3 e 4
# 
# • 3.0 e 4.0

# In[22]:


def media_de_dois_numeros(a,b):
    return (a + b) / 2


# In[23]:


media_de_dois_numeros(-5,7)


# In[24]:


media_de_dois_numeros(2,-2)


# In[25]:


media_de_dois_numeros(5,5)


# In[26]:


media_de_dois_numeros(3,4)


# In[27]:


media_de_dois_numeros(3.0,4.0)


# ## 7. Calcule a média ponderada de dois números com os respectivos pesos.

# In[30]:


def media_ponderada(peso1,nota1,peso2,nota2):
    return (nota1*peso1 + nota2*peso2) / (peso1 + peso2)


# In[31]:


media_ponderada(3,4,2,7)


# ## 8. Calcule a distância que a correnteza arrasta um barco que atravessa um rio. São conhecidas: a velocidade da correnteza, a largura do rio e a velocidade do barco perpendicular à correnteza.
# 

# In[ ]:


# tempo de travessia = largura do rio / velocidade
# distancia que a correnteza arrastou o barco = velocidade da correnteza * tempo de travessia


# In[32]:


def desvio_da_correnteza(velocidade_da_correnteza, largura_do_rio, velocidade_do_barco):
    tempo_de_travessia = largura_do_rio / velocidade_do_barco
    return velocidade_da_correnteza * tempo_de_travessia


# ## 9. Calcule o saldo final de uma conta, dado o saldo inicial, o número de meses e a taxa de juros mensal (juros simples).
# ### Saldo Final = Saldo Inicial (1 + juros.meses)
# 

# In[38]:


#No parâmetro juros_mensal deve ser informado o valor percentual sem o símbolo de porcentagem.
def saldo_final(saldo_inicial, numero_de_meses, juros_mensal):
    return saldo_inicial * (1 + juros_mensal * numero_de_meses/100)


# In[39]:


saldo_final(100,1,10)


# ## 10. Calcule o erro entre o valor da soma de uma PG infinita a partir de 1.0 e a soma dos n primeiros termos dessa PG. A soma dos termos de uma PG é 1/(1 − q), onde q é a razão e 0 ≤ q < 1.
# 

# In[ ]:





# 11.  Calcule o tempo total de prova de um corredor de maratona em horas, minutos e segundos, dados: o
# tempo de partida (hh,mm,ss), e o tempo de chegada (hh,mm,ss).
# 

# In[79]:


# Apesar de você, provavelmente, não saber usar a bibliotecas ainda, na questao parece que só dá dois parâmetros:
# tempo de partida e tempo de chegada
# Obs: horas devem ser dadas em strings '12:43:45'

from datetime import datetime #importando ...

def tempo_total(tempo_de_partida,tempo_de_chegada):
    return str(datetime.strptime(tempo_de_chegada,'%H:%M:%S') - datetime.strptime(tempo_de_partida, '%H:%M:%S'))


# In[80]:


tempo_total('12:00:00','13:00:00')


# In[ ]:


# segundo metodo de resolver!
def tempo_total(tempo_de_partida,tempo_de_chegada)


# In[ ]:





# 12. Calcule o valor da gorjeta (10%) e o quanto cada pessoa de um grupo deve pagar (divisão equalitária).São
# dados o valor total da conta do restaurante e o número de pessoas na mesa.

# In[73]:


def conta_equalitaria(valor_da_conta, numero_de_pessoas):
    return valor_da_conta * 1.10 / numero_de_pessoas


# In[74]:


conta_equalitaria(100,2)


# 13. Calcule a área da superfície de um cubo que tem c por aresta.

# In[75]:


def area_do_cubo(c):
    return c ** 3
    


# In[76]:


area_do_cubo(3)


# In[ ]:




