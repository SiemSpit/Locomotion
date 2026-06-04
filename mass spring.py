# %%
import numpy as np
import matplotlib.pyplot as plt

# %%
# Systeemeigenschappen: massa (m), veerconstante (k), dempingscoëfficiënt (c)
m = 1.0
k = 1.0
c = 0.1

# Beginvoorwaarden
x0 = 0.1   # startpositie
v0 = 0.0   # startsnelheid
a0 = 0.0   # startversnelling

# Tijdstap bepalen op basis van de trillingstijd (periode)
periode = 2 * np.pi * np.sqrt(m / k)
dt = periode / 100
aantal_stappen = 1000

# %%
# Tijdsintegratie
posities = []
snelheden = []
versnellingen = []

# Initialiseer de huidige staat
x = x0
v = v0
a = a0

for _ in range(aantal_stappen):
    # Sla de huidige waarden op
    posities.append(x)
    snelheden.append(v)
    versnellingen.append(a)
    
    # Bereken de nieuwe versnelling, snelheid en positie
    a = (-k * x - c * v) / m
    v += a * dt
    x += v * dt

# %%
plt.figure(figsize=(12, 4))

# Positie plot
plt.subplot(1, 3, 1)
plt.plot(posities, color='tab:blue')
plt.title('Positie (x)')

# Snelheid plot
plt.subplot(1, 3, 2)
plt.plot(snelheden, color='tab:orange')
plt.title('Snelheid (v)')

# Versnelling plot
plt.subplot(1, 3, 3)
plt.plot(versnellingen, color='tab:green')
plt.title('Versnelling (a)')

plt.tight_layout()
plt.show()

# %%
# %%
# Forced response, f = 0.1 * np.sin(2 * np.pi * t / periode)

# Lege lijsten voor de nieuwe simulatie
posities_gedwongen = []
snelheden_gedwongen = []
versnellingen_gedwongen = []

# Reset de beginvoorwaarden voor deze nieuwe berekening
x = x0
v = v0
a = a0
t = 0.0  # We moeten nu ook de tijd bijhouden voor de sinusfunctie

amplitude_kracht = 0.5


# %%
for _ in range(aantal_stappen):
    # Sla de huidige waarden op
    posities_gedwongen.append(x)
    snelheden_gedwongen.append(v)
    versnellingen_gedwongen.append(a)
    
    # Bereken de externe kracht op tijdstip t
    f_ext = amplitude_kracht * np.sin(2 * np.pi * t / periode)
    
    # Bereken de nieuwe versnelling (inclusief de externe kracht f_ext)
    a = (-k * x - c * v + f_ext) / m
    
    # Update snelheid, positie en tijd voor de volgende stap
    v += a * dt
    x += v * dt
    t += dt

# %%
# %%
# Plot de resultaten van de gedwongen trilling
plt.figure(figsize=(12, 4))

# Positie plot (Gedwongen)
plt.subplot(1, 3, 1)
plt.plot(posities_gedwongen, color='tab:blue')
plt.title('Positie (x) - Gedwongen')
plt.xlabel('Tijdstap')

# Snelheid plot (Gedwongen)
plt.subplot(1, 3, 2)
plt.plot(snelheden_gedwongen, color='tab:orange')
plt.title('Snelheid (v) - Gedwongen')
plt.xlabel('Tijdstap')

# Versnelling plot (Gedwongen)
plt.subplot(1, 3, 3)
plt.plot(versnellingen_gedwongen, color='tab:green')
plt.title('Versnelling (a) - Gedwongen')
plt.xlabel('Tijdstap')

plt.tight_layout()
plt.show()


