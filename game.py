import gymnasium as gym
import gym_super_mario_bros
from nes_py.wrappers import JoypadSpace
from gym_super_mario_bros.actions import SIMPLE_MOVEMENT

env = gym.make("SuperMarioBros-1-1-v0")

env = JoypadSpace(env, SIMPLE_MOVEMENT)
env.reset(seed=42)

total = 0.0

for t in range(60):
    obs, reward, terminated, truncated, info = env.step(1)
    total += reward
    if t % 10 == 0:
        print(f"t={t:2d}  x_pos={info['x_pos']}  reward={reward}")
print("final x_pos:", info["x_pos"], "| distance:", info["x_pos"] - 40)
print("coins:", info["coins"])
print("total reward: ", total)
print("time left:", info["time"])
print("last reward breakdown:", info["reward_components"])