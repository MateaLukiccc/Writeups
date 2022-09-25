n = 73542616560647877565544036788738025202939381425158737721544398356851787401183516163221837013929559568993844046804187977705376289108065126883603562904941748653607836358267359664041064708762154474786168204628181667371305788303624396903323216279110685399145476916585122917284319282272004045859138239853037072761
e = 65537
ct = 2657054880167593054409755786316190176139048369036893368834913798649283717358246457720021168590230987384201961744917278479195838455294205306264398417522071058105245210332964380113841646083317786151272874874267948107036095666198197073147087762030842808562672646078089825632314457231611278451324232095496184838


#we are missing parts of p and q and only have
#p=A10^71+x10^30+B
#q=C10^71+y10^30+D

A = 108294440701045353595867242719660522374526250640690193563048263854806748525172379331
x = ?
B = 341078269246532299656864881223

C = 679098724593514422867704492870375465007225641192338424726642090768164214390632598250
y = ?
D = 39563231146143146482074105407

#so we use sage
'''
# Set up a univariate polynomial
P.<x> = PolynomialRing(Integers(n))
p = A*10**71 + x*10**30 + B
# Make it monic
p *= inverse_mod(10**30,n)
print(p)

psol = p.small_roots(X=10**41, beta=1/10)[0]
P = int(A*10**71 + psol*10**30 + B)

assert n % P == 0
Q = n//P

print('P =',P)
print('Q =',Q)

f = (P-1)*(Q-1)
d = inverse(e,f)

pt = pow(ct,d,n)
print(long_to_bytes(pt))

'''