import domain
from KMC import KMC2D2 as KMC2D
import matplotlib.pyplot as plt
import numpy as np
import time

# Definition du substrat
x = 50
y = 50
grid = domain.create_grid(x,y)     # [hauteur, largeur]

liste_kT = [0.50, 0.75, 1.00, 1.25, 1.50, 1.75, 2.00]
liste_deltamu = np.linspace(-1.0, 1.0, 11)

nb_pas_temps = 1
gif = False

kT = liste_kT[3]
deltamu = liste_deltamu[5]

nb_iterations = 2

temps_1KMC = 0.5

temps_estimer =  5 * (temps_1KMC * nb_pas_temps * (x/50)) * nb_iterations
print(f"Temps estime: {temps_estimer} secondes")




liste_moy_gamma_kbt=[]
liste_moy_rugosite_kbt=[]
liste_std_gamma_kbt=[]
liste_std_rugosite_kbt=[]
start_big = time.time()
for param_kbT in liste_kT:
    # print(param_kbT)
    liste_gamma=[]
    liste_rugosite=[]
    # start = time.time()
    for b in range(nb_iterations):
        grid_f, deltatemps_reel, parametres = KMC2D(grid, param_kbT, deltamu, nb_pas_temps,gamma=True, rugosity=True)
        # print(parametres)
        gamma_iteration=parametres[0]
        liste_gamma.append(gamma_iteration)

        rugosite_iteration=parametres[1]
        liste_rugosite.append(rugosite_iteration)
    # end = time.time()
    # print("Temps d'execution : ", end-start)

    gamma_moy_param=np.mean(liste_gamma)
    rugosite_moy_param=np.mean(liste_rugosite)

    gamma_std_param=np.std(liste_gamma)
    rugosite_std_param=np.std(liste_gamma)

    liste_moy_gamma_kbt.append(gamma_moy_param)
    liste_moy_rugosite_kbt.append(rugosite_moy_param)

    liste_std_gamma_kbt.append(gamma_std_param)
    liste_std_rugosite_kbt.append(rugosite_std_param)
# end_big = time.time()
# print("Temps d'execution total : ", end_big-start_big)

liste_gamma_moy_mu=[]
liste_rugosite_moy_mu=[]
liste_gamma_std_mu=[]
liste_rugosite_std_mu=[]

for param_mu in liste_deltamu:
    # print(param_mu)
    liste_gamma=[]
    liste_rugosite=[]
    for b in range(nb_iterations):
        # start = time.time()        

        grid_f, deltatemps_reel, parametres = KMC2D(grid, kT, param_mu, nb_pas_temps,gamma=True, rugosity=True)

        gamma_iteration=parametres[0]
        liste_gamma.append(gamma_iteration)

        rugosite_iteration=parametres[1]
        liste_rugosite.append(rugosite_iteration)
        # end = time.time()
        # print("Temps d'execution : ", end-start)

    gamma_moy_param=np.mean(liste_gamma)
    rugosite_moy_param=np.mean(liste_rugosite)

    gamma_std_param=np.std(liste_gamma)
    rugosite_std_param=np.std(liste_gamma)

    liste_gamma_moy_mu.append(gamma_moy_param)
    liste_rugosite_moy_mu.append(rugosite_moy_param)

    liste_gamma_std_mu.append(gamma_std_param)
    liste_rugosite_std_mu.append(rugosite_std_param)
end_big = time.time()
print("Temps par KMC : ", (end_big-start_big)/(11+5))
print("Temps d'execution total : ", (end_big-start_big))

