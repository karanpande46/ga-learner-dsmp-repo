# --------------
import pandas as pd
import scipy.stats as stats
import math
import numpy as np
import warnings

warnings.filterwarnings('ignore')
#Sample_Size
sample_size=2000

#Z_Critical Score
z_critical = stats.norm.ppf(q = 0.95)  


# path        [File location variable]
data=pd.read_csv(path)
data.head(5)
#Code starts here

data_sample=data.sample(n=sample_size,random_state=0)

sample_mean=data_sample["installment"].mean()
print(sample_mean)
sample_std=data_sample["installment"].std()
print(sample_std)

squareroot=np.sqrt(sample_size)
print(squareroot)
margin_of_error=z_critical * (sample_std/squareroot)
print(margin_of_error)

confidence_interval=(sample_mean-margin_of_error,sample_mean+margin_of_error)
print(confidence_interval)
true_mean=data["installment"].mean()
print(true_mean)


# --------------
import matplotlib.pyplot as plt
import numpy as np

#Different sample sizes to take
sample_size=np.array([20,50,100])

fig ,axes=plt.subplots(nrows = 3 , ncols = 1)

for i in range(len(sample_size)):
    m=[]
    for j in range(1000):
        m.append(data['installment'].sample(n=sample_size[i]).mean())
    mean_series=pd.Series(m)
    axes[i].hist(mean_series)
plt.show()
        





# --------------
#Importing header files

from statsmodels.stats.weightstats import ztest
print(data.head(2))

#Code starts here
#Calculationg interest and stripping the % and dividing by 100
data['int.rate']=data['int.rate'].str.strip('%').astype(float)/100

#finding z_statistic,p_value for small business interests rates
z_statistic,p_value=ztest(x1=data[data['purpose']=='small_business']['int.rate'] ,value = data['int.rate'].mean(),alternative='larger')

#checking for hypothesis testing
if(p_value<=0.05):print('We reject the null hypothesis therefore H_1: μ>12 % i.e small_business is higher than the average interest rate')
else:print('We accept the null hypothesis that is H_0 :μ= 12% There is no difference in interest rate being given to people with purpose a')


# --------------
#Importing header files
from statsmodels.stats.weightstats import ztest

#Code starts here
#Code starts here
#Calculationg interest and stripping the % and dividing by 100

#finding z_statistic,p_value for small business interests rates
z_statistic,p_value=ztest(x1=data[data['paid.back.loan']=='No']['installment'], x2 = data[data['paid.back.loan']=='Yes']['installment'])

#checking for hypothesis testing
if(p_value<=0.05):print('We reject the null hypothesis therefore H_1: μ>12 % i.e small_business is higher than the average interest rate')
else:print('We accept the null hypothesis that is H_0 :μ= 12% There is no difference in interest rate being given to people with purpose a')


# --------------
#Importing header files
from scipy.stats import chi2_contingency

#Critical value 
critical_value = stats.chi2.ppf(q = 0.95, # Find the critical value for 95% confidence*
                      df = 6)   # Df = number of variable categories(in purpose) - 1

#Code starts here
yes=data[data['paid.back.loan']=='Yes']['purpose'].value_counts()

no=data[data['paid.back.loan']=='No']['purpose'].value_counts()
print(yes,no)
observed=pd.concat([yes.transpose(),no.transpose()],axis=1,keys= ['Yes','No'])
print(observed)
chi2, p, dof , ex=chi2_contingency(observed)
print(chi2, p, dof , ex)

#if(chi2>=critical_value):
#print(chi2 'chi is greater than or equal to critical value',critical_value,'therefore reject the null hypothesis that the two distributions are the same')
#else:print(chi2 'chi is less than critical value',critical_value,'we acept null hypothesis and it cannot be rejected')


