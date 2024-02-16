'''
Chemical kinetics is the study of the rates of reactions
Rate Law: v = -d[A]/dt = k[A]  (rate constant k)
The number of molecules that must simutaneously interact is defined as MOLECULARITY
A -> P is first-order reaction/unimolecular reaction


A+B -> P+Q is bimolecular
In this case, Rate law is v = k[A][B] (second-order)

Assumption: E + S <-> ES
Ks: enzyme-substrate dissociation equilibrium
Ks = k-1(reverse rate)/k1(forward rate)
ES equilibrium is only slightly disturbed by ES -> E + P,it is assumed k1 >> k2

Briggs & Haldane models: Steady State assumption
ES formation rate: vf = k1([ETotal] - [ES])[S]
ES dissapearance: vd = k-1[ES] + k2[ES] = (k-1 + k2)[ES]

At steady-state: vf = vd
So, k1([ET] - [ES])[S] = (k-1 + k2)[ES]
The ratio of constants (k-1 + k2)/k1 is itself a constant and is defined as the
Michaelis constant, KM
KM = ([ET] - [ES])[S] / [ES]
a measure of the substrate concentration required for effective catalysis to occur
Low KM indicates a strong affinity

Conditions:
1. The reaction involves 1 substrate, only one substrate is varied
while others are held constant.
2. The reaction ES -> E + P is irreversible
3. [S]0 > [ET] and [ET] is held constant
4. All other variables are constant

IMPORTANT!!!!
1. ES = [ET][S] / KM + [S]
2. vp = k2[ES]
1 + 2. vp = k2[ET][S] / KM + [S]
3. Vmax = k2[ET]
4. v = Vmax[S] / KM + [S]
'''

def MichaelisMenten(ET=None, S=None, ES=None, KM=None, v=None, vp=None, vmax=None, k2=None):
    if all(i is not None for i in [ET, S, KM]):
        ES = ET * S / (KM + S)
    if all(i is not None for i in [k2, ES]):
        vp = k2 * ES
    if all(i is not None for i in [k2, ET]):
        vmax = k2 * ET
    if all(i is not None for i in [vmax, ET, S, KM]):
        vp = vmax * S / (KM + S)
    print(locals())


def EnzymeUnit():
    pass

Type = {
    "MM": MichaelisMenten,
    "EU" Enzymeunit
}