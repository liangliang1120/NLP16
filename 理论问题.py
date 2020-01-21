Why we need γ in reinforcement learning ?
Ans:1.防止状态间循环，造成reward无穷大；2.越是后期的reward越是价值低。

Please breifly explain what is value function and what is Q function ?
Ans:value function，到某个状态的reward期望值;Q function,确定了某个action之后reward期望值。

How temperal difference related to dynamic programming and monte-carlo methods ?
Ans:temperal difference用monte-carlo methods采样，用dynamic programming计算。

Please briefly describe what are value iteration and policy iteration ?
Ans:value iteration：已知policy和马尔科夫决策过程的情况下，根据策略获得最优值函数和最优策略；
    policy iteration：在policy未知的情况下，根据每次的reward学到最优policy。

How can we use deep lerning in reinforcement learning ?
Ans:对话系统：用likelihood或互信息来评价模型好坏。

