//
//  Extensions.swift
//  SCI Recovery
//
//  Created by Tolga Saygi on 11/4/21.
//

import Foundation
import SwiftUI

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
