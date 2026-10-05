# Practical 1

## Summary

In this practical, five different sorting algorithms—Bubble Sort, Selection Sort, Insertion Sort, Quick Sort, and Merge Sort—were implemented using Python.
Each program takes input from the user, sorts the elements in ascending order, and displays the sorted array. The programs also show the time complexity and execution time of each algorithm.

## Conclusion

Through this practical, we learned how different sorting algorithms work and how they can be implemented in Python.
We also understood the importance of time complexity in comparing the efficiency of algorithms. Bubble Sort, Selection Sort, and Insertion Sort are simple to understand, while Quick Sort and Merge Sort are generally more efficient for larger datasets.
Overall, this practical helped us understand sorting algorithms, their performance, and how to choose a suitable algorithm for a particular problem.


# Practical 2

## Summary

In this practical, we implemented two important searching techniques in Python: Linear Search and Binary Search. Both programs take elements from the user and search for a given element in the array. The programs also display the position of the searched element, execution time, and time complexity.

## Conclusion

Through this practical, we understood how searching algorithms can be used to find a particular element from a collection of data. We learned that Linear Search is simple and can work directly on an unsorted array, but it may take more time when the number of elements is large.


# Practical 3

## Summary

In this practical, Max Heap Sort was implemented using Python. The program takes the elements from the user, builds a Max Heap, and repeatedly moves the largest element to its correct position to obtain the sorted array. The program also measures the execution time and displays the time and space complexity.

## Conclusion

Through this practical, we learned how Max Heap Sort works and how the heap data structure can be used for sorting elements efficiently. The practical gave us a better understanding of building a Max Heap, comparing parent and child elements, and repeatedly extracting the largest element.


# Practical 4

## Summary

In this practical, we implemented the factorial of a number using two different methods: iteration and recursion. In the iterative method, a for loop is used to multiply the numbers from 1 up to the given number. In the recursive method, the function repeatedly calls itself with a smaller value until it reaches the base case.The practical also helped us compare the time and space requirements of both approaches. Both methods have a time complexity of O(n), but the iterative method uses O(1) space, while the recursive method uses O(n) space because of the recursive function calls.

## Conclusion

Through this practical, we learned how the same problem can be solved using both iteration and recursion. The iterative approach is straightforward and uses less memory, while recursion provides a simpler way to represent the factorial calculation through repeated function calls.Overall, this practical helped us understand the basic difference between iteration and recursion and how their space requirements can vary even when their time complexity is the same. It also gave us practical experience in measuring the execution time of both approaches.


# Practical 6

## Summary

In this practical, we implemented Matrix Chain Multiplication using Dynamic Programming. The program takes the dimensions of the matrices from the user and uses a dynamic programming table to find the most efficient way to multiply the matrices. Instead of trying all possible multiplication orders directly, the program checks different split positions and stores the minimum multiplication cost for each part of the chain.

## Conclusion

Through this practical, we learned how Dynamic Programming can be used to solve the Matrix Chain Multiplication problem efficiently. We understood that the order in which matrices are multiplied can greatly affect the number of calculations required, even though the final result remains the same.The practical helped us understand how a DP table can store previously calculated results and use them to find the minimum multiplication cost.


# Practical 7

## Summary

In this practical, we implemented the Making Change Problem using Dynamic Programming. The program takes a set of coin denominations and a target amount from the user. It uses a dynamic programming array to find the minimum number of coins required to make the given amount.The program checks each amount step by step and compares the available coins to find the best possible combination. If the given amount cannot be formed using the available coins, the program displays an appropriate message. It also calculates the execution time and displays the time and space complexity.

## Conclusion

Through this practical, we learned how Dynamic Programming can be used to solve the Making Change Problem efficiently. Instead of calculating the same values repeatedly, the program stores previously calculated results and uses them to find the minimum number of coins.This practical helped us understand how a real-life problem like finding the minimum number of coins can be solved using an algorithmic approach.


# Practical 8

## Summary

In this practical, we implemented Breadth First Search (BFS) and Depth First Search (DFS) using an adjacency list to represent a graph. BFS uses a queue to visit the nodes level by level, while DFS uses recursion to explore one path as deeply as possible before moving to another path.By implementing both methods, we understood how graph traversal works and how the same graph can be explored in different ways depending on the algorithm used.

## Conclusion

Through this practical, we learned the basic working of BFS and DFS and how they can be implemented using an adjacency list. BFS is useful when we want to explore a graph level by level, whereas DFS is useful when we want to follow a path deeply before backtracking.Overall, this practical helped us understand graph traversal in a simple and practical way. Implementing both algorithms also made it easier to see the difference between using a queue in BFS and recursion in DFS.


# Practical 9

## Summary

In this practical, we implemented Prim’s Algorithm to find the Minimum Spanning Tree (MST) of a weighted graph. The graph contains four vertices A, B, C, and D, and is represented using an adjacency matrix. The algorithm starts from vertex A and repeatedly selects the smallest-weight edge that connects a selected vertex to an unselected vertex.The program keeps track of the selected vertices, adds the appropriate edges to the Minimum Spanning Tree, and calculates the total cost of the selected edges.

## Conclusion

Through this practical, we learned how Prim’s Algorithm can be used to connect all the vertices of a weighted graph with minimum total cost. We understood how the algorithm gradually builds the Minimum Spanning Tree by choosing the smallest suitable edge at each step.Implementing the algorithm using Python made the concept easier to understand because we could see how the selected vertices and edges change step by step. Overall, this practical helped us understand Minimum Spanning Trees, greedy algorithms, and the practical use of Prim’s Algorithm.
