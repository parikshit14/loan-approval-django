from django.shortcuts import render
from django.http import HttpResponse
#import sklearn.external.joblib as extjoblib
import joblib
import pandas as pd
# Create your views here.
reloadmodel=joblib.load('models/loan_approvals.pkl')
def index(request):
    temp={}
    temp['loan_type']=2
    temp['property_type']=1
    temp['loan_purpose']=3
    temp['occupancy']=1
    temp['loan_amount']=113
    temp['preapproval']=3
    temp['msa_md']=356
    temp['state_code']=5
    temp['county_code']=98
    temp['applicant_ethnicity']=3
    temp['applicant_race']=5
    temp['applicant_sex']=1
    temp['applicant_income']=471 
    temp['population']=3256
    temp['minority_population_pct']=24.824
    temp['ffiecmedian_family_income']=52771.0
    temp['tract_to_msa_md_income_pct']=100.000
    temp['number_of_owner_occupied_units']=800.0
    temp['number_of_1_to_4_family_units']=1013.0
    temp['lender']=5684
    temp['co_applicant']=True
    context={'temp':temp}
    return render(request,'index.html',context)

def loan_approval(request):
    
    if request.method == 'POST':
        temp={}
        temp['loan_type']=request.POST.get('loan_typeVal')
        temp['property_type']=request.POST.get('property_typeVal')
        temp['loan_purpose']=request.POST.get('loan_purposeVal')
        temp['occupancy']=request.POST.get('occupancyVal')
        temp['loan_amount']=request.POST.get('loan_amountVal')
        temp['preapproval']=request.POST.get('preapprovalVal')
        temp['msa_md']=request.POST.get('msa_mdVal')
        temp['state_code']=request.POST.get('state_codeVal')
        temp['county_code']=request.POST.get('county_codeVal')
        temp['applicant_ethnicity']=request.POST.get('applicant_ethnicityVal')
        temp['applicant_race']=request.POST.get('applicant_raceVal')
        temp['applicant_sex']=request.POST.get('applicant_sexVal')
        temp['applicant_income']=request.POST.get('applicant_incomeVal')
        temp['population']=request.POST.get('populationVal')
        temp['minority_population_pct']=request.POST.get('minority_population_pctVal')
        temp['ffiecmedian_family_income']=request.POST.get('ffiecmedian_family_incomeVal')
        temp['tract_to_msa_md_income_pct']=request.POST.get('tract_to_msa_md_income_pctVal')
        temp['number_of_owner_occupied_units']=request.POST.get('number_of_owner_occupied_unitsVal')
        temp['number_of_1_to_4_family_units']=request.POST.get('number_of_1_to_4_family_unitsVal')
        temp['lender']=request.POST.get('lenderVal')
        temp['co_applicant']=bool(request.POST.get('co_applicantVal'))
    testData=pd.DataFrame({'x':temp}).transpose()
    scoreval=reloadmodel.predict(testData)[0]
    context={'scoreval':scoreval, 'temp':temp}
    return render(request,'index.html',context)