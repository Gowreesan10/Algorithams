import numpy as np

# Function to create the flow matrix
def create_flow_matrix(peopleCount, committeesCount, peoples, committees, possibleCommittees, maxPeople):
    length = peopleCount + committeesCount + 2
    flowMatrix = [[0 for _ in range(length)] for _ in range(length)]

    for i in range(length):
        if i == 0:
            for people_index in range(peopleCount):
                flowMatrix[i][people_index + 1] = int(possibleCommittees[people_index][0])
        elif i > 0 and i <= peopleCount:
            desiered_community_count = int(possibleCommittees[i - 1][0])
            for z in range(desiered_community_count):
                for k in range(committeesCount):
                    if possibleCommittees[i - 1][z + 1] == committees[k]:
                        community_node_index = peopleCount + 1 + k
                        flowMatrix[i][community_node_index] = 1
        elif i > peopleCount and i <= peopleCount + committeesCount:
            flowMatrix[i][length - 1] = maxPeople[i - peopleCount - 1]

    return flowMatrix



def BFS(source, sink, parent, flow_Matrix):
    #initally assign all nodes as false to indicate not is unvisited
    visited = [False] * (sink + 1)
    queue = []

    #start path search from source
    queue.append(source)
    #set source node as visited
    visited[source] = True

    while queue:
        #get first node from queue
        u = queue.pop(0)
        #iterate adjecency matrix and get path values
        for ind, val in enumerate(flow_Matrix[u]):
            #if node is unvisited and it has value
            if not visited[ind] and val > 0:
                #append the nodes in the queue
                queue.append(ind)
                #set node as visited and include the parent in the list to track path
                visited[ind] = True
                parent[ind] = u
                #if sink is schived retun true
                if ind == sink:
                    return True
    return False


def FordFulkerson(flowMatrix, sink):
    #set source node as zero
    source = 0
    #create and assign all parents nodes as -1
    parent = [-1] * (sink + 1)
    #initializa max flow
    max_flow = 0

    while BFS(source, sink, parent, flowMatrix):
        #initialize path_flow as infinity to compare with another value and get minimum
        path_flow = float("Inf")
        #to back traverse start from sink
        start = sink
        #loop until reach the source and get the minimum path value
        while start != source:
            path_flow = min(path_flow, flowMatrix[parent[start]][start])
            #assign the parent of current node to the start
            start = parent[start]

        #add the current min path value
        max_flow += path_flow
        v = sink

        while v != source:
            u = parent[v]
            flowMatrix[u][v] -= path_flow
            flowMatrix[v][u] += path_flow
            v = parent[v]

    return max_flow

def assign_committees(flowMatrix, maxPeople, peopleCount, committeesCount):
    temp_matrix = [[0 for _ in range(len(flowMatrix))] for _ in range(len(flowMatrix))]

    for i in range(len(flowMatrix)):
        for j in range(len(flowMatrix)):
            temp_matrix[i][j] = flowMatrix[i][j]

    max_flow = FordFulkerson(flowMatrix, len(flowMatrix) - 1)

    if max_flow == sum(maxPeople):
        matrix_np = np.array(temp_matrix)
        graph_np = np.array(flowMatrix)
        flow_matrix = np.zeros(shape=(len(flowMatrix), len(flowMatrix)))

        flow_matrix = graph_np - matrix_np

        committeePeople = []
        committeePeopleTmp = []

        for i in range(committeesCount):
            t = 0
            indexes = []
            indexes_temp = []

            for j in range(peopleCount):
                if flow_matrix[j + 1][peopleCount + i + 1] == -1:
                    indexes.append('P' + str(j + 1))
                    indexes_temp.append(j + 1)
                    t += 1

            committeePeople.append(indexes)
            committeePeopleTmp.append(indexes_temp)

        peopleCommittee = []

        for i in range(peopleCount):
            temp_list = []

            for j in range(committeesCount):
                for k in committeePeopleTmp[j]:
                    if i + 1 == k:
                        temp_list.append('C' + str(j + 1))

            peopleCommittee.append(temp_list)

        return peopleCommittee, committeePeople
    else:
        return None

def get_inputs():
    peopleCount = int(input("Enter the number of people: "))
    committeesCount = int(input("Enter the number of committees: "))
    peoples = list(input("Enter the names of people (space-separated): ").split())
    committees = list(input("Enter the names of committees (space-separated): ").split())

    possibleCommittees = []
    for i in range(peopleCount):
        user_input = list(input(f"Enter preferences for {peoples[i]} (space-separated): ").split())
        possibleCommittees.append(user_input)

    maxPeople = []
    for j in range(committeesCount):
        user_input = int(input(f"Enter the maximum people allowed in {committees[j]}: "))
        maxPeople.append(user_input)

    return peopleCount, committeesCount, peoples, committees, possibleCommittees, maxPeople

def display_results(peopleCount, committeesCount, peopleCommittee, committeePeople):
    print('Person: Committee')
    for i in range(peopleCount):
        print(f'P{i + 1}:', end=" ")
        for j in peopleCommittee[i]:
            print(j, end=" ")
        print("")

    print('\nCommittee: Person')
    for i in range(committeesCount):
        print(f'C{i + 1}:', end=" ")
        for j in committeePeople[i]:
            print(j, end=" ")
        print("")



if __name__ == "__main__":

    peopleCount, committeesCount, peoples, committees, possibleCommittees, maxPeople = get_inputs()

    flowMatrix = create_flow_matrix(peopleCount, committeesCount, peoples, committees, possibleCommittees, maxPeople)

    result = assign_committees(flowMatrix, maxPeople, peopleCount, committeesCount)

    if result:
        peopleCommittee, committeePeople = result
        display_results(peopleCount, committeesCount, peopleCommittee, committeePeople)
    else:
        print('Not Possible')