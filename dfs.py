graph = { 
    '1': ['2', '4', '6'], 
    '2': ['1', '3'], 
    '3': ['2'], 
    '4': ['1', '5'], 
    '5': ['4'], 
    '6': ['1', '7'], 
    '7': ['6']  #change according to the given question 
} 
 
visited = []   
stack = [] 
 
def dfs(visited, graph, start, end): 
    stack.append(start) 
     
    while stack: 
        m = stack.pop() 
        if m not in visited: 
            visited.append(m) 
             
            if m == end: 
                break  # Stop when end node is found 
             
            stack.extend(reversed(graph[m]))  # Reverse to maintain 

 
# Take input from user 
start_node = input("Enter starting node: ") 
end_node = input("Enter ending node: ") 
 
dfs(visited, graph, start_node, end_node) 
print("Traversal path:", visited)
