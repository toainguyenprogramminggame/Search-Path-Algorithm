from ast import operator
import math
from pickle import TRUE
from turtle import distance
from Space import *
from Constants import *

def DFS(g:Graph, sc:pygame.Surface):
    print('Implement DFS algorithm')

    open_set = [g.start.value]
    closed_set = []
    father = [-1]*g.get_len()

    #TODO: Implement DFS algorithm using open_set, closed_set, and father
    while(open_set != []):
        # Get element from stack
        curNode = g.grid_cells[open_set[-1]]
        open_set.pop()

        # if curnode if goal, stop search
        if(g.is_goal(curNode)):
            # set color for the goal node
            curNode.set_color(purple)
            g.draw(sc)

            x = curNode.x
            y = curNode.y

            curFather = -1
            while(curFather != g.start.value):
                curFather = father[curNode.value]
                nodeFather = g.grid_cells[curFather]

                nodeFather.set_color(grey)
                g.draw(sc)

                pygame.draw.line(sc,green,(x,y),(nodeFather.x,nodeFather.y))

                curNode = nodeFather
                x = nodeFather.x
                y = nodeFather.y
            


            # set color for the start
            closed_set[0].set_color(orange)
            g.draw(sc)

            return

        # if curnode is visited, continue
        if curNode in closed_set:
            continue
        
        # set color for current node
        curNode.set_color(yellow)
        g.draw(sc)

        neibourNodes = g.get_neighbors(curNode)

        # set RED color for open node
        for neibourNode in neibourNodes:
            if neibourNode not in closed_set:
                father[neibourNode.value] = curNode.value #set father
                neibourNode.set_color(red)
                g.draw(sc)


        # Get indexs of nodes in neibourNodes, append to open
        for neibourNode in neibourNodes:
            open_set.append(neibourNode.value)

        curNode.set_color(blue)
        closed_set.append(curNode)

        
    
    # raise NotImplementedError('Not implemented')

def BFS(g:Graph, sc:pygame.Surface):
    print('Implement BFS algorithm')

    open_set = [g.start.value]
    closed_set = []
    father = [-1]*g.get_len()

    #TODO: Implement BFS algorithm using open_set, closed_set, and father
    while(open_set != []):
        # Get element from stack
        curNode = g.grid_cells[open_set[0]]
        open_set.pop(0)


        # if curnode if goal, stop search
        if(g.is_goal(curNode)):
            # set color for the goal node
            curNode.set_color(purple)
            g.draw(sc)

            x = curNode.x
            y = curNode.y

            curFather = -1
            while(curFather != g.start.value):
                curFather = father[curNode.value]
                nodeFather = g.grid_cells[curFather]

                nodeFather.set_color(grey)
                g.draw(sc)

                pygame.draw.line(sc,green,(x,y),(nodeFather.x,nodeFather.y))

                curNode = nodeFather
                x = nodeFather.x
                y = nodeFather.y
            


            # set color for the start
            closed_set[0].set_color(orange)
            g.draw(sc)

            return

        # if curnode is visited, continue
        if curNode in closed_set:
            continue
        
        # set color for current node
        curNode.set_color(yellow)
        g.draw(sc)

        neibourNodes = g.get_neighbors(curNode)

        # set RED color for open node
        for neibourNode in neibourNodes:
            if (neibourNode not in closed_set) and (neibourNode.value not in open_set):
                father[neibourNode.value] = curNode.value #set father
                neibourNode.set_color(red)
                g.draw(sc)

                open_set.append(neibourNode.value)
        


        curNode.set_color(blue)
        closed_set.append(curNode)

    # raise NotImplementedError('Not implemented')

