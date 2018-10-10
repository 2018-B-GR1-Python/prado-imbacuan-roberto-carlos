if True:
    print "Es verdad"
else:
    print "No es verdad"

if False:
    print "Es verdad"
else:
    print "No es verdad"

if 1.2:  # Truthy
    print "Si"  # Truthy
else:
    print "No"
nombre = "Roberto"

if 0:  # Falsy
    print "Si"
else:
    print "No"

if None:  # Falsy
    print "Si"
else:
    print "No"

if 1 != 1:  # Falsy
    print "Si"
else:
    print "No"

if not None:
    print "Si"
else:
    print "No"
if -1:
    print "Si"
else:
    print "No"


if 1 or not 0:
    print "Si"
else :
    print "No"

if 1 and not 0:
    print "Si"
else:
    print "No"


if "a,b".split(","):
    print "Si"
else:
    print "No"

diccionario = {}

if diccionario:
    print "Si"
else:
    print "No"

array = []
if array:
    print "Si"
else:
    print "No"

# False, None, 0, dicc, arreg: Falsy