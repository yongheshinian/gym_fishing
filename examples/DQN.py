import gym
import gym_fishing
from stable_baselines3 import DQN
from stable_baselines3.common.evaluation import evaluate_policy
from leaderboard import leaderboard

# Create environment
env = gym.make('fishing-v0', file = "results/dqn.csv")
# Instantiate the agent
model = DQN('MlpPolicy', env, verbose=1)
# Train the agent
model.learn(total_timesteps=int(2e5))

# Save the agent
model.save("results/dqn_fish_v0")

# Evaluate the agent
mean_reward, std_reward = evaluate_policy(model, model.get_env(), n_eval_episodes=10)
print("mean reward:", mean_reward, "std:", std_reward)

## Simulation for visualization purposes
obs = env.reset()
for i in range(100):
  action, _state = model.predict(obs)
  obs, reward, done, info = env.step(action)
  env.render()

env.plot("results/dqn.png")
