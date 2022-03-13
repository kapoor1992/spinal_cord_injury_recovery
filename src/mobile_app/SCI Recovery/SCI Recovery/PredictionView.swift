//
//  PredictionView.swift
//  SCI Recovery
//
//  Created by Tolga Saygi on 11/4/21.
//

import SwiftUI
import MaterialDesignSymbol

struct PredictionView: View {
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
        }
    }
}
