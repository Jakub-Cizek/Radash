import numpy as np
import matplotlib.pyplot as plt

class Material:
    def __init__(self,name,composition_element,composition_concentration,**kwargs):
        self.name=name
        self.composition_element=composition_element
        self.composition_concentration=composition_concentration
        self.number_composition_element=np.size(composition_element)
        self.composition_Z=np.zeros(self.number_composition_element,dtype=int)
        self.composition_units='a'
        
        #renormalization of concentrations
        sum=0
        for i in range(self.number_composition_element):
          sum=sum+self.composition_concentration[i]
        for i in range(self.number_composition_element):
          self.composition_concentration[i]=self.composition_concentration[i]/sum  
        for i in range(self.number_composition_element):
          if self.composition_element[i]=='H':
            self.composition_Z[i]=1  
          if self.composition_element[i]=='He':
            self.composition_Z[i]=2
          if self.composition_element[i]=='Li':
            self.composition_Z[i]=3
          if self.composition_element[i]=='Be':
            self.composition_Z[i]=4
          if self.composition_element[i]=='B':
            self.composition_Z[i]=5
          if self.composition_element[i]=='C':
            self.composition_Z[i]=6
          if self.composition_element[i]=='N':
            self.composition_Z[i]=7        
          if self.composition_element[i]=='O':
            self.composition_Z[i]=8  
          if self.composition_element[i]=='F':
            self.composition_Z[i]=9
          if self.composition_element[i]=='Ne':
            self.composition_Z[i]=10
          if self.composition_element[i]=='Na':
            self.composition_Z[i]=11
          if self.composition_element[i]=='Mg':
            self.composition_Z[i]=12
          if self.composition_element[i]=='Al':
            self.composition_Z[i]=13
          if self.composition_element[i]=='Si':
            self.composition_Z[i]=14
          if self.composition_element[i]=='P':
            self.composition_Z[i]=15  
          if self.composition_element[i]=='S':
            self.composition_Z[i]=16
          if self.composition_element[i]=='Cl':
            self.composition_Z[i]=17
          if self.composition_element[i]=='Ar':
            self.composition_Z[i]=18
          if self.composition_element[i]=='K':
            self.composition_Z[i]=19
          if self.composition_element[i]=='Ca':
            self.composition_Z[i]=20
          if self.composition_element[i]=='Sc':
            self.composition_Z[i]=21        
          if self.composition_element[i]=='Ti':
            self.composition_Z[i]=22  
          if self.composition_element[i]=='V':
            self.composition_Z[i]=23
          if self.composition_element[i]=='Cr':
            self.composition_Z[i]=24
          if self.composition_element[i]=='Mn':
            self.composition_Z[i]=25
          if self.composition_element[i]=='Fe':
            self.composition_Z[i]=26
          if self.composition_element[i]=='Co':
            self.composition_Z[i]=27
          if self.composition_element[i]=='Ni':
            self.composition_Z[i]=28
          if self.composition_element[i]=='Cu':
            self.composition_Z[i]=29 
          if self.composition_element[i]=='Zn':
            self.composition_Z[i]=30 
          if self.composition_element[i]=='Ga':
            self.composition_Z[i]=31
          if self.composition_element[i]=='Ge':
            self.composition_Z[i]=32 
          if self.composition_element[i]=='As':
            self.composition_Z[i]=33
          if self.composition_element[i]=='Se':
            self.composition_Z[i]=34
          if self.composition_element[i]=='Br':
            self.composition_Z[i]=35
          if self.composition_element[i]=='Kr':
            self.composition_Z[i]=36
          if self.composition_element[i]=='Rb':
            self.composition_Z[i]=37
          if self.composition_element[i]=='Sr':
            self.composition_Z[i]=38
          if self.composition_element[i]=='Y':
            self.composition_Z[i]=39
          if self.composition_element[i]=='Zr':
            self.composition_Z[i]=40
          if self.composition_element[i]=='Nb':
            self.composition_Z[i]=41 
          if self.composition_element[i]=='Mo':
            self.composition_Z[i]=42
          if self.composition_element[i]=='Tc':
            self.composition_Z[i]=43
          if self.composition_element[i]=='Ru':
            self.composition_Z[i]=44        
          if self.composition_element[i]=='Rh':
            self.composition_Z[i]=45  
          if self.composition_element[i]=='Pd':
            self.composition_Z[i]=46
          if self.composition_element[i]=='Ag':
            self.composition_Z[i]=47
          if self.composition_element[i]=='Cd':
            self.composition_Z[i]=48
          if self.composition_element[i]=='In':
            self.composition_Z[i]=49
          if self.composition_element[i]=='Sn':
            self.composition_Z[i]=50
          if self.composition_element[i]=='Sb':
            self.composition_Z[i]=51
          if self.composition_element[i]=='Te':
            self.composition_Z[i]=52  
          if self.composition_element[i]=='I':
            self.composition_Z[i]=53
          if self.composition_element[i]=='Xe':
            self.composition_Z[i]=54
          if self.composition_element[i]=='Cs':
            self.composition_Z[i]=55
          if self.composition_element[i]=='Ba':
            self.composition_Z[i]=56
          if self.composition_element[i]=='La':
            self.composition_Z[i]=57
          if self.composition_element[i]=='Ce':
            self.composition_Z[i]=58        
          if self.composition_element[i]=='Pr':
            self.composition_Z[i]=59  
          if self.composition_element[i]=='Nd':
            self.composition_Z[i]=60
          if self.composition_element[i]=='Pm':
            self.composition_Z[i]=61
          if self.composition_element[i]=='Sm':
            self.composition_Z[i]=62
          if self.composition_element[i]=='Eu':
            self.composition_Z[i]=63
          if self.composition_element[i]=='Gd':
            self.composition_Z[i]=64
          if self.composition_element[i]=='Tb':
            self.composition_Z[i]=65
          if self.composition_element[i]=='Dy':
            self.composition_Z[i]=66 
          if self.composition_element[i]=='Ho':
            self.composition_Z[i]=67 
          if self.composition_element[i]=='Er':
            self.composition_Z[i]=68
          if self.composition_element[i]=='Tm':
            self.composition_Z[i]=69 
          if self.composition_element[i]=='Yb':
            self.composition_Z[i]=70
          if self.composition_element[i]=='Lu':
            self.composition_Z[i]=71
          if self.composition_element[i]=='Hf':
            self.composition_Z[i]=72
          if self.composition_element[i]=='Ta':
            self.composition_Z[i]=73
          if self.composition_element[i]=='W':
            self.composition_Z[i]=74
          if self.composition_element[i]=='Re':
            self.composition_Z[i]=75
          if self.composition_element[i]=='Os':
            self.composition_Z[i]=76
          if self.composition_element[i]=='Ir':
            self.composition_Z[i]=77
          if self.composition_element[i]=='Pt':
            self.composition_Z[i]=78
          if self.composition_element[i]=='Au':
            self.composition_Z[i]=79
          if self.composition_element[i]=='Hg':
            self.composition_Z[i]=80
          if self.composition_element[i]=='Tl':
            self.composition_Z[i]=81
          if self.composition_element[i]=='Pb':
            self.composition_Z[i]=82
          if self.composition_element[i]=='Bi':
            self.composition_Z[i]=83
          if self.composition_element[i]=='Po':
            self.composition_Z[i]=84
          if self.composition_element[i]=='At':
            self.composition_Z[i]=85
          if self.composition_element[i]=='Rn':
            self.composition_Z[i]=86
          if self.composition_element[i]=='Fr':
            self.composition_Z[i]=87 
          if self.composition_element[i]=='Ra':
            self.composition_Z[i]=88 
          if self.composition_element[i]=='Ac':
            self.composition_Z[i]=89
          if self.composition_element[i]=='Th':
            self.composition_Z[i]=90 
          if self.composition_element[i]=='Pa':
            self.composition_Z[i]=91
          if self.composition_element[i]=='U':
            self.composition_Z[i]=92
          if self.composition_element[i]=='Np':
            self.composition_Z[i]=93
          if self.composition_element[i]=='Pu':
            self.composition_Z[i]=94
          if self.composition_element[i]=='Am':
            self.composition_Z[i]=95
          if self.composition_element[i]=='Cm':
            self.composition_Z[i]=96
          if self.composition_element[i]=='Bk':
            self.composition_Z[i]=97
          if self.composition_element[i]=='Cf':
            self.composition_Z[i]=98
          if self.composition_element[i]=='Es':
            self.composition_Z[i]=99
          if self.composition_element[i]=='Fm':
            self.composition_Z[i]=100
          if self.composition_element[i]=='Md':
            self.composition_Z[i]=101
          if self.composition_element[i]=='No':
            self.composition_Z[i]=102
          if self.composition_element[i]=='Lr':
            self.composition_Z[i]=103
          if self.composition_element[i]=='Rf':
            self.composition_Z[i]=104
          if self.composition_element[i]=='Db':
            self.composition_Z[i]=105
          if self.composition_element[i]=='Sg':
            self.composition_Z[i]=106
          if self.composition_element[i]=='Bh':
            self.composition_Z[i]=107
          if self.composition_element[i]=='Hs':
            self.composition_Z[i]=108
          if self.composition_element[i]=='Mt':
            self.composition_Z[i]=109
          if self.composition_element[i]=='Ds':
            self.composition_Z[i]=110
          if self.composition_element[i]=='Rg':
            self.composition_Z[i]=111
          if self.composition_element[i]=='Cn':
            self.composition_Z[i]=112     
        for i in range(self.number_composition_element):
          if self.composition_Z[i]==0:
            print(f"error: unknown element symbol {self.composition_element[i]}")                    
        
        print(f"material: {self.name}")
        print(f"number of constituents: {self.number_composition_element}")
        for i in range(self.number_composition_element):
          print(f"{self.composition_element[i]:2s} {self.composition_Z[i]:2d} {self.composition_concentration[i]:6.3f}")
        if self.composition_units=='a':
          print(f"units: atomic")
        
    def __str__(self):
        return f"material: {self.name}"    

    #average Z number
    def get_Zeff(self):
        self.Zeff=0
        for i in range(self.number_composition_element):
          self.Zeff=self.Zeff+self.composition_Z[i]*self.composition_concentration[i]
        print(f"effective Z number: {self.Zeff:5.3f}")
        
    #average density    
    def get_density(self):
         data_density=np.loadtxt("density.txt")
         number_data_density=np.size(data_density[:,0])
         self.composition_density=np.zeros(self.number_composition_element)
         for i in range(self.number_composition_element):
          for j in range(number_data_density):
            if self.composition_Z[i]==data_density[j,0]:
              self.composition_density[i]=data_density[j,1]
         for i in range(self.number_composition_element):
          if self.composition_density[i]==0:
            print(f"error: no data for density of element {self.composition_element[i]}")     
         self.density=0     
         for i in range(self.number_composition_element):
          print(f"{self.composition_element[i]:2s} {self.composition_density[i]:6.3f} g/cm3")
          self.density=self.density+self.composition_density[i]*self.composition_concentration[i]
         print(f"composition weighted mean density: {self.density:5.3f} g/cm3")
         
         
    #atomic misfit parameter
    def get_delta(self):
         data_radius=np.loadtxt('atomic_radius.txt')
         number_data_radius=np.size(data_radius[:,0])
         self.composition_radius=np.zeros(self.number_composition_element)
                 
         for i in range(self.number_composition_element):
          for j in range(number_data_radius):
            if self.composition_Z[i]==data_radius[j,0]:
              self.composition_radius[i]=data_radius[j,1]
         for i in range(self.number_composition_element):
          if self.composition_radius[i]==0:
            print(f"error: no data for atomic radius of element {self.composition_element[i]}")     
         self.mean_radius=0     
         for i in range(self.number_composition_element):
          print(f"{self.composition_element[i]:2s} {self.composition_radius[i]:6.3f} A")
          self.mean_radius=self.mean_radius+self.composition_radius[i]*self.composition_concentration[i]
         print(f"composition weighted mean atomic radius: {self.mean_radius:5.3f} A")
         
         self.delta=0
         for i in range(self.number_composition_element):
          self.delta=self.delta+self.composition_concentration[i]*(1-self.composition_radius[i]/self.mean_radius)**2
         self.delta=np.sqrt(self.delta)*100
         print(f"atomic misfit parameter: {self.delta:5.3f} %")       
         
    #configurational entropy    
    def get_entropy(self):
         self.entropy=0
         for i in range(self.number_composition_element):
          self.entropy=self.entropy-self.composition_concentration[i]*np.log(self.composition_concentration[i])
         print(f"configurational entropy: {self.entropy:5.3f} k")     
    
    #VEC
    def get_VEC(self):
         data_VEC=np.loadtxt("VEC.txt")
         number_data_VEC=np.size(data_VEC[:,0])
         self.composition_VEC=np.zeros(self.number_composition_element)
         for i in range(self.number_composition_element):
          for j in range(number_data_VEC):
            if self.composition_Z[i]==data_VEC[j,0]:
              self.composition_VEC[i]=data_VEC[j,1]
         for i in range(self.number_composition_element):
          if self.composition_VEC[i]==0:
            print(f"error: no data for VEC of element {self.composition_element[i]}")     
         self.VEC=0     
         for i in range(self.number_composition_element):
          print(f"{self.composition_element[i]:2s} {self.composition_VEC[i]:5.3f} g/cm3")
          self.VEC=self.VEC+self.composition_VEC[i]*self.composition_concentration[i]
         print(f"composition weighted VEC: {self.VEC:5.3f} g/cm3")
         
    #thermal neutron cross section
    def get_neutron_cross_section(self):
         data_neutron_cross_section=np.loadtxt("neutron_cross_section.txt")
         number_data_neutron_cross_section=np.size(data_neutron_cross_section[:,0])
         self.composition_neutron_cross_section=np.zeros(self.number_composition_element)
         for i in range(self.number_composition_element):
          for j in range(number_data_neutron_cross_section):
            if self.composition_Z[i]==data_neutron_cross_section[j,0]:
              self.composition_neutron_cross_section[i]=data_neutron_cross_section[j,1]
         for i in range(self.number_composition_element):
          if self.composition_neutron_cross_section[i]==0:
            print(f"error: no data for neutron cross-section of element {self.composition_element[i]}")     
         self.neutron_cross_section=0     
         for i in range(self.number_composition_element):
          print(f"{self.composition_element[i]:2s} {self.composition_neutron_cross_section[i]:6.3f} barn")
          self.neutron_cross_section=self.neutron_cross_section+self.composition_neutron_cross_section[i]*self.composition_concentration[i]
         print(f"composition weighted neutron cross-section: {self.neutron_cross_section:5.3f} barn")     