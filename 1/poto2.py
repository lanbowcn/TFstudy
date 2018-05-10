import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 50)
y1 = 2*x + 1
y2 = x**2
plt.figure()

plt.xlim((-4,4))
plt.xlabel("I am x")

new_ticks = np.linspace(-4,4,8)
print(new_ticks)
plt.xticks(new_ticks)

plt.yticks([-4,-2,0,2],
           [r'go xd',r'$nece\ \alpha$',r'percet',r'$2x$'])#用$$符号包括起来，使其按照数学字体输出，空格需要用\转义,前加r表示正则表达




l1, = plt.plot(x,y1,label='up')
l2, = plt.plot(x,y2,linestyle='--',label='down')#对线的返回值为l1，l2，加逗号是为了传入下方handles
#plt.legend()
plt.legend(handles=[l1,l2],labels=['aaa','bbb'],loc='best')#loc  best会选不影响的位置，还可以用'upper right''lower right'
#handles 与labels对应，标签为aaa，bbb，只打印一个aaa，则吧bbb去掉
plt.show()