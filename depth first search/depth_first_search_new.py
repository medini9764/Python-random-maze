#import random module
import random

#Create an 8 by 8 maze
maze = [[0 for i in range(8)] for j in range(8)]
 
#Assign value to each node
node = 0
for i in range(8):
	for j in range(8):
		maze[j][i] = [node,0]
		node += 1

#Randomly select a node within the 0-15 nodes as Start Node
start_node_x = random.randint(0,7)
start_node_y = random.randint(0,1)
maze[start_node_x][start_node_y][1] = 'S'
start = (start_node_x,start_node_y)


#Randomly select a node within the 48-63 nodes as the goal node
goal_node_x = random.randint(0,7)
goal_node_y = random.randint(6,7)
maze[goal_node_x][goal_node_y][1] = 'G'
goal = (goal_node_x,goal_node_y)

#Randomly select six barrier nodes.
barrier_nodes = []
for i in range(6):
	while True:
		row = random.randint(0,7)
		col = random.randint(0,7)
		if maze[row][col][1] not in ['S','G','B']:
			barrier_nodes.append(maze[row][col][0])
			maze[row][col][1] = 'B'
			break
for row in maze:
	print(row)

def depth_first_search(maze,start,goal):
	#dirs = [(0,-1),(-1,0),(1,0),(1,1)]
	dirs = [(0,-1),(-1,0),(1,0),(0,1)]
	#Create a stack to store the cells that need to be explored
	#Append staring node and [start] as the path
	stack = [(start,[maze[start[0]][start[1]][0]])]

	#Initialize the start node
	start_node=maze[start[0]][start[1]][0]

	#Initialize the goal node
	goal_node=maze[goal[0]][goal[1]][0]

	#Initialize the time
	time = 1

	#Create a list to store the visited nodes
	visited_node = [maze[start[0]][start[1]][0]]
	

	#While queue is not empty
	while stack:
		#Get the current cell
		(node,path) = stack.pop(-1)
		x,y=node
			
		#Check if the current cell is the goal
		if x==goal[0] and y==goal[1]:
			# if it is ,we found the goal,so we can stop the search
			name = 'Depth First Search\n'
			#goal_node = maze[x][y][0]
			return print(name,'Goal Node =',goal_node,'Start Node =',start_node,'Time =',time,'\n','Visited Nodes \n ',visited_node,'\n Final Path \n',path)
			#break
			
		#Add the neighbors of the current cell to the queue
		for dx,dy in dirs:
		#Calculate the coordinates of the neighbor
			nx = x + dx
			ny = y + dy

			#Check if the neighbor is inside the maze,not a barrier and not visited
			if 0 <= nx < len(maze) and 0 <= ny < len(maze) and maze[nx][ny][1] != 'B' and maze[nx][ny][0] not in visited_node:
				new_node=(nx,ny)
				stack.append((new_node,path + [maze[nx][ny][0]]))
				visited_node.append(maze[nx][ny][0])
				time +=1

	return print('Goal Node =',goal_node,'Start Node =',start_node,'Cannot find a path using Depth First Search')
depth_first_search(maze,start,goal)