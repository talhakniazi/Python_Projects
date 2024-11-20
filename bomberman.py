import random
import time
import threading

# Game constants
GRID_SIZE = 7
EMPTY, WALL, BOMB, PLAYER, EXPLOSION = ' ', '#', 'B', 'P', '*'
BOMB_TIMER = 3  # Bomb explodes after 3 seconds

class BombermanGame:
    def __init__(self):
        # Initialize grid
        self.grid = [[EMPTY] * GRID_SIZE for _ in range(GRID_SIZE)]
        self.place_walls()
        
        # Place player
        self.player_position = [0, 0]
        self.grid[0][0] = PLAYER

    def place_walls(self):
        # Place random walls on the grid
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                if random.random() < 0.2 and (i, j) != (0, 0):
                    self.grid[i][j] = WALL

    def display_grid(self):
        # Print the grid
        for row in self.grid:
            print(' '.join(row))
        print("\nUse W/A/S/D to move, 'B' to place a bomb, and 'Q' to quit.")

    def move_player(self, direction):
        x, y = self.player_position
        dx, dy = {'W': (-1, 0), 'A': (0, -1), 'S': (1, 0), 'D': (0, 1)}.get(direction, (0, 0))
        nx, ny = x + dx, y + dy
        
        if 0 <= nx < GRID_SIZE and 0 <= ny < GRID_SIZE and self.grid[nx][ny] == EMPTY:
            self.grid[x][y] = EMPTY
            self.player_position = [nx, ny]
            self.grid[nx][ny] = PLAYER

    def place_bomb(self):
        x, y = self.player_position
        if self.grid[x][y] == PLAYER:
            bomb_position = (x, y)
            self.grid[x][y] = BOMB
            
            # Start a separate thread to handle bomb explosion after the timer
            threading.Thread(target=self.bomb_timer, args=(bomb_position,), daemon=True).start()

    def bomb_timer(self, position):
        time.sleep(BOMB_TIMER)
        self.explode_bomb(position)

    def explode_bomb(self, position):
        x, y = position
        
        # Explosion pattern: affects up, down, left, right, and the bomb's position itself
        affected_positions = [(x, y), (x-1, y), (x+1, y), (x, y-1), (x, y+1)]
        
        for ax, ay in affected_positions:
            if 0 <= ax < GRID_SIZE and 0 <= ay < GRID_SIZE:
                if self.grid[ax][ay] == WALL or self.grid[ax][ay] == BOMB:
                    self.grid[ax][ay] = EXPLOSION
                elif self.grid[ax][ay] == PLAYER:
                    print("Game Over! You were caught in the explosion!")
                    self.grid[ax][ay] = EXPLOSION
                    self.display_grid()
                    exit()

        # Display explosion for a moment, then clear
        self.display_grid()
        time.sleep(0.5)
        
        for ax, ay in affected_positions:
            if 0 <= ax < GRID_SIZE and 0 <= ay < GRID_SIZE:
                self.grid[ax][ay] = EMPTY

    def play(self):
        self.display_grid()
        while True:
            move = input("Enter move: ").strip().upper()
            if move == 'Q':
                print("Thanks for playing Bomberman!")
                break
            elif move in ('W', 'A', 'S', 'D'):
                self.move_player(move)
            elif move == 'B':
                self.place_bomb()
            self.display_grid()

# Run the game
if __name__ == "__main__":
    game = BombermanGame()
    game.play()
