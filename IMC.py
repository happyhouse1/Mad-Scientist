print("Indiquez votre poids en KiloGramme sous la forme 'xx.x':")
poids = float(input())

print("Indiquez votre taille en Mètre sous la forme x.xx:", )
taille = float(input())

imc=poids/taille**2

print("Votre IMC (Indice de Masse Corporel) est de",imc,".")

if imc<=18.5:
    print("Vous êtes en insuffisance pondérale (maigreur)") 
elif imc<= 25.0:
    print("Vous avez une corpulence normale")
elif imc<=30.0:
    print("Vous êtes en surpoids")
elif imc<=35:
    print("Vous êtes en obésité modérée")
elif imc<=40:
    print ("Vous êtes en obésité sévère")
else:
    print ("Vous êtes en obésité morbide ou massive")

