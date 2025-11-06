#task 1
board = [" " for _ in range(9)]  

def print_board():
   
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")

def player_move(player_icon):
    
    while True:
        try:
            choice = int(input(f"Player {player_icon}, enter your move (1-9): ")) - 1
            if 0 <= choice <= 8 and board[choice] == " ":
                board[choice] = player_icon
                break
            else:
                print("Invalid move. Please choose an empty spot (1-9).")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")

def check_win(player_icon):
    
    # Check rows
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] == player_icon:
            return True
    # Check columns
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] == player_icon:
            return True
    # Check diagonals
    if board[0] == board[4] == board[8] == player_icon:
        return True
    if board[2] == board[4] == board[6] == player_icon:
        return True
    return False

def check_draw():
    
    return " " not in board

def play_game():
    
    current_player = "X"
    while True:
        print_board()
        player_move(current_player)
        if check_win(current_player):
            print_board()
            print(f"Player {current_player} wins!")
            break
        if check_draw():
            print_board()
            print("It's a draw!")
            break
        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    print("Welcome to Tic-Tac-Toe!")
    play_game()



#Task 2
def add_task(tasks):
    task = input("Enter the new task: ")
    tasks.append(task)
    print(f"✅ Task '{task}' added successfully!\n")


def view_tasks(tasks):
    if len(tasks) == 0:
        print("📝 No tasks found. Your to-do list is empty.\n")
    else:
        print("\nYour To-Do List:")
        for index, task in enumerate(tasks):
            print(f"{index + 1}. {task}")
        print()  # Blank line for spacing


def delete_task(tasks):
    if len(tasks) == 0:
        print("⚠️ No tasks to delete.\n")
        return

    view_tasks(tasks)
    try:
        index = int(input("Enter the task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            removed_task = tasks.pop(index)
            print(f"🗑️ Task '{removed_task}' deleted successfully!\n")
        else:
            print("❌ Invalid task number. Please try again.\n")
    except ValueError:
        print("❌ Please enter a valid number.\n")


def main():
    tasks = []
    while True:
        print("========== TO-DO LIST MENU ==========")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")
        print("====================================")
        
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            delete_task(tasks)
        elif choice == '4':
            print("👋 Exiting the To-Do List Application. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please select a valid option.\n")


if __name__ == "__main__":
    main()


#Task 3

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def astar(grid, start, goal):
    rows, cols = grid.shape

    open_set = [start]        
    came_from = {}             
    g_score = {start: 0}        
    f_score = {start: heuristic(start, goal)}  

    while open_set:

        current = min(open_set, key=lambda x: f_score.get(x, float('inf')))

        if current == goal:

            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]  

        open_set.remove(current)


        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            neighbor = (current[0]+dx, current[1]+dy)


            if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols:
                if grid[neighbor] == 1:  
                    continue

                tentative_g = g_score[current] + 1


                if tentative_g < g_score.get(neighbor, float('inf')):
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g
                    f_score[neighbor] = tentative_g + heuristic(neighbor, goal)
                    if neighbor not in open_set:
                        open_set.append(neighbor)

    return None 


def visualize(grid, path, start, goal):
    plt.figure(figsize=(6,6))
    plt.imshow(grid, cmap='Greys', origin='upper')


    if path:
        y_coords = [p[1] for p in path]
        x_coords = [p[0] for p in path]
        plt.plot(y_coords, x_coords, 'ro-', label='Path')


    plt.scatter(start[1], start[0], c='green', s=100, label='Start')
    plt.scatter(goal[1], goal[0], c='blue', s=100, label='Goal')

    plt.title("A* Pathfinding Visualization (Without heapq)")
    plt.legend()
    plt.show()



def main():
    while True:
        rows = int(input("Enter number of rows: "))
        cols = int(input("Enter number of columns: "))
        grid = np.zeros((rows, cols), dtype=int)


        num_obstacles = int(input("Enter number of obstacles: "))
        for i in range(num_obstacles):
            r, c = map(int, input(f"Enter obstacle {i+1} position (row col): ").split())
            if 0 <= r < rows and 0 <= c < cols:
                grid[r][c] = 1


        start = tuple(map(int, input("Enter start position (row col): ").split()))
        goal = tuple(map(int, input("Enter goal position (row col): ").split()))

        print("\n🧩 Grid Representation (0 = Free, 1 = Obstacle):")
        print(pd.DataFrame(grid))

        path = astar(grid, start, goal)


        if path:
            print("\n✅ Path Found:")
            print(path)
        else:
            print("\n❌ No valid path found.")


        visualize(grid, path, start, goal)

        retry = input("Do you want to try again with new inputs? (y/n): ").lower()
        if retry != 'y':
            print("👋 Exiting the program. Goodbye!")
            break



if __name__ == "__main__":
    main()
