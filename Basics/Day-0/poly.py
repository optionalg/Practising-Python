import scipy as sp
import matplotlib.pyplot as plt

x=sp.linespace(0, 1, 10)
x_long = sp.linspace(-0.1, 1.1, 100)

y=x+x**2-x**3 + 0.1 * sp.randn(len(x))

z = sp.polyfit(x,y,3)
p=sp.poly1d(z)
print (z)

z6=sp.ployfit(x,y,6)
p6=sp.polyid(z6)
print (z6)

plt.clf()
plt.plot(x,y,'b.', ms=18, label='Y')
plt.plot(x_long,p(x_long), 'r-', lw=5, label='3-degree poly')
plt.plot(x_long,p(x_long), 'g--', lw=6, label='6-degree poly')
plt.xlabel('X')
plt.legend(loc='best')

plt.show()
