//
//  APIController.swift
//  SCI Recovery
//
//  Created by Tolga Saygi on 10/25/21.
//

import Alamofire
import Combine
import SwiftUI

class APIController: ObservableObject {
    init() {
        postData()
    }
    
    // URL : 144.202.111.88
    func getData() {
        print("starting request")
        AF.request("http://144.202.111.88:8000/sample_get")
          .validate()
          .responseDecodable(of: ResponseModel.self) { (response) in
            guard let responseData = response.value else { return }
            print(responseData)
          }
    }

    func postData() {
        let model = RequestModel(f1: "value1", f2: "value2", f3: "value3")
        
        AF.request("http://144.202.111.88:8000/sample_post", method: .post, parameters: model, encoder: JSONParameterEncoder.default).responseJSON{ (response) in
            guard let responseData = response.value else { return }
            print(responseData)
          }
    }
}
