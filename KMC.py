
import numpy as np
import domain
import os
import interpreter
import potentiel
import sys



def KMC2D(config, kT, deltamu, nb_pas_temps, gif=False, gamma=False, rugosity=False):
    Ng=0
    deltatemps_reel=0
    os.makedirs("frames", exist_ok=True)
    N=len(config)
    nb_adsorption=0
    nb_desorption=0
    
    # Initialisation des paramètres en fonction du temps
    parametres=[]
    if gamma:
        Gamma = []
    if rugosity:
        Rugosity = []

    positions_surface = domain.find_surface(config)

    for iteration in range(nb_pas_temps):
        # Étape 1 : Générer la liste des 2N événements possibles
        #(site,0 = désorption ou 1 = adsorption)
        typeEvnt=[0,1]
        listeEvnt=[]
        

        for site in range(N):
            for adOuDes in typeEvnt:
                listeEvnt.append((site,adOuDes))

        # Étape 2 : Calcul des w de chaque événement
        w_liste=[]
        for i in listeEvnt:
            if i[1]==1:
                w=np.exp(deltamu/kT)
                w_liste.append(w)
            if i[1]==0:
                deltaE = potentiel.potentielEvnt(config, i, positions_surface)
                w=np.exp(-deltaE/kT)
                w_liste.append(w)

        W=np.sum(w_liste)

        # Étape 3 : Normalisation
        w_normalisee=[w/W for w in w_liste]

        # Étape 4 : On génère un nombre aléatoire en 0 et 1 et on choisit le premier événement qui a une proba cumulée supérieure à r.
        nombre_r=np.random.rand()
        somme=0
        compteur=0
        proba_cumulée=[]
        for i in w_normalisee:
            somme+=i
            proba_cumulée.append(somme)
            if somme>nombre_r:
                break
            compteur+=1
        
        # print(compteur)
        # print(len(listeEvnt))
        # print(listeEvnt)
        evnt=listeEvnt[compteur]
        
        
        if evnt[1]==1:
            Ng+=1
            nb_adsorption+=1
            # print(f"L'événement est une adsorption au site {evnt[0]}")
        if evnt[1]==0:
            nb_desorption+=1
            # print(f"L'événement est une désorption au site {evnt[0]}")
        

        # Réécrit les 3 lignes
        # print(f"Événement {iteration} / {len(nb_pas_temps)}")
        # print(f"Total adsorbé : {nb_adsorption}")
        # print(f"Total évaporé : {nb_desorption}")

        # Étape 5 : Nouvelle configuration
        site_changement=evnt[0]

        # Cas désorption
        if evnt[1]==0:
            if config[site_changement][positions_surface[site_changement][1]-1]==None:
                if gif:
                    interpreter.save_graph(config,iteration,deltatemps_reel)
                continue
            config[site_changement][positions_surface[site_changement][1]-1]=None
            positions_surface[site_changement][1]-=1
        
        # Cas adsorption
        if evnt[1]==1:
            if positions_surface[site_changement][1] == config.shape[1]-1:
                print("La configuration a atteint le plafond")
                break
            # Si somme de position de surface et site changement et paire, alors le prochain est un 0
            if (positions_surface[site_changement][1]+site_changement)%2==0:
                config[site_changement][positions_surface[site_changement][1]]=1
                positions_surface[site_changement][1]+=1
            else:
                config[site_changement][positions_surface[site_changement][1]]=0
                positions_surface[site_changement][1]+=1



        # Étape 6  : Assigner un temps
        nombre_r_temps=np.random.rand()
        deltatemps_reel+=-1/(W*np.log(nombre_r_temps))

        
        if gif:
            interpreter.save_graph(config,iteration,deltatemps_reel)

        # Calculs des paramètres d'intérêt
        if gamma:
            # Paramètres d'intérêt
            wa=np.exp(deltamu/kT)
            Gamma.append(Ng/(wa*deltatemps_reel) )
        if rugosity:
            Rugosity.append(domain.fct_rugosite(positions_surface))
    

    if gamma:
        parametres.append(Gamma)
    if rugosity:
        parametres.append(Rugosity)

            # print(f"L'événement est une désorption au site {evnt[0]}")
    


    return config, deltatemps_reel, parametres

