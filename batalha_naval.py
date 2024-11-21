
import numpy as np
from numpy.random import random
def fimJogo(tam):
  porta=4
  totalPorta=int(tam/10)
  sub=3
  totalSub=int(tam/3)
  destro=2
  totalDes=int(tam/3)
  bote=1
  totalBote=int(tam/5)
  return totalPorta*4+totalSub*3+totalDes*2+totalBote


def encher(cam,tam):
  porta=4
  totalPorta=int(tam/10)
  sub=3
  totalSub=int(tam/3)
  destro=2
  totalDes=int(tam/3)
  bote=1
  totalBote=int(tam/5)
  colunaLivre=np.zeros(tam)
  repetir=totalPorta
  while(repetir!=0):
    tmp=tam-4
    linha=np.random.randint(0, tmp)
    coluna=np.random.randint(0, tam)
    existe=0
    for k in range(porta):
      if(cam[linha+k][coluna]!='A'):
        existe=1
    if(colunaLivre[coluna]!=0):
      existe=1
    if(existe==0):
      for k in range(porta):
        cam[linha+k][coluna]="P"
        colunaLivre[coluna]=1
      repetir=repetir-1


  repetir=totalSub
  while(repetir!=0):
    linha=np.random.randint(0, tam-3)
    coluna=np.random.randint(0, tam)
    existe=0
    for k in range(sub):
      if(cam[linha+k][coluna]!='A'):
        existe=1
    if(colunaLivre[coluna]!=0):
      existe=1
    if(existe==0):
      for k in range(sub):
        cam[linha+k][coluna]="S"
        colunaLivre[coluna]=1
      repetir=repetir-1


  repetir=totalDes
  while(repetir>0):
    tmp=np.zeros(tam)
    cont=0
    for t in range(tam):
      if(colunaLivre[t]==0):
        tmp[cont]=t
        cont+=1
    tm=np.zeros(cont)
    for t in range(cont):
        tm[t]=tmp[t]
    existe=0
    linha=np.random.randint(0, tam-2)
    coluna=int(tm[np.random.randint(0, cont)])
    for k in range(destro):
      if(cam[linha+k][coluna]!='A'):
        existe=1
    if(colunaLivre[coluna]!=0):
      existe=1
    if(existe==0):
      for k in range(destro):
        cam[linha+k][coluna]="D"
        colunaLivre[coluna]=1
      repetir=repetir-1


  repetir=totalBote
  while(repetir!=0):
    tmp=np.zeros(tam)
    cont=0
    for t in range(tam):
      if(colunaLivre[t]==0):
        tmp[cont]=t
        cont+=1
    tm=np.zeros(cont)
    for t in range(cont):
        tm[t]=tmp[t]
    linha=np.random.randint(0, tam)
    coluna=int(tm[np.random.randint(0, cont)])
    existe=0
    for k in range(bote):
      if(cam[linha+k][coluna]!='A'):
        existe=1
    if(colunaLivre[coluna]!=0):
      existe=1
    if(existe==0):
      cam[linha+k][coluna]="B"
      colunaLivre[coluna]=1
      repetir=repetir-1

  return cam

a=15
print("Bem-vindo ao jogo Batalha Naval!")
while(True):
  print("Informe o tramanho do tabuleiro: [10:25]")
  a=int(input())
  while(a>25 or a<10):
      print("Informe o tramanho do tabuleiro: [10:25]")
      a=int(input())
  campo=np.zeros((a,a), dtype=np.str_)
  campo.fill('A')
  campo=encher(campo,a)
  campoVisivel=np.zeros((a,a), dtype=np.str_)
  campoVisivel.fill('X')
  pontos=0
  pontosFim=fimJogo(a)
  jogadas=0
  while(pontos!=pontosFim):
    print("Tabuleiro do Jogo\n",campoVisivel)
    print("Tabuleiro do oculto\n",campo)
    print("Escolha uma posição com X")
    print("linha (1 a",a,"):")
    linha=int(input())
    print("coluna (1 a",a,"):")
    coluna=int(input())
    if(linha>a or coluna>a):
      print("Posição inválida!!!")
    else:
      if(campoVisivel[linha-1][coluna-1]=='X'):
        jogadas+=1
        if(campo[linha-1][coluna-1]!='A'):
          pontos+=1
          print("Acertou...!!!! Acertos:",pontos,"Jogadas:", jogadas)
          campoVisivel[linha-1][coluna-1]=campo[linha-1][coluna-1]
        else:
          campoVisivel[linha-1][coluna-1]=campo[linha-1][coluna-1]
          print("Errouuu...!!!! Acertos:",pontos,"Jogadas:", jogadas)
      else:
        print("Posição inválida1!!!")


  print("Parabéns!!! Você venceu!!!", pontos,"tiros certeiros em", jogadas,"tentativas!")
  print("Redimento de", (pontos*100/jogadas))
  sair=int(input("Gostaria de jogar novamente? 1=sim 2= não"))
  if(sair==2):
    break;

#campo2=np.array(a,a)



