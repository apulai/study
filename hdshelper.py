
import socket
# hoszt fájl betöltése

input_file=open('/tmp/hosztok.txt','r')
output_file=open('/tmp/hdshelper_kimenet.txt','w+')
error_file=open('/tmp/hdshelper_hibaslookup.txt',"w+")
csv_file=open('/tmp/hdshelper_cvsimporthoz.txt',"w+")

aptaredomain="aptare.company.intra"
domainlist=["",".hu",".com",".test.io",".mydomain.edu"]
tilto_lista=["rhel","dummy","al","ax","af","aa","cv"]
ervenytelen_hosztok=[]

hosts_name={}
hosts_ip={}

for line in input_file:
    # Beolvassuk a sort és felszeleteljük a _ mentén
    line=line.rstrip()
    words=line.split("_")

    # Minden szóhoz hozzá fogunk fűzni lehetséges domaineket és
    for word in words:
        # Ha csak szám van egy szóban, akkor az biztosan nem hosztnév
        if not word.isnumeric() and word not in tilto_lista:
            #Megpróbáljuk az előre megadott domaineket hozzáfűzni
            for domain in domainlist:
                probanev= word + domain
                # Ha olyasmi jönne ki, amit már néztünk de nem volt, azt nem nézzük újra
                if( probanev not in ervenytelen_hosztok):
                    try:
                        # Megprobáljuk a lookupot, ha sikerül ki is mentjük
                        print("\nLooking up {}".format(probanev), end='')
                        addr1 = socket.gethostbyname(probanev)
                        print("\n {} {} {}".format(addr1, line, probanev).rstrip())
                        print("{} \t{} {}".format(addr1, line, probanev).rstrip(), file=output_file)
                        print("{},{},{}".format(aptaredomain,probanev,line).rstrip(), file=csv_file)
                    except socket.gaierror:
                        # Nemsikerült a lookup, megjegyezzük
                        print(" -- ervenytelen hoszt: {}".format(probanev))
                        print("{} ".format(probanev), file=error_file)
                        ervenytelen_hosztok.append(probanev)
                        pass

output_file.close()
csv_file.close()
error_file.close()
input_file.close()
