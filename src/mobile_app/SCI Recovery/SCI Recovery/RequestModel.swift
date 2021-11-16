//
//  RequestModel.swift
//  SCI Recovery
//
//  Created by Tolga Saygi on 10/23/21.
//

import Foundation

struct RequestModel : Codable {
    var age: String
    var sex: String
    var loi: String
    var education: String
    var isVeteran: String
    var depression: String
    var diabetes: String
    var dailyAlcohol: String
    var lossOfCons: String
    var lossOfMem: String
    var tbi: String
    var race: String
    var marital: String
    var occupStatus: String
    var occupCode: String
    var primaryInsurance: String
    var anxiety: String
    var neuro: String
    var asia: String
    
    enum CodingKeys: String, CodingKey {
        case age = "Age - Injury"
        case sex = "Sex"
        case loi = "Level of Injury - Admission"
        case education = "Education - Injury"
        case isVeteran = "Veteran"
        case depression = "Depression - History"
        case diabetes = "Diabetes - History"
        case dailyAlcohol = "Daily Alcohol - History"
        case lossOfCons = "Loss of Consciousness - Injury"
        case lossOfMem = "Loss of Memory - Injury"
        case tbi = "TBI Likelihood - Injury"
        case race = "Race"
        case marital = "Marital Status - Injury"
        case occupStatus = "Occupation Status - Injury"
        case occupCode = "Occupation Code - Injury"
        case primaryInsurance = "Primary Insurance"
        case anxiety = "Anxiety - History"
        case neuro = "Neurologic Category - Admission"
        case asia = "ASIA - Admission"
    }
}
