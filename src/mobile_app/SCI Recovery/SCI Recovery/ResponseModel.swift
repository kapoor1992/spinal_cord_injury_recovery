//
//  ResponseModel.swift
//  SCI Recovery
//
//  Created by Tolga Saygi on 10/23/21.
//

import Foundation

struct ResponseModel : Decodable {
    var prediction: String
    
    enum CodingKeys: String, CodingKey {
        case prediction = "Prediction"
    }
}
