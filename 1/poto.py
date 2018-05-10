import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 50)
y1 = 2*x + 1
y2 = x**2
plt.figure()
plt.plot(x, y1)
plt.figure(num=3)
plt.plot(x, y2)
plt.plot(x, y1,linestyle='--')
plt.xlim((-4,4))
plt.xlabel("I am x")

new_ticks = np.linspace(-4,4,8)
print(new_ticks)
plt.xticks(new_ticks)

plt.yticks([-4,-2,0,2],
           [r'go xd',r'$nece\ \alpha$',r'percet',r'$2x$'])#用$$符号包括起来，使其按照数学字体输出，空格需要用\转义,前加r表示正则表达

#"gca" = get current axis
ax=plt.gca()
ax.spines['right'].set_color('none')#坐标轴,设置颜色为none，即没有
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position("bottom")#下放坐标轴为x
ax.yaxis.set_ticks_position("left")
ax.spines['bottom'].set_position(('axes',0.5))#将横轴放在纵轴的多少比例处
ax.spines['left'].set_position(('data',0))
plt.show()