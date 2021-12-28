//
//  CalculateView.swift
//  SCI Recovery
//
//  Created by Tolga Saygi on 11/4/21.
//

import Alamofire
import SwiftyJSON
import SwiftUI
import MaterialDesignSymbol
import ExytePopupView

struct CalculateView: View {
    @State var apiController = APIController()
    @State var username: String = ""
    @State var isPrivate: Bool = true
    @State var predictionResult: String = ""
    @State var result: String = "" {
        didSet {
            showingAlert = true
        }
    }
    var ageOptions = ["0-14y", "15-29y", "30-44y", "45-59y", "60-74y", "75+y", "Unknown"]
    var sexOptions = ["Male", "Female", "Other"]
    var loiAdmissionOptions = ["C UNKNOWN", "C01", "C02", "C03", "C04", "C05", "C06", "C07", "C08",
    "T UNKNOWN", "T01", "T02", "T03", "T04", "T05", "T06", "T07", "T08", "T09", "T10", "T11", "T12",
    "L UNKNOWN", "L01", "L02", "L03", "L04", "L05"]
    var educationOptions = ["Less Than 9th Grade", "9th-11th Grade", "High School", "Associate Degree",
                            "Bachelors Degree", "Masters Degree", "Doctorate", "Other", "Unknown"]
    var diabetesOptions = ["False", "Medication Controlled", "Lifestyle Controlled", "Not Controlled",
                           "Unknown If Controlled", "Unknown"]
    var alcoholOptions = ["0", "1-2", "3-4", "5-6", "7-9", "10+", "Unknown"]
    var raceOptions = ["White", "Black", "Native American", "Asian", "Multiracial", "Unknown"]
    var maritalOptions = ["Never Married", "Married", "Divorced", "Separated", "Widowed", "Other",
                          "Living Unmarried With Partner", "Unknown"]
    var occupationOptions = ["Working", "Homemaker", "In Training", "In Workshop", "Retired",
                             "Student or Infant", "Unemployed", "Other", "Unknown"]
    var occupationCodeOptions = ["Managerial", "Specialty", "Technicians", "Sales",
                                 "Administrative Support", "Private Household", "Protective Service",
                                 "Service", "Farming, Forestry, Fishing", "Precision Craft and Repair",
                                 "Machinery and Inspection", "Transportation", "Cleaners and Labourers",
                                 "Military", "Not Applicable", "Unknown"]
    var anxietyOptions = ["False", "PTSD", "Panic Disorder", "General Anxiety", "Multiple", "Unknown"]
    var insuranceOptions = ["Private Insurance", "Medicare", "Medicaid", "Workers' Compensation", "VA",
                            "Other Government", "No Pay", "Private Funds", "Other", "Unknown"]
    var neurologicOptions = ["Incomplete Paraplegic", "Complete Paraplegic", "Minimal Deficit Paraplegic",
                             "Incomplete Tetraplegic", "Complete Tetraplegic", "Minimal Deficit Tetraplegic",
                             "Minimal Deficit Normal", "Unknown"]
    var asiaOptions = ["A", "B", "C", "D", "Unknown"]
    var consciousnessOptions = ["False", "<=30min", "31min-24hrs", "24hrs+", "Unknown"]
    var tbiOptions = ["Improbable", "Possible", "Mild", "Moderate", "Severe", "Unknown"]
    
    
    @State var defaultAge = ""
    @State var defaultSex = ""
    @State var defaultLoi = ""
    @State var defaultEducation = ""
    @State var isVeteran: Bool = false
    @State var hasDepression: Bool = false
    @State var defaultDiabetes = ""
    @State var defaultAlcohol = ""
    @State var defaultRace = ""
    @State var defaultMarital = ""
    @State var defaultOccupation = ""
    @State var defaultOccupationCode = ""
    @State var defaultAnxiety = ""
    @State var defaultInsurance = ""
    @State var defaultNeurologic = ""
    @State var defaultAsia = ""
    @State var defaultConsciousness = ""
    @State var lostMemory: Bool = false
    @State var defaultTbi = ""
    @State var showingAlert = false
    @State var showingDisclaimer = false
    @State var showingError = false
    
    init(){
        let navigationBarAppearance = UINavigationBarAppearance()
        navigationBarAppearance.backgroundColor = UIColor(red: 0.03, green: 0.35, blue: 0.36, alpha: 1.00)
        UIScrollView.appearance().backgroundColor = UIColor(red: 0.03, green: 0.35, blue: 0.36, alpha: 1.00)
    }
    
