//
//  ImportanceView.swift
//  SCI Recovery
//
//  Created by Tolga Saygi on 12/2/21.
//

import SwiftUI
import MaterialDesignSymbol
import PagerTabStripView

struct ImportanceView: View {
    @State var apiController = APIController()
    
    init(){
        let navigationBarAppearance = UINavigationBarAppearance()
        navigationBarAppearance.backgroundColor = UIColor(red: 0.03, green: 0.35, blue: 0.36, alpha: 1.00)
        UIScrollView.appearance().backgroundColor = UIColor(red: 0.03, green: 0.35, blue: 0.36, alpha: 1.00)
    }
    
    var body: some View {
        ScrollView([.horizontal, .vertical], showsIndicators: false) {
            VStack(alignment: .leading, spacing: 10){
                Image("importance")
                    //.resizable()
                    .scaledToFit()
            }
        }
    }
}

