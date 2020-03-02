# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data=pd.read_csv(path)
data.head()

loan_status=data["Loan_Status"].value_counts()
loan_status.plot.bar()

#Code starts here


# --------------
#Code starts here
print(data.head(2))



property_and_loan=data.groupby(["Property_Area","Loan_Status"]).size().unstack()
print(property_and_loan)
#property_and_loan=property_and_loan.size()

property_and_loan.plot(kind="bar",stacked=False,rot=45)
plt.xlabel('Property Area')
plt.ylabel('Loan Status')


# --------------
#Code starts here
print(data.head(2))



education_and_loan=data.groupby(["Education","Loan_Status"]).size().unstack()
education_and_loan.plot(kind="bar",rot=45)
plt.xlabel('Education Status')
plt.ylabel('Loan Status')


# --------------
#Code starts here
print(data.head(2))
graduate=data[data['Education']=="Graduate"]
not_graduate=data[data['Education']=="Not Graduate"]


graduate['LoanAmount'].plot(kind="density",label="Graduate")
not_graduate['LoanAmount'].plot(kind="density",label="Not Graduate")

#For automaticlly displaying legend
plt.legend()


plt.show()












#Code ends here

#For automatic legend display
plt.legend()


# --------------
#Code starts here
import matplotlib.pyplot as plt
import numpy as np
fig,(ax_1,ax_2,ax_3)=plt.subplots(nrows=3,ncols=1)
data.plot.scatter(x="ApplicantIncome",y="LoanAmount",ax=ax_1)
data.plot.scatter(x="CoapplicantIncome",y="LoanAmount",ax=ax_1)
data["TotalIncome"]=data["ApplicantIncome"]+ data["CoapplicantIncome"]
data.plot.scatter(x="TotalIncome",y="LoanAmount",ax=ax_3)
plt.show()


