class buscador:
    def __init__(self,dato):
        self.lista=dato
        
    def  recorrerElemento(self):
        for ele in self.lista:
            print(ele,end=" ")
            
        for ele in self.lista[::-1]:
            print(ele,end=" ")    
            
        print()
        for pos, ele in enumerate (self.lista):
            print("[{}]={}"   .format(pos,ele))
        print()   
         
        for pos in range(len(self.lista)-1,-1,-1):
            print("[{}]={}"   .format(pos,self.lista[pos]))
           
    def buscar(self,buscado):
         for pos, ele in enumerate (self.lista):
            if ele ==buscado:
                break
       
         return pos
           
datos = [8,4,2,9,1] 
#buscado=9
#        0 1 2 3 4
#datos="hola"
bus = buscador(datos)
#bus.recorrerElemento()
valor=9
resp= bus.buscar(valor)
print(resp)

    