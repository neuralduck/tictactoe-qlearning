from tictactoe import Tictactoe
from minimax import minimax
from typing import List
import random
import pickle
import os
'''
notes:
for each episode
while true
current state = get state
action = pick an action
move as per that action
result = get result
reward = get reward
next state = get state
update q for the player

if game over and has reached a terminal state
update q one more time for both players and break

'''
class Qtable:
    def __init__(self):
        self.qtable = dict()
        self.alpha = 0.3
        self.gamma = 0.9

    def set_value(self, state, action, value) -> None:
        self.qtable.setdefault(state, [0 for i in range(9)])[action] = value 

    def get_values(self, state: str) -> List:
        return self.qtable.get(state, [0 for i in range(9)])

    def update_value(self, q0, q1, state, action, reward):
        q0[action] = q0[action] + self.alpha * (reward + self.gamma * max(q1) - q0[action])
        self.set_value(state, action, q0[action])

    def save_qtable(self):
        pass

    def load_qtable(self):
        pass


    def __str__(self):
        table = ''
        for key in self.qtable:
            table += f'{key}: {self.qtable.get(key, [0 for i in range(9)])}\n'
        return table


def get_reward(result, player):
    if player == 1:
        if result == 1:
            return 1
        elif result == -1:
            return -1
        elif result == 0:
            return 0.5
        else:
            return 0
    else:
        if result == 1:
            return -1
        elif result == -1:
            return 1
        elif result == 0:
            return 0.5
        else:
            return 0

def choose_action(state, moves, qtable, epsilon = 0.7) -> int:
    if random.uniform(0, 1) < epsilon:
        print("exploration")
        return random.choice(moves)
    else:
        print("exploitation")
        best_value = -float("inf")
        best_move = None
        for move in moves:
            value = qtable.get_values(state)[move]
            if value > best_value:
                best_value = value
                best_move = move
        return best_move


qtableX = Qtable()
qtableO = Qtable()
player1 = 1
player2 = -1
for episode in range(episodes):
    board = Tictactoe()
    while True:
        print('*'*30)
        print(board)
        current_state = board.get_state()
        q0 = qtableX.get_values(current_state)
        print(f"current state: {current_state}")
        print(f"values of current state: {q0}")

        result = board.check()
        if result != 3:
            #game over, terminal state reached
            #update qtable without next state
            print("terminal state reached")
            break
        else:
            action = choose_action(board.get_state(), board.available_moves(), qtableX)
            print(f"chosen action: {action}")

            board.move(action, player1)

            next_state = board.get_state()
            q1 = qtableX.get_values(next_state)
            print(f"next state: {next_state}")
            print(f"values of next state: {q1}")
            print(board)

            result = board.check()
            reward = get_reward(result, player1)
            print(f"result: {result}")
            print(f"reward: {reward}")
            qtableX.update_value(q0, q1, current_state, action, reward)
            print('Qtable X')
            print(qtableX)
            if result != 3:
                print("end of the episode")
                #end the episode
                break
        print('-'*30)
        print(board)
        current_state = board.get_state()
        q0 = qtableO.get_values(current_state)
        print(f"current state: {current_state}")
        print(f"values of current state: {q0}")

        result = board.check()
        if result != 3:
            #game over, terminal state reached
            #update qtable without next state
            print("terminal state reached")
            break
        else:
            action = choose_action(board.get_state(), board.available_moves(), qtableO)
            print(f"chosen action: {action}")

            board.move(action, player2)

            next_state = board.get_state()
            q1 = qtableO.get_values(next_state)
            print(f"next state: {next_state}")
            print(f"values of next state: {q1}")
            print(board)

            result = board.check()
            reward = get_reward(result, player2)
            print(f"result: {result}")
            print(f"reward: {reward}")

            qtableO.update_value(q0, q1, current_state, action, reward)
            print('Q table O')
            print(qtableO)
            if result != 3:
                print("end of the episode")
                #end the episode
                break
        print('*'*30)





    
    
