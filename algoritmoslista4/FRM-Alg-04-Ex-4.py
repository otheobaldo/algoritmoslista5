# 4. Perímetro de um polígono. Crie um programa Python para calcular o perímetro de um
# polígono sendo fornecidas as coordenadas x e y de cada um de seus vértices. Inicie lendo x e
# y do primeiro vértice. Depois disso continue lendo x e y dos próximos vértices até que o
# usuário entre com uma linha em branco para o valor da coordenada x (ou seja, quando ele
# digitar “Enter" ou “Return" sem fornecer um valor). Cada vez que você ler as coordenadas de
# um novo vértice, você deve calcular a distância em relação ao vértice anterior e acrescentá-la
# ao valor do perímetro. A figura abaixo ilustra como se calcula a distância entre dois pontos
# sendo dadas suas coordenadas x e y.

x = int(input("Digite a coordenada x do ponto 1: "))
y = int(input("Digite a coordenada y do ponto 1: "))
xant = x
yant = y
distancia = 0
p = 1

while True:    
    p = 1 + p
    x1 = input(f"Digite a coordenada x do ponto {p} (enter para sair): ")
    if not x1:
        break
    else:
        y1 = int(input(f"Digite a coordenada y do ponto {p}: "))
        d = distancia
        distancia = ((y1-y)**2+(int(x1)-x)**2)**(1/2)  
        distancia = distancia + d     
        x = int(x1)
        y = y1

d = ((yant-y)**2+(int(xant)-x)**2)**(1/2)        
distancia += d 
print("O perimetro é",distancia)
    
