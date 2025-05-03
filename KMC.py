
import numpy as np
import domain
import os
import interpreter
import potentiel_2D




def KMC2D(config,positions_surface, kT, deltamu, nb_pas_temps, gif=False, gamma=False, rugosity=False):
    Ng=0
    deltatemps_reel=0
    os.makedirs("frames", exist_ok=True)
    N=len(config)
    
    nb_atomes_final=0
    
    # Initialisation des paramètres en fonction du temps
    parametres=[]
    if gamma:
        Gamma = []
    if rugosity:
        Rugosity = []



    for iteration in range(nb_pas_temps):
        # Étape 1 : Générer la liste des 2N événements possibles
        #(site,0 = désorption, 1 = adsorption, 2 = diffusion)
        typeEvnt=[0,1,2]
        listeEvnt=[]
        tousmeme=False
        

        for site in range(N):
            for adOuDesouDiff in typeEvnt:
                listeEvnt.append((site,adOuDesouDiff))

        # Étape 2 : Calcul des w de chaque événement
        w_liste=[]
        for i in listeEvnt:

            if i[1]==0:
                deltaE = domain.potentiel(config,i,positions_surface)
                w=np.exp(-deltaE/kT)
                w_liste.append(w)

            if i[1]==1:
                w=np.exp(deltamu/kT)
                w_liste.append(w)

            if i[1]==2:
                w=np.exp(deltamu/(2*kT))  #TAUX ARBITRAIRE PAS PHYISIQUE
                w_liste.append(w)

        W=np.sum(w_liste)

        # Étape 3 : Normalisation
        w_normalisee=w_liste/W

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
        if evnt[1]==1:
            nb_atomes_final+=1
            Ng+=1
            print(f"{iteration}  L'événement est une adsorption au site {evnt[0]}")
        if evnt[1]==0:
            Ng-=1     
            print(f"{iteration}  L'événement est une désorption au site {evnt[0]}")
        

        # Étape 5 : Nouvelle configuration
        site_changement=evnt[0]

        # Cas diffusion
        # On détermine si l'atome est un Na ou Cl
        if ((positions_surface[site_changement][1]-1)+site_changement)%2==0:
            atome='Na'
        else : 
            atome='Cl'
        

        if evnt[1]==2: #ALORS ON A UNE DIFFUSION! ON TROUVE DONC LE PLUS PROCHE SITE COMPATIBLE

            #Itération sur les atomes de droite
            droite=site_changement+1
            if droite>len(positions_surface)-1:
                droite=droite-len(positions_surface)-1
            parite=((positions_surface[droite][1]-1)+droite)%2
            if parite==0:
                sitedroite='Na'
            else :
                sitedroite='Cl'
            nb_while=0
            while sitedroite==atome:
                nb_while+=1
                droite+=1
                if droite >= len(positions_surface):
                    droite -= len(positions_surface)
                parite=((positions_surface[droite][1]-1)+droite)%2
                if parite==0:
                    sitedroite='Na'
                else :
                    sitedroite='Cl'
                if nb_while>len(config):
                    tousmeme=True
                    break
            if droite>site_changement:
                if tousmeme:
                    continue
                proximite_droite=droite-site_changement
            else :
                if tousmeme:
                    continue
                proximite_droite=droite+(len(positions_surface)-site_changement)
            

            #Itération sur les atomes de gauche
            
            gauche=site_changement-1
            parite=((positions_surface[gauche][1]-1)+gauche)%2
            if parite==0:
                sitegauche='Na'
            else :
                sitegauche='Cl'

            nb_while=0
            while sitegauche==atome:
                nb_while+=1
                gauche-=1
                parite=((positions_surface[gauche][1]-1)+gauche)%2
                if parite==0:
                    sitegauche='Na'
                else :
                    sitegauche='Cl'
                if nb_while>len(config):
                    tousmeme=True
                    break
                if tousmeme:
                    continue
            proximite_gauche=site_changement-gauche


            if proximite_droite<proximite_gauche:
                #ON A ALORS DIFFUSION À DROITE
                print(f"{iteration}  Diffusion à droite du site {site_changement} vers le site {droite}")
                config[site_changement][positions_surface[site_changement][1]-1]=None
                if atome=='Na':
                    config[droite][positions_surface[droite][1]]=1
                else:
                    config[droite][positions_surface[droite][1]]=0
                positions_surface[site_changement][1]-=1
                positions_surface[droite][1]+=1
            
            if proximite_gauche<proximite_droite:
                #ON A ALORS DIFFUSION À GAUCHE
                print(f"{iteration}  Diffusion à gauche du site {site_changement} vers le site {gauche}")
                config[site_changement][positions_surface[site_changement][1]-1]=None
                if atome=='Na':
                    config[gauche][positions_surface[gauche][1]]=1
                else :
                    config[gauche][positions_surface[gauche][1]]=0
                positions_surface[site_changement][1]-=1
                positions_surface[gauche][1]+=1

            if proximite_gauche==proximite_droite:
                #ON A ALORS DIFFUSION ÉQUIPROBABLE DE CHAQUE BORD
                rprimeprime=np.random.rand()
                if rprimeprime<=0.5:
                    #diffusion à droite
                    # print(f"{iteration}  Diffusion à droite du site {site_changement} vers le site {droite}")
                    config[site_changement][positions_surface[site_changement][1]-1]=None
                    if atome=='Na':
                        config[droite][positions_surface[droite][1]]=1
                    else : 
                        config[droite][positions_surface[droite][1]]=0
                    positions_surface[site_changement][1]-=1
                    positions_surface[droite][1]+=1

                if rprimeprime>0.5:
                    #diffusion à gauche
                    print(f"{iteration}  Diffusion à gauche du site {site_changement} vers le site {gauche}")
                    config[site_changement][positions_surface[site_changement][1]-1]=None
                    if atome=='Na':
                        config[gauche][positions_surface[gauche][1]]=1
                    else : 
                        config[gauche][positions_surface[gauche][1]]=0
                    positions_surface[site_changement][1]-=1
                    positions_surface[gauche][1]+=1
            

        # Cas désorption
        if evnt[1]==0:
            config[site_changement][positions_surface[site_changement][1]-1]=None
            positions_surface[site_changement][1]-=1
            
        
        # Cas adsorption
        if evnt[1]==1:
            if positions_surface[site_changement][1] == config.shape[1]-1:
                # print("La configuration a atteint le plafond")
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
            Gamma.append(Ng/(wa*deltatemps_reel))
        if rugosity:
            Rugosity.append(domain.fct_rugosite(positions_surface))
    

    if gamma:
        parametres.append(Gamma)
    if rugosity:
        parametres.append(Rugosity)

    


    return config, deltatemps_reel, parametres, positions_surface