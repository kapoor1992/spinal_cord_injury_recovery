//
//  RequestModel.swift
//  SCI Recovery
//
//  Created by Tolga Saygi on 10/23/21.
//

import Foundation

struct RequestModel : Codable {
    var f1: String
    var f2: String
    var f3: String
    
    enum CodingKeys: String, CodingKey {
        case f1
        case f2
        case f3
    }
}
