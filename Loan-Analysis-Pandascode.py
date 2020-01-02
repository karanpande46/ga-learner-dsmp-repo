# --------------
# Import packages
import numpy as np
import pandas as pd
from scipy.stats import mode 
filepath =path
bank=pd.read_csv(filepath)
#print(bank)


# code starts here
categorical_var=bank.select_dtypes(include = 'object')
print("categorical_var",categorical_var)

numerical_var=bank.select_dtypes(include = 'number')
print("numerical_var",numerical_var)



# code ends here


# --------------
# code starts here


# print (bank['Loan_ID'] )
banks=bank.drop('Loan_ID',axis=1)

print(banks.head(10))
print( banks.isnull().sum() )

bank_mode=banks.mode()
print(bank_mode)
banks=banks.fillna(0)
print(banks)
#code ends here



# --------------
# Code starts here
print(banks.head(2))


import pandas as pd
avg_loan_amount=pd.pivot_table(banks, index=['Gender', 'Married', 'Self_Employed'],values='LoanAmount', aggfunc='mean')

print(avg_loan_amount)


# code ends here



# --------------
# code starts here
#loan_approved_se=df[banks]
#print(banks.head(2)).


loan_approved_se=banks[(banks.Self_Employed == "Yes") & (banks.Loan_Status == "Y")].count()
print("loan_approved_se",loan_approved_se)
loan_approved_nse=banks[(banks.Self_Employed == "No") & (banks.Loan_Status == "Y")].count()
print(loan_approved_nse)
percentage_se=(56/614) *100
percentage_nse=(366/614) *100
# code ends here


# --------------
# code starts here
print(banks.head(2))
loan_term=banks['Loan_Amount_Term'].apply(lambda x:x/12)
print(loan_term)
big_loan_term=len(loan_term[loan_term >=25])
print(big_loan_term)


# code ends here


# --------------
# code starts here




loan_groupby=banks.groupby("Loan_Status")["ApplicantIncome","Credit_History"]
print(loan_groupby)
mean_values=loan_groupby.mean()



# code ends here


