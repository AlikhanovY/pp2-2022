import json

with open('sample.json') as file:
    data = json.load(file)
    print("""
Interface Status
================================================================================
DN                                                 Description           Speed    MTU  
-------------------------------------------------- --------------------  ------  ------
    """)
    imdata = data["imdata"]
    for thing in imdata:
        main =  thing["l1PhysIf"]
        attribute =   main["attributes"]
        dn = attribute["dn"]
        speed = attribute["speed"]
        mtu = attribute["mtu"]
        output = ""
        if(len(dn) == 42):
            output += dn + "                              " + speed + "   " + mtu
        else:
            output += dn + "                               " + speed + "   " + mtu
       
        print(output)