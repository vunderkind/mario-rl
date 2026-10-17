import gymnasium as gym
import gym_super_mario_bros
from nes_py.wrappers import JoypadSpace
from gym_super_mario_bros.actions import SIMPLE_MOVEMENT

env = gym.make("SuperMarioBros-1-1-v0", render_mode="human", max_episode_steps=3000)
env = JoypadSpace(env, SIMPLE_MOVEMENT)

obs, info = env.reset(seed=42)

total_reward = 0.0
steps = 0
terminated = truncated = False

while not (terminated or truncated):
    action = env.action_space.sample()
    obs, reward, terminated, truncated, info = env.step(action)
    env.render()
    total_reward += reward
    steps += 1

print("Steps: ", steps)
print("total reward:", total_reward)
print("got as far as x_pos:", info["x_pos"])
print("terminated:", terminated, "| truncated:", truncated)
env.close()