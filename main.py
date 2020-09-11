#!/bin/python3


# Complete the minimumBribes function below.
def minimumBribes(q):
    bribes = 0
    wsize = len(q)
    for i in range(wsize-1):
      for j in range(i+1,wsize):
        if q[i]>q[j] :
          bribes +=1
          if q[i]-(i+1) > 2 :
            return "Too chaotic"
    return bribes



        
if __name__ == '__main__':
    print("Lendo os dados")
    with open('dados2.dat', 'r') as f:
      data = f.readlines()
    print("criando vetor")
    for line in data:
        q = list(map(int, line.rstrip().split()))
    print('Temos ',len(q)," elementos")
    print('Analisando')
    print("ocorreram ",minimumBribes(q),"bribes")
