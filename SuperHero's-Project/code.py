# --------------
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#path of the data file- path
data = pd.read_csv(path)

data.Gender.replace({'-':'Agender'})


#Code starts here 

gender_count = data.Gender.value_counts()
gender_count.plot(kind='hist')



# --------------
#Code starts here
alignment = data.Alignment.value_counts()

alignment.plot(label= "Character Alignment")


# --------------
#Code starts here

sc_df = data[['Strength','Combat']]
sc_covariance = sc_df.cov().Combat.Strength

sc_strength = sc_df.Strength.std()
sc_combat = sc_df.Combat.std()

sc_pearson = sc_covariance/(sc_combat*sc_strength)
####
ic_df = data[['Intelligence','Combat']]
ic_covariance = ic_df.cov().Intelligence.Combat

ic_intelligence = ic_df.Intelligence.std()
ic_combat = ic_df.Combat.std()

ic_pearson = ic_covariance/(ic_combat*ic_intelligence)



# --------------
#Code starts here
total_high = data.Total.quantile(0.99)

super_best = data[data.Total>total_high]
super_best_names = super_best.Name.tolist()

print(super_best_names)



# --------------
#Code starts here

import numpy as np
fig,(ax_1,ax_2,ax_3) = plt.subplots(3)

data.Intelligence.plot(ax=ax_1,title='Intelligence')
data.Speed.plot(ax=ax_2,title="Speed")
data.Power.plot(ax=ax_3,title='Power')