def UCS(g:Graph, sc:pygame.Surface):
    print('Implement UCS algorithm')

    open_set = {}
    open_set[g.start.value] = 0
    closed_set:list[int] = []
    father = [-1]*g.get_len()
    cost = [100_000]*g.get_len()
    cost[g.start.value] = 0

    # #TODO: Implement UCS algorithm using open_set, closed_set, and father
    while(open_set):
        # Sắp xếp lại cái open_set 
        sort = sorted(open_set.items(),key=lambda item:item[1])
        open_set = {k:v for k, v in sort}

        
        # Lấy node có đường đi nhỏ nhất ra khỏi open_set, pop open_set
        index = next(iter(open_set))
        curNode = g.grid_cells[index]


        # Kiểm tra xem curNode có phải là goal hay không
        if(g.is_goal(curNode)):
            curNode.set_color(purple)
            g.draw(sc)

            x = curNode.x
            y = curNode.y

            curFather = -1

            while(curFather != g.start.value):
                curFather = father[curNode.value]
                nodeFather = g.grid_cells[curFather]

                nodeFather.set_color(grey)
                g.draw(sc)

                pygame.draw.line(sc,green,(x,y),(nodeFather.x,nodeFather.y))

                curNode = nodeFather
                x = nodeFather.x
                y = nodeFather.y
            
            pygame.draw.line(sc,green,(x,y),(g.start.x,g.start.y))
            g.start.set_color(orange)
            g.draw(sc)
            return
        
        # Kiểm tra xem curNode đã được mở hay chưa
        if curNode.value in closed_set:
            continue

        curNode.set_color(yellow)
        g.draw(sc)

        # Lấy các node neibour và cho vào open_set
        neibourNodes = g.get_neighbors(curNode)
        distanceCur = open_set[index]

        for neibourNode in neibourNodes:
            distanceFromNeibourNode = distanceCur + 1
                  
            if(neibourNode.value not in closed_set):
                if((open_set.get(neibourNode.value) != None and distanceFromNeibourNode < open_set.get(neibourNode.value)) or open_set.get(neibourNode.value) == None):
                    father[neibourNode.value] = curNode.value #set father

                    open_set[neibourNode.value] = distanceFromNeibourNode
                    #set color for open node
                    neibourNode.set_color(red)
                    g.draw(sc)
        
        # Lấy curNode ra khỏi open_set
        open_set.pop(index)

        # Cho node vừa lấy vào closed_set 
        closed_set.append(index)

        #set color cho curNode
        curNode.set_color(blue)



    # raise NotImplementedError('Not implemented')

def AStar(g:Graph, sc:pygame.Surface):
    print('Implement A* algorithm')

    open_set = {}
    open_set[g.start.value] = 0
    closed_set:list[int] = []
    father = [-1]*g.get_len()
    cost = [100_000]*g.get_len()
    cost[g.start.value] = 0


    # Heuristic: h(n) = max(|xn - xgoal|, |yn - ygoal|)
    #TODO: Implement A* algorithm using open_set, closed_set, and father
    while(open_set):
        #Lấy node có fn nhỏ nhất ra khỏi open_set, pop open_set
        index = next(iter(open_set))
        curNode = g.grid_cells[index]

        for openIndex in open_set:
            openNode = g.grid_cells[openIndex]
            curNodeFn = open_set[index] + abs(curNode.x - g.goal.x) + abs(curNode.y - g.goal.y)
            openNodeFn = open_set[openIndex] + abs(openNode.x - g.goal.x) + abs(openNode.y - g.goal.y)

            if(curNodeFn > openNodeFn):
                index = openIndex
                curNode = openNode

        if(g.is_goal(curNode)):
            curNode.set_color(purple)
            g.draw(sc)

            x = curNode.x
            y = curNode.y

            curFather = -1

            while(curFather != g.start.value):
                curFather = father[curNode.value]
                nodeFather = g.grid_cells[curFather]

                nodeFather.set_color(grey)
                g.draw(sc)

                pygame.draw.line(sc,green,(x,y),(nodeFather.x,nodeFather.y))

                curNode = nodeFather
                x = nodeFather.x
                y = nodeFather.y
            
            pygame.draw.line(sc,green,(x,y),(g.start.x,g.start.y))
            g.start.set_color(orange)
            g.draw(sc)
            return
        
        if curNode.value in closed_set:
            continue

        curNode.set_color(yellow)
        g.draw(sc)

        # Lấy các node neibour
        neibourNodes = g.get_neighbors(curNode)
        distanceCur = open_set[index]

        for neibourNode in neibourNodes:
            distanceFromNeibourNode = distanceCur + 1

            if(neibourNode.value not in closed_set):
                if((open_set.get(neibourNode.value) != None and distanceFromNeibourNode < open_set[neibourNode.value]) or open_set.get(neibourNode.value) == None):
                    father[neibourNode.value] = curNode.value #set father

                    open_set[neibourNode.value] = distanceFromNeibourNode
                    neibourNode.set_color(red)
                    g.draw(sc)

        # Lấy curNode ra khỏi open_set sau đó cho vào closed_set
        open_set.pop(index)

        closed_set.append(index)

        #set color for curNode
        curNode.set_color(blue)
            

    # raise NotImplementedError('Not implemented')
