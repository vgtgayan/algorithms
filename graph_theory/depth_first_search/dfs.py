
# Global variables
debug = False
n = 9 # No: of nodes
# List notation of graph with adjecent node details
# Each node contains its adjacent nodes in a list
adj_graph = [
    [6,7], #0 -> 6,7 (likewise)
    [2,8], #1
    [1,8], #2
    [5],   #3
    [6,7], #4
    [3],   #5
    [0,4], #6
    [0,4], #7
    [1,2]  #8
]
# This list keeps track of each visited node
visited = [False for _ in range(n)]
# List to keep component index
components = [-1 for _ in range(n)]
# Counter to assign component values
count = 0

def find_components():
    global count
    for i in range(n):
        if (visited[i] == False):
            dfs_for_find_components(i)
            count += 1
        
    return [count, components]



def dfs_for_find_components(at):
    visited[at] = True
    if debug:
        print("{} Visited ".format(at))

    components[at] = count
    neighbours = adj_graph[at]
    for next in neighbours:
        if (visited[next] == False):
            dfs_for_find_components(next)



def dfs(at):
    # if visited[at]:
    #     return
    visited[at] = True
    if debug:
        print("{} Visited ".format(at))

    neighbours = adj_graph[at]
    for next in neighbours:
        if (visited[next] == False):
            dfs(next)



def main():
    #print("This is Depth first search algo......")
    #dfs(0)
    print(find_components())
    if debug:
        print(visited)


if __name__ == "__main__":
    main()