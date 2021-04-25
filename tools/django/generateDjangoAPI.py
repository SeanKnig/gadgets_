def generateViews(models):
    modelList = []
    modelDetail = []
    modelViewSet = []
    f = open("views.py", "a")
    for i in models:
        #List
        list1 = "class %sList(generics.ListAPIView):\n"%(i)
        list2 = "   queryset = %s.objects.all()\n"%(i) 
        list3 = "   serializer_class = %sSerializer\n"%(i)
        modelList.append("#%s Views\n"%(i))
        modelList.append(list1)
        modelList.append(list2)
        modelList.append(list3)
        
        #Detail
        detail1 = "class %sDetail(generics.RetrieveAPIView):\n"%(i)
        detail2 = "     queryset = %s.objects.all()\n"%(i) 
        detail3 = "     serializer_class = %sSerializer\n"%(i)
        detail4 = "     permission_classes = [permissions.IsAuthenticated]\n"
        modelDetail.append(detail1)
        modelDetail.append(detail2)
        modelDetail.append(detail3)
        modelDetail.append(detail4)
        #ViewSet
        view1 = "class %sViewSet(viewsets.ModelViewSet):\n"%(i)
        view2 = "   queryset = %s.objects.all().order_by('-date_joined')\n"%(i) 
        view3 = "   serializer_class = %sSerializer\n"%(i)
        view4 = "   permission_classes = [permissions.IsAuthenticated]\n"
        modelViewSet.append(view1)
        modelViewSet.append(view2)
        modelViewSet.append(view3)
        modelViewSet.append(view4)
        #Write
        f.write(listToString(modelDetail)+'\n')
        f.write(listToString(modelList)+'\n')
        f.write(listToString(modelViewSet)+'\n')

        modelList.clear()
        modelDetail.clear()
        modelViewSet.clear()

def generateModelsAndFields(models, fields):
    listoflists = []
    list = []
    for i in range(len(models)):
        listoflists.append((models[i], fields[i]))
    generateSerializer(listoflists)

def generateSerializer(models_and_fields):
    print("Test")
    serial = []
    f = open("serializers.py", "a")
    print(models_and_fields[0])
    for serializer in models_and_fields:
        line1 = "class %sSerializer(serializers.HyperlinkedModelSerializer):\n"%(serializer[0])
        line2 = "   class Meta:\n"
        line3 = "       model = %s\n"%(serializer[0])
        line4 = "       fields = %s\n"%(serializer[1])
        serial.append(line1)
        serial.append(line2)
        serial.append(line3)
        serial.append(line4)
        print(serial)
        f.write(listToString(serial)+ '\n')
        serial.clear()

def generateSerializerClassNames(models):
    for model in models:
        print(listToString(model)+'Serializer,')
        
def generateClassNames(models):
    for model in models:
        print(listToString(model)+',')

def listToString(x):
    str1 = "" 
    for ele in x: 
        str1 += ele  
    return str1 



