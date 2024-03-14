import matplotlib.pyplot as plt
import random

cm1 = plt.cm.RdYlBu

# F represent Li flux (10^9 mol/yr)
# R represent Li isotopic composition  (‰)
# D represent isotope fractionation factor (‰)
# f represents the proportion (from 0-100) of Li sink
# h represent HT; AOC represent AOC; r represent river; sw represent seawater; sc represent Li "source"
Fh = 5.2
Rh = 6.3
f_AOC,F_r,R_sw,R_r,D_A= [],[],[],[],[]
D_MAAC = 5
D_AOC = 10

D_sink = D_MAAC - D_AOC

fig, axes = plt.subplots(3,1, figsize = (12,16),dpi = 300)
ax1 = axes[0]
ax2 = axes[1]
ax3 = axes[2]
for o in range(1000000):
        Fr = random.uniform(2,50)
        Rr = random.uniform(1.3,43)
        f_MAAC = random.uniform(50,95)
        
        Fsc = Fh + Fr
        Rsc = (Fh*Rh + Fr*Rr)/Fsc
    
        # Rsw = Rsc + D_MAAC*f_MAAC+D_AOC*(1-f_MAAC) can deive the follow formula
        Rsw = Rsc + D_sink*f_MAAC/100 + D_AOC 
      
        if (Rsw <= 16.9) and  (Rsw >= 8.8):
            f_AOC.append(100-f_MAAC)
            F_r.append(Fr)
            R_sw.append(Rsw)
            R_r.append(Rr)
            D_A.append(D_AOC)

c1=ax1.scatter(f_AOC,F_r,c=R_sw,vmin=8.8,vmax=16.9,cmap = cm1,s=0.5)
c2=ax2.scatter(f_AOC,R_r,c=R_sw,vmin=8.8,vmax=16.9,cmap = cm1,s=0.5)
c3=ax3.scatter(F_r,R_r,c=R_sw,vmin=8.8,vmax=16.9,cmap = cm1,s=0.5)
            
ax1.set_xlabel('f$_\mathregular{AOC}$(%)', fontsize = 'large', labelpad = 5)
ax1.set_ylabel('F$_\mathregular{Riv}$ x 10$^\mathregular{10}$ (mol/yr)', fontsize = 'large', labelpad = 5)
ax2.set_xlabel('f$_\mathregular{AOC}$(%)', fontsize = 'large', labelpad = 5)
ax2.set_ylabel('\u03B4$^\mathregular{7}$Li$_\mathregular{Riv}$ (\u2030)', fontsize = 'large', labelpad = 5)
ax3.set_xlabel('F$_\mathregular{Riv}$ x 10$^\mathregular{10}$ (mol/yr)', fontsize = 'large', labelpad = 5)
ax3.set_ylabel('\u03B4$^\mathregular{7}$Li$_\mathregular{Riv}$ (\u2030)', fontsize = 'large', labelpad = 5)

f = plt.colorbar(c1,ax=[ax1,ax2,ax3]) 
f.ax.set_title('\u03B4$^\mathregular{7}$Li$_\mathregular{SW}$ (\u2030)', fontsize = 'large') 
plt.figtext(0.15,0.885,'\u0394$^\mathregular{7}$Li$_\mathregular{SW-MAAC}$ (\u2030) = 5          \u0394$^\mathregular{7}$Li$_\mathregular{SW-AOC}$ (\u2030) = 10') 

plt.savefig(r'C:\Users\Fig.8.jpg',bbox_inches = 'tight' ,pad_inches = 0.2)


          
           

