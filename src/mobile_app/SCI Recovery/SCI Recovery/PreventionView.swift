//
//  PreventionView.swift
//  SCI Recovery
//
//  Created by Tolga Saygi on 11/4/21.
//

import SwiftUI
import MaterialDesignSymbol

struct PreventionView: View {
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
        }
    }
}