models = ['InsuranceCarrier', 'Gender', 'Specialty', 'ResidencyType', 'Location', 'State', 'Clinic', 'ClinicTypes', 'Hospital', 'HospitalTypes', 'CertBoard', 'ProviderEducationHistory', 'ProviderFacility', 'ProviderStateLicensure', 'ProviderMalPractice', 'ProviderWorkHistory', 'ProviderInsuranceInformation', 'ProviderReference', 'DEAStateInfo', 'ProviderWorkLocation', 'Provider']
fields = [['id', 'carrier'], ['id', 'gender'], ['id', 'primaryspecialty', 'secondaryspecialty'], ['id', 'residency_type'], ['id', 'location_name'], ['id', 'state_name', 'state_abbr'], ['Clinic_Name', 'Street_Address', 'City', 'State', 'Zip', 'Voting_member', 'Date_Joined', 'Telephone', 'Fax_Number', 'External_Clinic_Id', 'Tax_ID', 'Billing_NPI', 'Billing_Address', 'Billing_City', 'Billing_State', 'NPI_Type', 'Hours', 'County', 'Rural_Health_Clinic', 'Clinic_Manager', 'Manager_Phone', 'Email', 'Medical_Director', 'Med_Dir_Phone', 'Credentialing', 'Cred_phone', 'Cred_email', 'Quality', 'Remarks', 'Quality_phone', 'MainSatellite', 'Satellite_2', 'Clinic_Type', 'Provider1', 'Provider2', 'Provider3', 'Provider5', 'Provider4', 'Provider6', 'Provider7', 'Provider8', 'Provider9', 'Provider10', 'Provider11', 'Provider12', 'Provider13', 'Provider14', 'Provider15', 'Provider16', 'Provider17', 'Quality_email', 'Clinic_CCN', 'InsuranceBroker'], ['id', 'clinic_type'], ['id', 'Legal_Name', 'Joined', 'Address', 'City', 'Administrator', 'Zip', 'State', 'County', 'Tax_ID', 'Billing_Address', 'Billing_NPI', 'NPI_Type', 'Email', 'Phone_number', 'Quality_Email', 'Quality', 'CFO', 'Medical_Director', 'Compliance', 'Credentialing', 'CMS_Designation', 'Beds', 'Acute', 'Part_B', 'HomeCare', 'SkilledNursing', 'Medicare_CCN', 'Swing_bed_CCN', 'SNF_CCN', 'Home_Health_CCN', 'Hospice', 'Note', 'SNF_bill', 'Lic_Hosp_Bed', 'InsuranceBroker', 'Clinic1_Medicare_number', 'Clinic2_Medicare_number'], ['id', 'hospital_type'], ['certification_board', 'board_specialty', 'certification_date', 'certification_expire'], ['medicalEducation', 'medicalDegree', 'medicalDegreeStartDate', 'medicalDegreeEndDate', 'medicalEduation2', 'internEducation', 'internType', 'internStartDate', 'internEndDate', 'residentEducation', 'residentType', 'residentStart', 'residentEnd', 'remarks'], ['facility_clinic', 'facility_hospital', 'is_primary', 'start_date', 'end_date'], ['licensure_state', 'licensure_num', 'licensure_issue_date', 'licensure_end_date'], ['complaints', 'collaborative', 'malpractice', 'settlement', 'settlement_remarks', 'date'], ['past_start_date0', 'past_end_date0', 'past_employment_location0', 'past_start_date1', 'past_end_date1', 'past_employment_location1', 'past_start_date2', 'past_end_date2', 'past_employment_location2', 'past_start_date3', 'past_end_date3', 'past_employment_location3', 'past_start_date4', 'past_end_date4', 'past_employment_location4', 'past_start_date5', 'past_end_date5', 'past_employment_location5', 'past_start_date6', 'past_end_date6', 'past_employment_location6', 'past_start_date7', 'past_end_date7', 'past_employment_location7', 'past_start_date8', 'past_end_date8', 'past_employment_location8', 'past_start_date9', 'past_end_date9', 'past_employment_locatio9', 'past_start_date10', 'past_end_date10', 'past_employment_location10', 'past_start_date11', 'past_end_date11', 'past_employment_location11', 'past_start_date12', 'past_end_date12', 'past_employment_location12', 'past_start_date13', 'past_end_date13', 'past_employment_location13', 'past_start_date14', 'past_end_date14', 'past_employment_location14', 'past_start_date15', 'past_end_date15', 'past_employment_location15', 'past_start_date16', 'past_end_date16', 'past_employment_location16', 'past_start_date17', 'past_end_date17', 'past_employment_location17', 'past_start_date18', 'past_end_date18', 'past_employment_location18', 'past_start_date19', 'past_end_date19', 'past_employment_location19'], ['insurance_carrier', 'policy_number', 'expiration_date', 'amt_coverage'], ['remarks1', 'ref1', 'remarks2', 'ref2', 'remarks3','ref3'], ['dea_state', 'dea_expiration'], ['primary_facility', 'parentfacilityC', 'parentfacilityH', 'facilityaddress', 'facilitycity', 'facilitystate', 'facilityzip'], ['Lastname', 'Firstname', 'Middle', 'Degree', 'Specialty', 'MRHC_Initial', 'MRHC_Last', 'MRHC_Current', 'MRHC_Next', 'PCPSCP', 'npinumber', 'socialsecurity', 'gender', 'birthdate', 'birthplace', 'citizenship', 'upinnumber', 'medicaid', 'medicare', 'medicaresanctions', 'homeaddress', 'homecity', 'homestate', 'homezip', 'homephone', 'tinnumber', 'cred_for_clinic', 'cred_for_hospital', 'startdate', 'contactfirstname', 'contactlastname', 'contactphone', 'contactfax', 'contactemail', 'certboard', 'deainfo', 'insuranceInfo', 'ProviderReference', 'educationHistory', 'Sec_Lang_Spoken', 'Languages', 'RWHC_Status', 'EPLS', 'NPDB', 'ProviderMalPractice', 'ProviderWorkHistory', 'Voting', 'Opt_out', 'Quality_concern', 'NPI_Lookup', 'FTC_DecisionConsent', 'FTC_Cert_Mail_Rcpt', 'Clinics', 'Hospitals']]
#generateModelsAndFields(models, fields)
#generateViews(models)
generateSerializerClassNames(models)
#generateClassNames(models)