    var body: some View {
        NavigationView {
             Form {
                 HStack(alignment: .center, spacing: 5.0) {
                     CircleImage(image: Image(materialDesignIcon: .report48px, size: 60, color: .white), borderColor: Color(UIColor(red: 0.96, green: 0.59, blue: 0.19, alpha: 1.00)), shadowRadius: 5).padding()
                     Spacer()
                     Text("Calculation")
                         .bold()
                         .padding()
                         .font(.title)
                         .foregroundColor(.white)
                         .background(Color(UIColor(red: 0.96, green: 0.59, blue: 0.19, alpha: 1.00)))
                 }.listRowBackground(Color(UIColor(red: 0.03, green: 0.35, blue: 0.36, alpha: 1.00)))
                 
                 Section(header: Text("Personal Information").foregroundColor(.white)
                     .foregroundColor(.black)
                     .font(.system(size: 15))
                     .fontWeight(.bold)) {
                     Picker(selection: $defaultAge, label: Text("Age - Injury")) {
                         ForEach(ageOptions, id: \.self) { element in
                             Text(element.capitalized)
                         }
                     }
                     Picker(selection: $defaultSex, label: Text("Sex")) {
                         ForEach(sexOptions, id:\.self) { opt in
                             Text(opt)
                         }
                     }
                     Picker(selection: $defaultRace, label: Text("Race")) {
                         ForEach(raceOptions, id:\.self) { opt in
                             Text(opt)
                         }
                     }
                     Picker(selection: $defaultEducation, label: Text("Education - Injury")) {
                         ForEach(educationOptions, id:\.self) { opt in
                             Text(opt)
                         }
                     }
                     Picker(selection: $defaultMarital, label: Text("Marital Status - Injury")) {
                         ForEach(maritalOptions, id:\.self) { opt in
                             Text(opt)
                         }
                     }
                     Picker(selection: $defaultOccupation, label: Text("Occupation Status - Injury")) {
                         ForEach(occupationOptions, id:\.self) { opt in
                             Text(opt)
                         }
                     }
                     Picker(selection: $defaultOccupationCode, label: Text("Occupation Code - Injury")) {
                         ForEach(occupationCodeOptions, id:\.self) { opt in
                             Text(opt)
                         }
                     }
                     Picker(selection: $defaultInsurance, label: Text("Primary Insurance")) {
                         ForEach(insuranceOptions, id:\.self) { opt in
                             Text(opt)
                         }
                     }
                     Toggle(isOn: $isVeteran) {
                         Text("Is Veteran?")
                     }
                 }.font(.system(size: 15))
                 
                 Section(header: Text("History").foregroundColor(.white)
                            .foregroundColor(.black)
                            .font(.system(size: 15))
                            .fontWeight(.bold)) {
                     Toggle(isOn: $hasDepression) {
                         Text("Has depression?")
                     }
                     Picker(selection: $defaultDiabetes, label: Text("Has diabetes?")) {
                         ForEach(diabetesOptions, id:\.self) { opt in
                             Text(opt)
                         }
                     }
                     Picker(selection: $defaultAlcohol, label: Text("Daily alcohol")) {
                         ForEach(alcoholOptions, id:\.self) { opt in
                             Text(opt)
                         }
                     }
                     Picker(selection: $defaultAnxiety, label: Text("Anxiety")) {
                         ForEach(anxietyOptions, id:\.self) { opt in
                             Text(opt)
                         }
                     }
                 }.font(.system(size: 15))
                 
                 Section(header: Text("Admission").foregroundColor(.white)
                            .foregroundColor(.black)
                            .font(.system(size: 15))
                            .fontWeight(.bold)) {
                     Picker(selection: $defaultLoi, label: Text("Level of Injury")) {
                         ForEach(loiAdmissionOptions, id:\.self) { opt in
                             Text(opt)
                         }
                     }
                     Picker(selection: $defaultNeurologic, label: Text("Neurologic Category")) {
                         ForEach(neurologicOptions, id:\.self) { opt in
                             Text(opt)
                         }
                     }
                     Picker(selection: $defaultAsia, label: Text("ASIA")) {
                         ForEach(asiaOptions, id:\.self) { opt in
                             Text(opt)
                         }
                     }
                 }.font(.system(size: 15))
                 
                 Section(header: Text("Injury").foregroundColor(.white)
                            .foregroundColor(.black)
                            .font(.system(size: 15))
                            .fontWeight(.bold)) {
                     Picker(selection: $defaultConsciousness, label: Text("Loss of Consciousness")) {
                         ForEach(consciousnessOptions, id:\.self) { opt in
                             Text(opt)
                         }
                     }
                     Toggle(isOn: $lostMemory) {
                         Text("Loss of Memory?")
                     }
                     Picker(selection: $defaultTbi, label: Text("TBI Likelihood")) {
                         ForEach(tbiOptions, id:\.self) { opt in
                             Text(opt)
                         }
                     }
                 }.font(.system(size: 15))
                 
                 Section {
                     Button(action: {
                         let model = RequestModel(age: defaultAge, sex: defaultSex, loi: defaultLoi, education: defaultEducation, isVeteran: isVeteran ? "True" : "False", depression: hasDepression ? "True" : "False", diabetes: defaultDiabetes, dailyAlcohol: defaultAlcohol, lossOfCons: defaultConsciousness, lossOfMem: lostMemory ? "True" : "False", tbi: defaultTbi, race: defaultRace, marital: defaultMarital, occupStatus: defaultOccupation, occupCode: defaultOccupationCode, primaryInsurance: defaultInsurance, anxiety: defaultAnxiety, neuro: defaultNeurologic, asia: defaultAsia)
                         if (model.isReady()) {
                             print(model)
                             apiController.postData(model: model) { data in
                                 print(data)
                                 /*do {
                                     result = try data.get().prediction
                                 } catch {
                                     return
                                 }*/
                                 result = data.prediction
                                 predictionResult = "Prediction: " + result
                                 //showingAlert = true
                             }
                         } else {
                             showingError = true
                         }
                         /*var result = apiController.postData(model: model) != nil {
                             .alert("Result: " + result, isPresented: $showingAlert) {
                                         Button("OK", role: .cancel) { }
                                     }
                         }*/

                     }) {
                         Text("Estimate Your ASIA Classification at Discharge")
                     }
                 }
                 
                 HStack(alignment: .center, spacing: 5.0) {
                     Text(predictionResult)
                         .bold()
                         .padding()
                         .foregroundColor(Color(UIColor(red: 1.00, green: 0.95, blue: 0.36, alpha: 1.00)))
                         .hidden()
                 }.listRowBackground(Color(UIColor(red: 0.03, green: 0.35, blue: 0.36, alpha: 1.00)))
                 
                 HStack(alignment: .center, spacing: 5.0) {
                     Text("The predictions made here are part of an ongoing research project to improve diagnoses of SCIs. They are not to be taken as guarantees of any kind and patients are strongly encouraged to consult their attending physicians to discuss recovery goals.")
                         .padding()
                         .foregroundColor(Color(UIColor(red: 1.00, green: 0.95, blue: 0.36, alpha: 1.00)))
                 }.listRowBackground(Color(UIColor(red: 0.03, green: 0.35, blue: 0.36, alpha: 1.00)))
             }
             .navigationBarHidden(true)
             .navigationBarTitle(Text("Home"))
             .edgesIgnoringSafeArea([.top, .bottom])
             .popup(isPresented: $showingAlert, type: .`default`/* autohideIn: 2*/) {
                 createPopup(text: predictionResult, header: "Calculation Complete", buttonText: "Close")
             }
             .popup(isPresented: $showingError, type: .`default`/* autohideIn: 2*/) {
                 createPopup(text: "Please fill all fields", header: "Error", buttonText: "Close")
             }
             .popup(isPresented: $showingDisclaimer, type: .`default`, autohideIn: 15) {
                 createPopup(text: "This client application is created for informational purposes only. The predictions made here are part of an ongoing research project to improve diagnoses of SCIs. They are not to be taken as guarantees of any kind and patients are strongly encouraged to consult their attending physicians to discuss recovery goals.", header: "Warning", buttonText: "Dismiss")
             }
             .onAppear() {
                 showingDisclaimer = true
             }
         }
    }
    
    func createPopup(text: String, header: String, buttonText: String) -> some View {
        VStack(spacing: 10) {
            Image("okay")
                .resizable()
                .aspectRatio(contentMode: ContentMode.fit)
                .frame(width: 50, height: 50)

            Text(header)
                //.foregroundColor(.white)
                .foregroundColor(Color.black)
                .fontWeight(.bold)

            Text(text)
                .font(.system(size: 12))
                .foregroundColor(Color.black)
                .fontWeight(.bold)

            Spacer()

            Button(action: {
                //self.showingPopup = false
            }) {
                Text(buttonText)
                    .font(.system(size: 14))
                    .foregroundColor(.black)
                    .fontWeight(.bold)
            }
            .frame(width: 100, height: 40)
            .background(Color.white)
            .cornerRadius(20.0)
        }
        .padding(EdgeInsets(top: 70, leading: 20, bottom: 40, trailing: 20))
        .frame(width: 300, height: 400)
        .background(Color(red: 0.85, green: 0.8, blue: 0.95))
        .cornerRadius(10.0)
        .shadow(color: Color(.sRGBLinear, white: 0, opacity: 0.13), radius: 10.0)
    }
}
