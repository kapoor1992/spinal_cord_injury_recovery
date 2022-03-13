//
//  NavBarItem.swift
//  SCI Recovery
//
//  Created by Tolga Saygi on 11/4/21.
//

import SwiftUI
import PagerTabStripView

private class ButtonTheme: ObservableObject {
    @Published var textColor = Color.gray
}

struct NavBarItem: View, PagerTabViewDelegate {
    let title: String
    
    @ObservedObject fileprivate var theme = ButtonTheme()
    
    var body: some View {
        VStack {
            Text(title)
                .foregroundColor(theme.textColor)
                .font(.subheadline)
                .bold()
                .padding()
        }
        .background(Color.clear)
    }
    
    func setState(state: PagerTabViewState) {
        switch state {
        case .selected:
            self.theme.textColor = .white
        case .highlighted:
            self.theme.textColor = .red
        default:
            self.theme.textColor = .gray
        }
    }
}

struct NavBarItem_Previews: PreviewProvider {
    static var previews: some View {
        NavBarItem(title: "Tweets")
    }
}
