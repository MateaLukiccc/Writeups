import owiener

def mapping(str1):
    for i in str1:
        if i not in "AbEglOSBTZ":
            print(i)
    str1 = str1.replace("O", '0')
    str1 = str1.replace("l", '1')
    str1 = str1.replace("Z", '2')
    str1 = str1.replace("E", '3')
    str1 = str1.replace("A", '4')
    str1 = str1.replace("S", '5')
    str1 = str1.replace("b", '6')
    str1 = str1.replace("T", '7')
    str1 = str1.replace("B", '8')
    str1 = str1.replace("g", '9')
    return str1

N = "lObAbAbSBlZOOEBllOEbblTlOAbOlTSBATZBbOSAEZTZEAlSOggTggbTlEgBOgSllEEOEZZOSSAOlBlAgBBBBbbOOSSTOTEOllbZgElgbZSZbbSTTOEBZZSBBEEBTgESEgAAAlAOAEbTZBZZlOZSOgBAOBgOAZEZbOBZbETEOSBZSSElSSZlbBSgbTBOTBSBBSOZOAEBEBZEZASbOgZBblbblTSbBTObAElTSTOlSTlATESEEbSTBOlBlZOlAOETAZAgTBTSAEbETZOlElBEESObbTOOlgAZbbOTBOBEgAOBAbZBObBTg"
e = "lBlbSbTASTTSZTEASTTEBOOAEbEbOOOSBAgABTbZgSBAZAbBlBBEAZlBlEbSSSETAlSOlAgAOTbETAOTSZAZBSbOlOOZlZTETAOSSSlTZOElOOABSZBbZTSAZSlASTZlBBEbEbOEbSTAZAZgAgTlOTSEBEAlObEbbgZBlgOEBTBbbSZAZBBSSZBOTlTEAgBBSZETAbBgEBTATgOZBTllOOSSTlSSTOSSZSZAgSZATgbSOEOTgTTOAABSZEZBEAZBOOTTBSgSZTZbOTgZTTElSOATOAlbBZTBlOTgOSlETgTBOglgETbT"
c = "SOSBOEbgOZTZBEgZAOSTTSObbbbTOObETTbBAlOSBbABggTOBSObZBbbggggZZlbBblgEABlATBESZgASBbOZbASbAAOZSSgbAOZlEgTAlgblBTbBSTAEBgEOEbgSZgSlgBlBSZOObSlgAOSbbOOgEbllAAZgBATgEAZbBEBOAAbZTggbOEZSSBOOBZZbAAlTBgBOglTSSESOTbbSlTAZATEOZbgbgOBZBBBBTBTOSBgEZlOBTBSbgbTlZBbbOBbTSbBASBTlglSEAEgTOSOblAbEgBAbOlbOETAEZblSlEllgTTbbgb"

N = int(mapping(N))
e = int(mapping(e))
c = int(mapping(c))

d = owiener.attack(e, N)

M = pow(c, d, N)

print("Decrypted message: ", M)

print(bytes.fromhex(hex(M)[2:]))

