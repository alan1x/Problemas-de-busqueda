from pyamaze import maze,agent,COLOR
from queue import PriorityQueue
def h(cell1,cell2):
    x1,y1=cell1
    x2,y2=cell2

    return abs(x1-x2) + abs(y1-y2)
def aStar(m,final=(1,1),origen=(5,5)):
    cola_prioridad=PriorityQueue()
    costo={celda:float('inf') for celda in m.grid}
    funcion={celda:float('inf') for celda in m.grid}
    costo[origen]=0
    funcion[origen]=h(origen,final)
    cola_prioridad.put((h(origen,final),h(origen,final),origen))
    a_est={}
    caminos=[]
    while not cola_prioridad.empty() and origen!=final:
        inicio=cola_prioridad.get()[2]
        for d in 'ESNW':
            if m.maze_map[inicio][d]==True:
                if d=="E":
                    hijo=(inicio[0],inicio[1]+1)
                if d=="W":
                    hijo=(inicio[0],inicio[1]-1)
                if d=="N":
                    hijo=(inicio[0]-1,inicio[1])
                if d=="S":
                    hijo=(inicio[0]+1,inicio[1])
                costo_temp=costo[inicio]+1
                funcion_temp=costo_temp+h(hijo,final)
                caminos.append(hijo)
                if funcion_temp<funcion[hijo]:
                    funcion[hijo]=funcion_temp
                    costo[hijo]=costo_temp
                    cola_prioridad.put((funcion_temp,h(hijo,final),hijo))
                    a_est[hijo]=inicio
    camino_real={}
    while final!=origen:
        camino_real[a_est[final]]=final
        final=a_est[final]
    return camino_real



def dfs(m,final=(1,1),origen=(5,5)):
    explorados=[origen]
    frontera=[origen]
    dfscamino={}
    while len(frontera)>0:
        inicio=frontera.pop()
        if inicio==final:
            break
        for d in 'ESNW':
            if m.maze_map[inicio][d]==True:
                if d=="E":
                    hijo=(inicio[0],inicio[1]+1)
                if d=="W":
                    hijo=(inicio[0],inicio[1]-1)
                if d=="N":
                    hijo=(inicio[0]-1,inicio[1])
                if d=="S":
                    hijo=(inicio[0]+1,inicio[1])
                if hijo not in explorados:
                    explorados.append(hijo)
                    frontera.append(hijo)
                    dfscamino[hijo]=inicio
    camino_real={}
    while final!=origen:
        camino_real[dfscamino[final]]=final
        final=dfscamino[final]

    return camino_real

def bfs(m,final=(1,1),origen=(5,5)):
    explorados=[origen]
    frontera=[origen]
    bfs={}
    while len(frontera)>0:
        inicio=frontera.pop(0)
        if inicio==final:
            break
        for d in 'ESNW':
            if m.maze_map[inicio][d]==True:
                if d=="E":
                    hijo=(inicio[0],inicio[1]+1)
                if d=="W":
                    hijo=(inicio[0],inicio[1]-1)
                if d=="N":
                    hijo=(inicio[0]-1,inicio[1])
                if d=="S":
                    hijo=(inicio[0]+1,inicio[1])
                if hijo in explorados:
                    continue
                explorados.append(hijo)
                frontera.append(hijo)
                bfs[hijo]=inicio
    camino_real={}
    while final!=origen:
        camino_real[bfs[final]]=final
        final=bfs[final]
    return camino_real





if __name__=='__main__':
    x=1
    y=2
    n=9
    m=20
    objetivo=(n,m)
    origen=(x,y)
    m=maze(n,m)
    m.CreateMaze(objetivo[0],objetivo[1],loadMaze='laberinto.csv')
    #m.CreateMaze(x,y)
    path=aStar(m,objetivo,origen)
    path2=dfs(m,objetivo,origen)
    path3=bfs(m,objetivo,origen)
    a=agent(m,footprints=True,filled=True,color=COLOR.red,x=origen[0],y=origen[1])
    a2=agent(m,footprints=True,filled=True,color=COLOR.green,x=origen[0],y=origen[1])
    a3=agent(m,footprints=True,filled=True,x=origen[0],y=origen[1])
    m.tracePath({a:path},delay=50,kill=True)
    m.tracePath({a2:path2},delay=50,kill=True)
    m.tracePath({a3:path3},delay=50)
    m.run()