def KMC2D2(config, kT, deltamu, nb_pas_temps, gif=False, gamma=False, rugosity=False):
    Ng=0
    deltatemps_reel=0
    os.makedirs("frames", exist_ok=True)
    N=len(config)


    positions_surface = domain.find_surface(config)

    for iteration in range(nb_pas_temps):
        # Étape 1 : Générer la liste des 2N événements possibles
        #(site,0 = désorption ou 1 = adsorption)
        typeEvnt=[0,1]
        listeEvnt=[]
        

        for site in range(N):
            for adOuDes in typeEvnt:
                listeEvnt.append((site,adOuDes))

        # Étape 2 : Calcul des w de chaque événement
        w_liste=[]
        for i in listeEvnt:
            if i[1]==1:
                w=np.exp(deltamu/kT)
                w_liste.append(w)
            if i[1]==0:
                deltaE = potentiel.potentielEvnt(config, i, positions_surface)
                w=np.exp(-deltaE/kT)
                w_liste.append(w)

        W=np.sum(w_liste)

        # Étape 3 : Normalisation
        w_normalisee=[w/W for w in w_liste]

        # Étape 4 : On génère un nombre aléatoire en 0 et 1 et on choisit le premier événement qui a une proba cumulée supérieure à r.
        nombre_r=np.random.rand()
        somme=0
        compteur=0
        proba_cumulée=[]
        for i in w_normalisee:
            somme+=i
            proba_cumulée.append(somme)
            if somme>nombre_r:
                break
            compteur+=1
    
        evnt=listeEvnt[compteur]
        


        # Étape 5 : Nouvelle configuration
        site_changement=evnt[0]

        # Cas désorption
        if evnt[1]==0:
            if config[site_changement][positions_surface[site_changement][1]-1]==None:
                if gif:
                    interpreter.save_graph(config,iteration,deltatemps_reel)
                continue
            config[site_changement][positions_surface[site_changement][1]-1]=None
            positions_surface[site_changement][1]-=1
        
        # Cas adsorption
        if evnt[1]==1:
            if positions_surface[site_changement][1] == config.shape[1]-1:
                print("La configuration a atteint le plafond")
                break
            # Si somme de position de surface et site changement et paire, alors le prochain est un 0
            if (positions_surface[site_changement][1]+site_changement)%2==0:
                config[site_changement][positions_surface[site_changement][1]]=1
                positions_surface[site_changement][1]+=1
            else:
                config[site_changement][positions_surface[site_changement][1]]=0
                positions_surface[site_changement][1]+=1



        # Étape 6  : Assigner un temps
        nombre_r_temps=np.random.rand()
        deltatemps_reel+=-1/(W*np.log(nombre_r_temps))

        
        if gif:
            interpreter.save_graph(config,iteration,deltatemps_reel)

    if gamma:
        # Paramètres d'intérêt
        wa=np.exp(deltamu/kT)
        Gamma = Ng/(wa*deltatemps_reel)
    if rugosity:
        Rugosity = domain.fct_rugosite(positions_surface)

    parametres = []
    if gamma:
        parametres.append(Gamma)
    if rugosity:
        parametres.append(Rugosity)

            # print(f"L'événement est une désorption au site {evnt[0]}")
    


    return config, deltatemps_reel, parametres

def calcul_temps_KMC(x, y, nb_pas_temps, iterations):
    import time
    grid = domain.create_grid(x, y)
    elapsed_time = []
    kT, param_mu = 1.25,0.25

    for i in range(iterations):
        start_time = time.time()
        KMC2D2(grid, kT, param_mu, nb_pas_temps, gif=False, gamma=True, rugosity=True)
        end_time = time.time()
        elapsed_time.append(end_time - start_time)
    
    std_times = np.std(elapsed_time)

    return np.mean(elapsed_time), std_times

def calcul_temps_allonger(x, y, nb_pas_temps_max, iterations):
    import matplotlib.pyplot as plt
    from scipy.optimize import curve_fit

    nb_pas = np.arange(1,nb_pas_temps_max,2)
    mean_time = []
    std_time = []

    for pas in nb_pas:
        mean, std = calcul_temps_KMC(x, y, pas, iterations)
        mean_time.append(mean)
        std_time.append(std)
    
    plt.figure()
    plt.errorbar(nb_pas, mean_time, yerr=std_time, fmt='.', markersize=10, capsize=5, label='Temps moyen ± écart-type')
    plt.xlabel('Nombre de pas de temps')
    plt.ylabel('Temps moyen (s)')
    plt.title(f'Temps de calcul pour KMC \npour un substrat {x}x{y} (itération {iterations})')
    plt.grid()
    plt.show()

# calcul_temps_allonger(x=50, y=100, nb_pas_temps_max=25, iterations=3)

