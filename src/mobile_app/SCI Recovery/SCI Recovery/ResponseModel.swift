//
//  ResponseModel.swift
//  SCI Recovery
//
//  Created by Tolga Saygi on 10/23/21.
//

import Foundation

struct ResponseModel : Decodable {
    var score: String
    var description: String
    var color: String
    
    enum CodingKeys: String, CodingKey {
        case score
        case description
        case color
    }
}
