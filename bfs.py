graph = { 
    '1': ['2','4','6'], 
    '2': ['1','3'], 
    '3': ['2'], 
    '4': ['1','5'], 
    '5': ['4'], 
    '6': ['1','7'], 
    '7': ['6'] #change according to the given question 
} 
def bfs(graph, start, end): 
    visited = [] 
    queue = [] 
     
    queue.append(start) 
     
    while queue: 
        m = queue.pop(0) 
         
        if m not in visited: 
            visited.append(m) 
 
            # Stop traversal if end node is found 
            if m == end: 
                print("Reached:", end) 
                break 
 
            for neighbour in graph[m]: 
                if neighbour not in visited: 
                    queue.append(neighbour) 
     
    print("Traversal path:", visited) 
# Take input from user 
start_node = input("Enter starting node: ") 
end_node = input("Enter ending node: ") 
 
# Call BFS with input 
bfs(graph, start_node, end_node)
