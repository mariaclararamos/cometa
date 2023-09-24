import math

#menu 
print("Sistema para análise de Chuva de Meteoro.")
print("1. Definir perímetro da propriedade e da edificação de interesse.")
print("2. Unificar sistemas de coordenadas de referência.")
print("3. Processar registros de chuva de meteoros")
print("4. Apresentar estatísticas.")
print("5. Sair")

#opções

while True:
    a = int(input("Qual a opção?"))
    print('Analisando sua escolha!')
    if a == 2:
        print('é necessário primeiro definir o perímetro!')
        
    elif a == 3:
        print('é necessário primeiro unificar sistemas de coordenadas de referência!')
        
    elif a == 4:
        print ('é necessário completar as outras tarefas!')
        
    elif a == 5:
        print('fechando sistema!')
        break
    else:
        #Definir o tamanho das propriedades 
        print('1.Definir perímetro da propriedade e da edificação de interesse.') 
        print('Vamos definir o perímetro!')
        b = int(input('Nos diga o x superior de sua propriedade.'))
        c = int(input('Nos diga o y superior de sua propriedade.'))
        d = int(input('Nos diga o x inferior de sua propriedade.'))
        e = int(input('Nos diga o y inferior de sua propriedade.'))
        p = int(input('Nos diga o perímetro?'))
        print('Agora vamos medir a edificação!')
        f = int(input('Nos diga o x superior de sua edificação.'))
        g = int(input('Nos diga o y superior de sua edificação.'))
        h = int(input('Nos diga o x inferior de sua edificação.'))
        i = int(input('Nos diga o y inferior de sua edificação.'))
        p1 = int(input('Nos diga o perímetro?'))
        #registro de chuvas
        print('3. Processar registros de chuva de meteoros')
        print ('Vamos registrar a chuva de meteoros!(para terminar os registros pfvr responder ambas perguntas com 0.)')
        cont = 1
        cont1 = 0
        cont2 = 0
        cont3 = 0
        cont4 = 0
        while True:
            print('Registro {}'.format(cont))
            op3 = float(input('ângulo(apenas o dividendo,se houver apenas o pi colocar 1):'))
            op4 = float(input('angulo(apenas o divisor,caso não houver colocar o numero 1):'))
            op5 = float (input('Distância'))
            if (op3 == 0 and op4 == 0):
                break
            else:
            #convertendo valor para cartesiana
                x = op5 * math.cos((op3*math.pi)/op4)
                y = op5 * math.sin((op3*math.pi)/op4)
                forma = "{:.1f}".format(x)
                forma2 = "{:.1f}".format(y)
                print("{},{}".format(forma,forma2))
                cont += 1
                if x>0 and y>0:
                    cont1 +=1
                if x<0 and y>0:
                    cont2 +=1
                if x<0 and y<0:
                    cont3 +=1
                if x>0 and y<0:
                    cont4 +=1
             
    print('opção 4. Apresentar estatísticas!')
    print('Quedas registradas:{},(100%).'.format(cont-1))
    
    #definindo se foi atingida ou não.   
    if c<x<e and b<y<d:
            
        print('Edificio foi atingido {}vezes.'.format(st))
    else:
        print('O edificio não foi atingido')
        
    print('NE:{}, {}%'.format(cont1, (cont1 / (cont - 1)) * 100))
    print('NO:{}, {}%'.format(cont2, (cont2 / (cont - 1)) * 100))
    print('SO:{}, {}%'.format(cont3, (cont3 / (cont - 1)) * 100))
    print('SE:{}, {}%'.format(cont4, (cont4 / (cont - 1)) * 100))



            
    if f<x<h and g<y<1:
            print('A edificação foi atingida {}vezes.'.format(st))
    else:
            print('A edificação não foi atingida')
    break

 
        
        


           
    

            

       

        
                 
    
    
