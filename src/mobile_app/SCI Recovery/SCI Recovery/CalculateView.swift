//
//  CalculateView.swift
//  SCI Recovery
//
//  Created by Tolga Saygi on 11/4/21.
//

import SwiftUI
import MaterialDesignSymbol

struct CalculateView: View {
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
                    CircleImage(image: Image(materialDesignIcon: .report48px, size: 60, color: .white), borderColor: Color(UIColor(red: 0.96, green: 0.59, blue: 0.19, alpha: 1.00)), shadowRadius: 5).padding()
                    Spacer()
                    Text("Calculation")
                        .bold()
                        .padding()
                        .font(.title)
                        .foregroundColor(.white)
                        .background(Color(UIColor(red: 0.96, green: 0.59, blue: 0.19, alpha: 1.00)))
                        .padding()
                }
                HStack(alignment: .center, spacing: 5.0) {
                    Text("Form will be shown here.")
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
