
import numpy as np
import gymnasium as gym
import os
import matplotlib.pyplot as plt


class Maze:
    def __init__(self, task, obs_key="image", act_key="action", size=(64, 64), seed=0):
        # 9x9, 11x11, 13x13 and 15x15 are available
        import gym_maze
        self._env = gym.make(task,apply_api_compatibility=True)
        self._obs_is_dict = hasattr(self._env.observation_space, "spaces")
        self._obs_key = obs_key
        self._act_key = act_key
        self._size = size
        self._gray = False
        os.environ['SDL_VIDEODRIVER'] = 'dummy'

    def __getattr__(self, name):
        if name.startswith("__"):
            raise AttributeError(name)
        try:
            return getattr(self._env, name)
        except AttributeError:
            raise ValueError(name)

    @property
    def observation_space(self):
        if self._obs_is_dict:
            spaces = self._env.observation_space.spaces.copy()
        else:
            spaces = {self._obs_key: self._env.observation_space}
        return gym.spaces.Dict(
            {
                **spaces,
                "is_first": gym.spaces.Box(0, 1, (), dtype=bool),
                "is_last": gym.spaces.Box(0, 1, (), dtype=bool),
                "is_terminal": gym.spaces.Box(0, 1, (), dtype=bool),
            }
        )

    @property
    def action_space(self):
        space = self._env.action_space
        space.discrete = True
        return space

    def step(self, action):
        obs , reward,terminated, truncated ,info = self._env.step(action)
        # obs= self.render()
        # plt.imshow(obs)
        # plt.axis('off')  # 可选：隐藏坐标轴
        # plt.show()
        if not self._obs_is_dict:
            obs = {self._obs_key: obs}
        obs["is_first"] = False
        obs["is_last"] = terminated
        obs["is_terminal"] = info.get("is_terminal", False)
        return obs, reward, terminated, info
    def render(self):
        return self._env.render()
    def reset(self,seed=None,options={}):
        obs = self._env.reset(seed=seed,options=options)
        obs = self.render()
        if not self._obs_is_dict:
            obs = {self._obs_key: obs}
        obs["is_first"] = True
        obs["is_last"] = False
        obs["is_terminal"] = False
        return obs

