"""
Chapter 1 - Introduction: the Hodgkin-Huxley Model.

Integrates the full four-variable Hodgkin-Huxley system (V, m, n, h) with a
custom 4th-order Runge-Kutta solver and plots the resulting voltage trace,
as an introductory reproduction of the model's spiking behaviour under
constant applied current.
"""

import numpy as np
import matplotlib.pyplot as plt

# Hodgkin-Huxley ODEs:
# dv/dt = (1/C)*(I-g_Na*m**3*h*(v-E_Na)-g_K*n**4(v-E_K)-gL*(v-E_L))
# dm/dt = a_m*(1-m)-b_m*m
# dn/dt = a_n*(1-n)-b_n*n
# dh/dt = a_h*(1-h)-b_h*h

# Initialize parameters for Hodgkin-Huxley model
t = 200               # Simulation time in ms
E_Na = 45            # Sodium reversal potential (mV)
E_K = -82            # Potassium reversal potential (mV)
E_L = -59            # Leakage reversal potential (mV)
g_Na = 120           # Sodium conductance (mS/cm^2)
g_K = 36             # Potassium conductance (mS/cm^2)
g_L = 0.3            # Leakage conductance (mS/cm^2)
C = 1                # Membrane capacitance (uF/cm^2)
I = 7.0              # External current (μA/cm2)
delta_t = 2**(-10)   # Time step for numerical integration

N = int(t / delta_t) # Number of time steps

# Initialize arrays for voltage and gating variables
v = np.zeros(N+1)
m = np.zeros(N+1)
n = np.zeros(N+1)
h = np.zeros(N+1)
t_value = np.linspace(0, t, N+1)  # Time vector


# Define Alpha rate functions
def a_m(v):
  return ((v + 45) / 10) / (1 - np.exp(-(v + 45) / 10))

def a_n(v):
  return ((v + 60) / 100) / (1 - np.exp(-(v + 60) / 10))

def a_h(v):
  return 0.07 * np.exp(-(v + 70) / 20)


# Define Beta rate functions
def b_m(v):
  return 4 * np.exp(-(v + 70) / 18)

def b_n(v):
  return (1 / 8) * np.exp(-(v + 70) / 80)

def b_h(v):
  return 1 / (1 + np.exp(-(v + 40) / 10))


# Define Limiting Functions for steady-state values and time constants
def m_inf(v):
  return a_m(v) / (a_m(v) + b_m(v))

def tau_m(v):
  return 1 / (a_m(v) + b_m(v))

def n_inf(v):
  return a_n(v) / (a_n(v) + b_n(v))

def tau_n(v):
  return 1 / (a_n(v) + b_n(v))

def h_inf(v):
  return a_h(v) / (a_h(v) + b_h(v))

def tau_h(v):
  return 1 / (a_h(v) + b_h(v))


# Define functions for differential equations
def f(t, v, m, n, h):
  # Membrane voltage differential equation
  return (1 / C) * (I - g_Na * (m ** 3) * h * (v - E_Na) - g_K * (n ** 4) * (v - E_K) - g_L * (v - E_L))

def f_m(t, v, m):
  return a_m(v) * (1 - m) - b_m(v) * m

def f_n(t, v, n):
  return a_n(v) * (1 - n) - b_n(v) * n

def f_h(t, v, h):
  return a_h(v) * (1 - h) - b_h(v) * h


# Collect all differential equations into a vector
def F(t, v, m, n, h):
  K_1 = []
  K_1.append(f(t, v, m, n, h))
  K_1.append(f_m(t, v, m))
  K_1.append(f_n(t, v, n))
  K_1.append(f_h(t, v, h))
  return np.array(K_1)


# Runge-Kutta 4th-order method for numerical integration
def runge_kutta(delta_t, t, v, m, n, h):
  vmnh = []
  K_1 = delta_t * F(t, v, m, n, h)
  K_2 = delta_t * F(t + 0.5 * delta_t, v + 0.5 * K_1[0], m + 0.5 * K_1[1], n + 0.5 * K_1[2], h + 0.5 * K_1[3])
  K_3 = delta_t * F(t + 0.5 * delta_t, v + 0.5 * K_2[0], m + 0.5 * K_2[1], n + 0.5 * K_2[2], h + 0.5 * K_2[3])
  K_4 = delta_t * F(t + delta_t, v + K_3[0], m + K_3[1], n + K_3[2], h + K_3[3])
  vmnh.append(v + (1 / 6) * (K_1[0] + 2 * K_2[0] + 2 * K_3[0] + K_4[0]))
  vmnh.append(m + (1 / 6) * (K_1[1] + 2 * K_2[1] + 2 * K_3[1] + K_4[1]))
  vmnh.append(n + (1 / 6) * (K_1[2] + 2 * K_2[2] + 2 * K_3[2] + K_4[2]))
  vmnh.append(h + (1 / 6) * (K_1[3] + 2 * K_2[3] + 2 * K_3[3] + K_4[3]))
  return vmnh

v[0] = -70
m[0] = a_m(v[0]) / (a_m(v[0]) + b_m(v[0]))
n[0] = a_n(v[0]) / (a_n(v[0]) + b_n(v[0]))
h[0] = a_h(v[0]) / (a_h(v[0]) + b_h(v[0]))

for i in range(N):
    vmnh = runge_kutta(delta_t, t_value[i], v[i], m[i], n[i], h[i])
    v[i+1] = vmnh[0]
    m[i+1] = vmnh[1]
    n[i+1] = vmnh[2]
    h[i+1] = vmnh[3]

# Plot:
plt.figure(figsize=(12, 6))

# Plot v:
plt.plot(t_value, v, 'black')
plt.xlim(min(t_value), max(t_value))
plt.ylim(-100, 50)
plt.xlabel('t [ms]')
plt.ylabel('v [mv]')
plt.title('Voltage trace')
plt.show()
