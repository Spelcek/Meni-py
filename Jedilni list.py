meni = {}
print "Dnevni meni Juhcokuh:"

while True:
    jed=raw_input("Vnesi jed v meni:")
    print "Izbrali ste " + jed

    if jed == "ne":
        print"Dnevni Meni:."
        break

    cenik = str(raw_input("Vnesi ceno v eur:"))
    meni [jed]= cenik
    print "Cena je:" + str(cenik)

for key, value in meni.iteritems():
    print "%s:%s" % (key, value)
    print "*********"

meni_file = open("meni.txt", "w+")
meni_file.write("dnevni meni\n")
meni_file.write("tedenski meni\n")
meni_file.close()









