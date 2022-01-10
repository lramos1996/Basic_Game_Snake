from os import system
from random import choice
import time
import keyboard
from busqueda import buscar

class Snake:
    def __init__(self, posx,posy,sensorx,sensory):
        self.dirx,self.diry,self.posx,self.posy,self.cuerpo =1,1,posx,posy,[chr(64)]
        self.sensorx,self.sensory = sensorx,sensory
        self.posxini, self.posyini = [0],[0]
    def movex(self,dir):
        if dir == 1 : self.posx +=1
        elif dir == -1 : self.posx -=1
    def movey(self,dir):
        if dir == 1 : self.posy +=1
        elif dir == -1 : self.posy -=1
    def colaSnake(self, guardar):
        self.posxini.append(self.posx)
        self.posyini.append(self.posy)
        if guardar:
            self.posxini.pop(0)
            self.posyini.pop(0)
    def explorar(self,name,objeto,posy):
        busqueda = buscar(name,objeto,posy)
        self.sensorx,self.sensory = busqueda[0],busqueda[1]
        return busqueda
class Juego:
    def __init__(self):
        self.mapa = [ [chr(32) for _ in range(25)] for _ in range(25)]
        for i in self.mapa:
            i.append("|")
        self.mapa.append(["_" for _ in range(25)])
    def impMapa(self):
        for i in self.mapa:
            print(*i)
    def addSerp(self, x,y,n,m,cue):
        self.mapa[y][x]=cue
        self.mapa[m][n]=chr(32)
        #self.mapa[y].pop()
    def addObj(self, x,y,cue):
        self.mapa[y][x]=cue
    def vaciarMapa(self):
        pass
        #self.__init__()
        """self.mapa = [ [chr(32) for _ in range(25)] for _ in range(25)]
        for i in self.mapa:
            i.append("|")
        self.mapa.append(["_" for _ in range(25)])"""

class Comida:
    def __init__(self):
        self.cuerpo = [chr(36)]
        self.lista = [i for i in range(25)]
        self.posx=choice(self.lista)
        self.posy=choice(self.lista)
    def newPos(self):
        self.posx = choice(self.lista)
        self.posy = choice(self.lista)

def jugar():
    game,i,serp,tecla = Juego(),0,Snake(choice([i for i in range(25)]),choice([i for i in range(25)]),25,25),"d"
    eat,posicion, guardar, puntos =Comida(),(), True, 0
    while tecla != "fin" :
        game.addSerp(serp.posx,serp.posy,serp.posxini[0],serp.posyini[0],serp.cuerpo[0])
        game.addObj(eat.posx,eat.posy,eat.cuerpo[0])
        game.impMapa()
        if posicion == (): posicion = serp.explorar(game.mapa,eat.cuerpo[0],serp.posy)
        print (f"Sensor : {serp.sensorx} {serp.sensory}")
        print (f"Puntos : {puntos}")
        #game.vaciarMapa()
        time.sleep(1/40)
        #time.sleep(1/2)
        #print(["_" for _ in range(25)]))
        print (serp.posx," ",serp.posy," ", tecla)
        #game.addObj(serp.posx,serp.posy,serp.cuerpo)
        if keyboard.is_pressed("w") and tecla!="s": tecla = "w"
        elif keyboard.is_pressed("d") and tecla!="a": tecla = "d"
        elif keyboard.is_pressed("s") and tecla!="w": tecla = "s"
        elif keyboard.is_pressed("a") and tecla!="d": tecla = "a"
        elif keyboard.is_pressed(chr(27)): tecla = "fin"
        serp.colaSnake(guardar)
        if tecla == "w"   : serp.movey(-1)
        elif tecla == "d" : serp.movex(1)
        elif tecla == "a" : serp.movex(-1)
        elif tecla == "s" : serp.movey(1)
        #if serp.posx >= 24 and tecla == "d": tecla = "a"
        #if serp.posx <= 0 and tecla == "a": tecla = "d"
        #if serp.posy >= 24 and tecla == "s": tecla = "w"
        #if serp.posy <= 0 and tecla == "w": tecla = "s"
        if serp.posx > 24 : serp.posx-=24
        if serp.posx < 0 : serp.posx+=24
        if serp.posy > 24 : serp.posy-=24
        if serp.posy < 0 : serp.posy+=24
        guardar = True
        if eat.posx == serp.posx and eat.posy == serp.posy :
            guardar = False
            puntos += 1
            eat.newPos()
            posicion = ()
        if (serp.posx,serp.posy) in list(zip(serp.posxini, serp.posyini)):
            tecla = "fin"
        game.vaciarMapa()
        #print(f"{serp.posxini} {serp.posyini}")
        system("cls")
    game.impMapa()
    print("FIN DEL JUEGO!")
    print (f"Puntaje Final : {puntos}")
    print(f"{serp.posxini} {serp.posyini}")
    print (serp.posx," ",serp.posy," ", tecla)
if __name__ == "__main__":
    jugar()
