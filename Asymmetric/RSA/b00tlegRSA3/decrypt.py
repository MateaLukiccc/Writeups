#Multy-prime RSa
c= 19385504861532072629301479019672718482335135713423399947303287055496560051986885951549664842511804438835444600713396184370536644477856317836547182933555496233846763881714982598038427647667257071851065535519440914581990369184075380972727586283714850419378397525131147275313297571937307203851907995241916111275164783595102454955023360442231637239
n= 30754490349458604626630507886468516939981244806769890037754213309038675463546104307379144622642175348609112100564322285860561264917473604880800295870895158540251307322557556433350483480130923056318372607997373092165489233301624422029578537683312629967416579176094515759188710823304749732362657662713620485447180083810958392344220324305349152853
e= 65537

#we can calculate totient with https://www.alpertron.com.ar/ECM.HTM
#phi(n) = phi(p*q*r*s*t*u*v) = phi(p) * phi(q) *phi(r) * phi(s) * phi(t) * phi(u) * phi(v) = (p-1)(q-1)(r-1)(s-1)(t-1)(u-1)(v-1)
phi=30754490265731493120575132475055889646879865936476450409876293332203665478863216496534456278342325779904097363586360738352658462657571522881080995953270539384699655439426030014002940254130549073364062890199399518206468761450956639662350174873034318769087639534088642232111027392263883594895821747939638606692347721233517178215464960000000000000

d=pow(e,-1,phi)

m=pow(c,d,n)
print(bytes.fromhex(hex(m)[2:]))

