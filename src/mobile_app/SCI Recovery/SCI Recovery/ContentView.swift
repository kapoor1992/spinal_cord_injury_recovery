//
//  ContentView.swift
//  SCI Recovery
//
//  Created by Tolga Saygi on 10/25/21.
//

import SwiftUI
import MaterialDesignSymbol
import PagerTabStripView

struct ContentView: View {
    @State var apiController = APIController()
    @State var selection = 5
    
    init(){
        let navigationBarAppearance = UINavigationBarAppearance()
        navigationBarAppearance.backgroundColor = UIColor(red: 0.03, green: 0.35, blue: 0.36, alpha: 1.00)
        UIScrollView.appearance().backgroundColor = UIColor(red: 0.03, green: 0.35, blue: 0.36, alpha: 1.00)
    }
    
    var body: some View {
        PagerTabStripView(selection: $selection) {
            PreventionView()
                .pagerTabItem {
                    NavBarItem(title: "SCI Prevention")
                }
            TreatmentView()
                .pagerTabItem {
                    NavBarItem(title: "SCI Treatment")
                }
            RecoveryView()
                .pagerTabItem {
                    NavBarItem(title: "SCI Recovery")
                }
            PredictionView()
                .pagerTabItem {
                    NavBarItem(title: "SCI Prediction")
                }
            ImportanceView()
                .pagerTabItem {
                    NavBarItem(title: "Importance")
                }
            CalculateView()
                .pagerTabItem {
                    NavBarItem(title: "Calculate")
                }
        }
        .frame(alignment: .center)
        .pagerTabStripViewStyle(.scrollableBarButton(indicatorBarColor: Color.blue, tabItemSpacing: 15, tabItemHeight: 50))
        .navigationBarTitleDisplayMode(.inline)
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
