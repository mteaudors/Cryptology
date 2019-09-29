
def extended_euclidean(a,b):
    if a==0:
        return 0,1
    elif b==0:
        return 1,0
    else:
        u,v = extended_euclidean(b % a, a)
        return (v - (b//a) * u, u)



def rsa_private_key(p,q,e):
    phi = (p-1)*(q-1)
    u,v = extended_euclidean(e , phi)
    return u%phi


p = 152004274830911
q = 114441141188494785806336036780098446852178985275832534772936751508802911207311163587447867989220834129452082478435394438089316337529231532372741691790355702911122737540871596267001637740517999491829156274331732425972560042261009456330900355061362740705986794833712825541765215326087187214236576863322856391572159503409257904393137062639526125095334414161681488393611481782233666552574029176822295772390683156579703401596695200058943747788897107170272078912647771872645116208520442541674032982252244084542893763572012658374492634830802735749880900802023622181479334021660219273092158222664733646069576657
e = 65537

d = rsa_private_key(p,q,e)
print("d : ",d)