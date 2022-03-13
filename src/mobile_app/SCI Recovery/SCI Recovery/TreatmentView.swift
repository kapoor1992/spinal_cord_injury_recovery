//
//  TreatmentView.swift
//  SCI Recovery
//
//  Created by Tolga Saygi on 11/4/21.
//

import SwiftUI
import MaterialDesignSymbol

struct TreatmentView: View {
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
        }
    }
}
