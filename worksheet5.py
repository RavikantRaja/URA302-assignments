#q1
import numpy as np
from scipy import stats

arr = np.random.rand(20) * 100
mean = np.mean(arr)
median = np.median(arr)
variance = np.var(arr)

print("Array:", arr)
print("Mean:", mean)
print("Median:", median)
print("Variance:", variance)


#q2
import numpy as np
from scipy.fftpack import fft2

data = np.random.rand(5,5)
fft_result = fft2(data)

print("Original Data:\n", data)
print("FFT Result:\n", fft_result)


#q3
import numpy as np
from scipy import linalg

A = np.array([[4, 2], [3, 1]])
det = linalg.det(A)
inv = linalg.inv(A)
eigvals, eigvecs = linalg.eig(A)

print("Determinant:", det)
print("Inverse:\n", inv)
print("Eigenvalues:", eigvals)
print("Eigenvectors:\n", eigvecs)


#q4
import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 10)
y = np.sin(x)
f = interpolate.interp1d(x, y, kind='cubic')
xnew = np.linspace(0, 10, 100)
ynew = f(xnew)

plt.plot(x, y, 'o', label="Data")
plt.plot(xnew, ynew, '-', label="Cubic Interpolation")
plt.legend()
plt.show()


#q5
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

t = np.linspace(0, 1, 500, endpoint=False)
data = np.sin(2*np.pi*5*t) + 0.5*np.random.randn(500)

b, a = signal.butter(3, 0.05)
filtered = signal.filtfilt(b, a, data)

plt.plot(t, data, label="Noisy Signal")
plt.plot(t, filtered, label="Filtered Signal")
plt.legend()
plt.show()


#q6
import numpy as np

sales = np.random.randint(100, 500, size=(12,4))  # 12 months, 4 products
total_sales = np.sum(sales)
avg_sales = np.mean(sales)
max_month = np.argmax(np.sum(sales, axis=1)) + 1
min_month = np.argmin(np.sum(sales, axis=1)) + 1

print("Total Sales:", total_sales)
print("Average Sales:", avg_sales)
print("Best Month:", max_month)
print("Worst Month:", min_month)


#q7
import pandas as pd

data = {
    "Name":["Arin","Aditya","Chirag","Gurleen","Kunal"],
    "Math":[85,79,90,66,70],
    "Physics":[78,82,85,75,68],
    "Chemistry":[92,74,89,80,75],
    "English":[88,90,92,78,85]
}
df = pd.DataFrame(data)
df["Total"] = df.iloc[:,1:].sum(axis=1)
df["Average"] = df.iloc[:,1:5].mean(axis=1)

print(df)
print("Top Performer:", df.loc[df["Total"].idxmax()])
print("Bottom Performer:", df.loc[df["Total"].idxmin()])


#q8
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

t = np.array([0,1,2,3,4,5])
v = np.array([2,3.1,7.9,18.2,34.3,56.2])

def model(t,a,b,c): return a*t**2 + b*t + c
params, _ = curve_fit(model, t, v)
a,b,c = params
print("a,b,c =", params)

plt.scatter(t,v,label="Data")
plt.plot(t, model(t,a,b,c), 'r-', label="Fit")
plt.legend()
plt.show()


#q9
df.iloc[:,1:5].plot(kind="bar")
plt.title("Subject-wise Marks")
plt.show()



#q10
plt.scatter(t,v,label="Original Data")
plt.plot(t, model(t,a,b,c), 'r-', label="Quadratic Fit")
plt.xlabel("Time")
plt.ylabel("Velocity")
plt.legend()
plt.show()


#q11
from scipy.stats import pearsonr
from scipy.interpolate import interp1d

years = np.array([2000,2005,2010,2015,2020])
pop = np.array([50,55,70,80,90])

corr,_ = pearsonr(years,pop)
print("Pearson Correlation:", corr)

f = interp1d(years, pop, kind='linear')
print("Population in 2008:", f(2008))


#12
import numpy as np
import matplotlib.pyplot as plt

coeff = [3,-5,2,-8]
roots = np.roots(coeff)
print("Roots:", roots)

x = np.linspace(-3,3,400)
y = np.polyval(coeff,x)
plt.plot(x,y)
plt.axhline(0,color='k')
plt.scatter(roots, [0]*len(roots), color='red')
plt.show()


#q13
import os, time

sizes = [200,400,600,800,1000]  # MB
times = []

for size in sizes:
    filename = f"file_{size}MB.txt"
    with open(filename,"w") as f:
        f.write("a"*size*1024*1024)  # random text
    
    start = time.time()
    with open(filename,"r") as f:
        data = f.read().upper()
    end = time.time()
    times.append(end-start)

print("Times:", times)


#14
from scipy.optimize import minimize_scalar

f = lambda x: x**4 - 3*x**3 + 2
res = minimize_scalar(f, bounds=(-2,3), method="bounded")
print("Local minima at x =", res.x, "f(x) =", res.fun)

x = np.linspace(-2,3,400)
plt.plot(x,f(x))
plt.scatter(res.x,res.fun,color="red")
plt.show()


#q15
from scipy.integrate import odeint

def model(y,t):
    theta, dtheta = y
    dydt = [dtheta, -0.2*dtheta - theta]
    return dydt

y0 = [1,0]
t = np.linspace(0,20,200)
sol = odeint(model,y0,t)

plt.plot(t, sol[:,0])
plt.title("Damped Oscillation")
plt.xlabel("Time (s)")
plt.ylabel("Theta (rad)")
plt.show()

max_disp = np.max(sol[:,0])
t_max = t[np.argmax(sol[:,0])]
print("Max Displacement:", max_disp, "at time", t_max)
