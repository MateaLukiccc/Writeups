import base64
from calendar import c

m="diN1cHV7dXtwcnVzdHB0c3VwcCFwcnV0dHVwcnR0dXB1cHUjdHRwcnRwdHp0d3BydXB0c3VydHd0IXRxdHV1dHRwdHNwcnUjdCd1cnV3dXR0c3VwcHJ1c3RwdXB0dHRzcHV0dXBydCN0cHR3dXpwcnR1dXd0J3R1cHJ1dnRwdHB1c3AncHJ3dnR6dXB0dHR0cHJ0I3VwcHJ1d3QndHt1cHBydHV0cHBydXZ0cHBydCR0J3VydXpwcnR1dHBwcnR1dXd1cHBydXN0d3QndCN1dHRzdXZwcnR1dCd0JHV7dXBwJ3Byd3J0cHRzdXZ0d3QndHV0enV7dCd0dXV0dHB0c3R0cCFwcnQhdHB0enBydXN1cHR0dXB0d3R7dXBwcnQncHJ1cXV7dCd1dnEjcHJ1cXV7dCd1dnUgdXNxdnFzdXNxenVydXNxe3F6dXFxcnFydCRxcHFycXZ1cHF7cXpxcnFycXtxe3F6dXB1cnVxcXpxdnFwcXV1cHUm"

def b(m):
    return base64.b64decode(m)

def x(m):
    m=str(m)
    return ''.join(chr(ord(c)^0x42) for c in m)

print(x(b(m)))


#+unhexify and rot13





