//
//  RecoveryView.swift
//  SCI Recovery
//
//  Created by Tolga Saygi on 11/4/21.
//

import SwiftUI
import MaterialDesignSymbol

struct RecoveryView: View {
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
        }
    }
}
