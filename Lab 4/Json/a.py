import json 
with open('sample.json') as file:
    data=json.load(file)
    print("""                           
Interface status
========================================================================================
DN                                                 Description              Speed     MTU  
-----------------------------------------------    ------------------     --------  -------
 """)
    imdata = data["imdata"]
    for thing in imdata:
        main = thing["l1PhysIf"]
        attribute = main["attributes"]
        dn = attribute["dn"]
        speed = attribute["speed"]
        mtu = attribute["mtu"]
        p = ""
        p+= dn + "                               " + speed + "     " + mtu
        print(p)
