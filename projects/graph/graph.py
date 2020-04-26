"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError('That Vertex Does Not Exist.')

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # create a plan to visit queue and add starting vertex to it
        plan_to_visit = Queue()
        plan_to_visit.enqueue(starting_vertex)
        # create set for visited_vertices
        visited_vertices = set()
        # while the plan_to_visit queue is not Empty:
        while plan_to_visit.size() > 0:
            # dequeue the first vertex from the queue
            current_vertex = plan_to_visit.dequeue()
            # if it has not been visited (check visited)
            if current_vertex not in visited_vertices:
                # print the vertex
                print(current_vertex)
                # mark it as visited / add it to visited_vertices
                visited_vertices.add(current_vertex)
                # add all neighbors to the queue
                for neighbor in self.get_neighbors(current_vertex):
                    if neighbor not in visited_vertices:    
                        plan_to_visit.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # because of the way the stack works, you in effect dft just by popping from the last entered instead of first entered like in bfs

        # create a plan to visit stack and add starting vertex to it
        plan_to_visit = Stack()
        plan_to_visit.push(starting_vertex)
        # create set for visited_vertices
        visited_vertices = set()
        # while the plan_to_visit stack is not Empty:
        while plan_to_visit.size() > 0:
            # pop the first vertex from the stack
            current_vertex = plan_to_visit.pop()
            # if it has not been visited (check visited)
            if current_vertex not in visited_vertices:
                # print the vertex
                print(current_vertex)
                # mark it as visited / add it to visited_vertices
                visited_vertices.add(current_vertex)
                # add all neighbors to the stack
                for neighbor in self.get_neighbors(current_vertex):
                    if neighbor not in visited_vertices:    
                        plan_to_visit.push(neighbor)

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        pass  # TODO

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # create an empty queue, and enqueue a PATH to the starting vertex_id
        # queue.enqueue([starting_vertex])
        # create a set for visited_vertices
        # while the queue is not empty:
            # dequeue the first PATH
            # grab the last vertex in the path
                # if it hasn't been visited
                    # check if its the target
                        # Return the path
                    # mark it as visited
                    # make new versions of the current path, with each neighbor added to them
                        # duplicate the path 
                        # add the neighbor
                        # add the new path to the queue
        

        # create an empty queue, and enqueue a PATH to the starting vertex_id
        neighbors_to_visit = Queue()
        # queue.enqueue([starting_vertex])
        neighbors_to_visit.enqueue([starting_vertex])
        # create a set for visited_vertices
        visited_vertices = set()
        # while the queue is not empty:
        while neighbors_to_visit.size() > 0:
            # dequeue the first PATH in the queue
            current_path = neighbors_to_visit.dequeue()
            # grab the last vertex in the path
            current_vertex = current_path[-1]
                # if it hasn't been visited
            if current_vertex not in visited_vertices:
                # check if its the target
                if current_vertex == destination_vertex:
                    # Return the path
                    return current_path
                # mark it as visited
                visited_vertices.add(current_vertex)
                # make new versions of the current path, with each neighbor added to them
                for next_vertex in self.get_neighbors(current_vertex):
                    # duplicate the path 
                    new_path = list(current_path)
                    # new_path = current_path[:]
                    # add the neighbor
                    new_path.append(next_vertex)
                    # add the new path to the queue
                    neighbors_to_visit.enqueue(new_path)

        pass  # TODO

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # create an empty stack, and the visited vertices set
        neighbors_to_visit = Stack()
        visited_vertices = set()
        # add the first value, and the path array (currently empty bc we have not traversed any vertices yet)
        neighbors_to_visit.push((starting_vertex, []))
        # while the stack is not empty
        while neighbors_to_visit.size() > 0:
            # return the neighbor to visit
            current_vertex_plus_path = neighbors_to_visit.pop()
            # grab the vertex out of the tuple
            current_vertex = current_vertex_plus_path[0]
            # check if we have been here before
            if current_vertex not in visited_vertices:
                # is this our target?
                if current_vertex == destination_vertex:
                    # return the path to the target
                    updated_path = current_vertex_plus_path[1] + [current_vertex]
                    return updated_path
                # mark it as visited
                visited_vertices.add(current_vertex)
                # add the neighbors to the stack
                for neighbor in self.get_neighbors(current_vertex):
                    updated_path = current_vertex_plus_path[1] + [current_vertex]
                    neighbors_to_visit.push((neighbor, updated_path))


    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        pass  # TODO

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
