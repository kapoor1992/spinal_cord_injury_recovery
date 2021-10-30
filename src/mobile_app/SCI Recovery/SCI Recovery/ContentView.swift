//
//  ContentView.swift
//  SCI Recovery
//
//  Created by Tolga Saygi on 10/25/21.
//

import SwiftUI
import MaterialDesignSymbol

struct ContentView: View {
    @State var apiController = APIController()
    
    init(){
        let navigationBarAppearance = UINavigationBarAppearance()
        navigationBarAppearance.backgroundColor = UIColor(red: 0.03, green: 0.35, blue: 0.36, alpha: 1.00)
        UIScrollView.appearance().backgroundColor = UIColor(red: 0.03, green: 0.35, blue: 0.36, alpha: 1.00)
    }
    
    var body: some View {
        ScrollView(.vertical, showsIndicators: false) {
            VStack(alignment: .leading, spacing: 10){
                HStack(alignment: .center, spacing: 5.0) {
                    Spacer()
                    Text("Spinal Cord Injury")
                        .font(.title)
                        .foregroundColor(.white)
                        .bold()
                        .padding()
                    Spacer()
                }.background(Color(UIColor(red: 0.20, green: 0.20, blue: 0.20, alpha: 1.00)))
                HStack(alignment: .center, spacing: 5.0) {
                    CircleImage(image: Image(materialDesignIcon: .timeToLeave48px, size: 60, color: .white), borderColor: Color(UIColor(red: 0.96, green: 0.59, blue: 0.19, alpha: 1.00)), shadowRadius: 5).padding()
                    Spacer()
                    Text("SCI Prevention")
                        .bold()
                        .padding()
                        .font(.title)
                        .foregroundColor(.white)
                        .background(Color(UIColor(red: 0.96, green: 0.59, blue: 0.19, alpha: 1.00)))
                        .padding()
                }
                HStack(alignment: .center, spacing: 5.0) {
                    Text("About 90% of SCI cases are caused by preventable injuries, whereas only 10% are due to unavoidable causes such as neurodegeneration and cancer.")
                        .font(.subheadline)
                        .foregroundColor(Color(UIColor(red: 1.00, green: 0.95, blue: 0.36, alpha: 1.00)))
                        .padding()
                }
                HStack(alignment: .center, spacing: 5.0) {
                    Text("Among preventable SCI cases, the leading sources are car crashes, accidental falls, and firearm injuries.")
                        .font(.subheadline)
                        .foregroundColor(Color(UIColor(red: 1.00, green: 0.95, blue: 0.36, alpha: 1.00)))
                        .padding()
                }
                HStack(alignment: .center, spacing: 5.0) {
                    Text("Currently, participant education and environmental safety training are the primary avenues for promoting behaviors that prevent SCI.")
                        .font(.subheadline)
                        .foregroundColor(Color(UIColor(red: 1.00, green: 0.95, blue: 0.36, alpha: 1.00)))
                        .padding()
                }
                Group{
                }
                //Spacer()
            }
            VStack(alignment: .leading, spacing: 10){
                HStack(alignment: .center, spacing: 5.0) {
                    Text("SCI Treatment")
                        .bold()
                        .padding()
                        .font(.title)
                        .foregroundColor(.white)
                        .background(Color(UIColor(red: 0.96, green: 0.59, blue: 0.19, alpha: 1.00)))
                        .padding()
                    Spacer()
                    CircleImage(image: Image(materialDesignIcon: .accessibility48px, size: 60, color: .white), borderColor: Color(UIColor(red: 0.96, green: 0.59, blue: 0.19, alpha: 1.00)), shadowRadius: 5).padding()
                }
                HStack(alignment: .center, spacing: 5.0) {
                    Text("The treatment phases of SCI patients divide into the acute phase during the first three months following injury, then the sub-acute phase during the subsequent three months, and finally the chronic phase after the first six months.")
                        .font(.subheadline)
                        .foregroundColor(Color(UIColor(red: 1.00, green: 0.95, blue: 0.36, alpha: 1.00)))
                        .padding()
                }
                HStack(alignment: .center, spacing: 5.0) {
                    Text("In the acute phase, clinicians typically treat patients with range of motion (ROM) exercises in which they rotate and stretch the patient’s joints and muscles, support lung function via breathing exercises, and maximize patient comfort with the use of splints and sandbags. ")
                        .font(.subheadline)
                        .foregroundColor(Color(UIColor(red: 1.00, green: 0.95, blue: 0.36, alpha: 1.00)))
                        .padding()
                }
                HStack(alignment: .center, spacing: 5.0) {
                    Text("In the sub-acute phase, clinicians then shift the focus to physical therapy involving weight and resistance exercises in order to rebuild the patient’s ability to walk and use their muscles")
                        .font(.subheadline)
                        .foregroundColor(Color(UIColor(red: 1.00, green: 0.95, blue: 0.36, alpha: 1.00)))
                        .padding()
                }
                Group{
                }
                //Spacer()
            }
            VStack(alignment: .leading, spacing: 10){
                HStack(alignment: .center, spacing: 5.0) {
                    CircleImage(image: Image(materialDesignIcon: .localHospital48px, size: 60, color: .white), borderColor: Color(UIColor(red: 0.96, green: 0.59, blue: 0.19, alpha: 1.00)), shadowRadius: 5).padding()
                    Spacer()
                    Text("SCI Recovery")
                        .bold()
                        .padding()
                        .font(.title)
                        .foregroundColor(.white)
                        .background(Color(UIColor(red: 0.96, green: 0.59, blue: 0.19, alpha: 1.00)))
                        .padding()
                }
                HStack(alignment: .center, spacing: 5.0) {
                    Text("A good treatment plan for acute and sub-acute SCI patients during the six months following injury is foundational to SCI recovery, since success or failure during the preliminary phases has long-term effects for the outcomes of the patient’s chronic conditions.")
                        .font(.subheadline)
                        .foregroundColor(Color(UIColor(red: 1.00, green: 0.95, blue: 0.36, alpha: 1.00)))
                        .padding()
                }
                HStack(alignment: .center, spacing: 5.0) {
                    Text("One research team found that physical therapy contributes to ASIA classification C, D patients recovering a level of walking ability. Furthermore, SCI patients who show improvement early on are more likely to recover an additional degree of muscle function during the acute and sub-acute treatment phases.")
                        .font(.subheadline)
                        .foregroundColor(Color(UIColor(red: 1.00, green: 0.95, blue: 0.36, alpha: 1.00)))
                        .padding()
                }
                Group{
                }
                //Spacer()
            }
            VStack(alignment: .leading, spacing: 10){
                HStack(alignment: .center, spacing: 5.0) {
                    Text("SCI Prediction")
                        .bold()
                        .padding()
                        .font(.title)
                        .foregroundColor(.white)
                        .background(Color(UIColor(red: 0.96, green: 0.59, blue: 0.19, alpha: 1.00)))
                        .padding()
                    Spacer()
                    CircleImage(image: Image(materialDesignIcon: .contentCopy48px, size: 60, color: .white), borderColor: Color(UIColor(red: 0.96, green: 0.59, blue: 0.19, alpha: 1.00)), shadowRadius: 5).padding()
                }
                HStack(alignment: .center, spacing: 5.0) {
                    Text("These final sections are intended to provide an understanding of where care can be tailored so a new patient has a better chance at seeing recovery. The backbone of the machine learning portion will be the extensive National Spinal Cord Injury Statistical Center database which comprises more than 29,000 SCIs since 1973:")
                        .font(.subheadline)
                        .foregroundColor(Color(UIColor(red: 1.00, green: 0.95, blue: 0.36, alpha: 1.00)))
                        .padding()
                }
                Group{
                }
                //Spacer()
            }
            Button {
                apiController.postData()
            } label: {
                Text("Estimate Your ASIA Classification at Discharge")
                    .padding(5)
                    .background(.white)
                    .padding()
            }
        }
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}

struct CircleImage: View {
    var image: Image
    var borderColor: Color = .white
    var shadowRadius: CGFloat = 10
 
    var body: some View {
        image
            .clipShape(Circle())
            .overlay(Circle().stroke(borderColor, lineWidth: 4))
            .shadow(radius: shadowRadius)
    }
}
