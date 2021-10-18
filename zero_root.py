import matplotlib.pyplot as plt
import numpy as np
from   ROOT import * 


def findZero(f1,emin,emax,tol):
    emed = (emin+emax)/2
    while (emax-emin>tol):
        fmed = f1(emed);
        fmin = f1(emin)
        if (fmin*fmed<=0):
            emax = emed
        else:
            emin = emed
        emed=(emin+emax)/2
    return emed


f = TF1("f","x^3-1",0,2,1)
x = findZero(f,0.,2.,0.001)
print(x)
f.Draw()

gr = TGraph()
gr.SetPoint(0,x,f(x))
gr.SetMarkerStyle(20)
gr.Draw("P")

gApplication.Run(True)

