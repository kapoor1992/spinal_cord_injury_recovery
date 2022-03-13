//
//  APIController.swift
//  SCI Recovery
//
//  Created by Tolga Saygi on 10/25/21.
//

import Alamofire
import Combine
import SwiftyJSON
import SwiftUI

class APIController: ObservableObject {
    init() {
    }
    
    func postData(model: RequestModel, completion: @escaping (ResponseModel) -> Void) {
        AF.request("http://144.202.111.88:8000/PostInference", method: .post, parameters: model, encoder: JSONParameterEncoder.default).responseJSON{ (response) in
            switch response.result {
            case .success(let JSON): // stores the json file in JSON variable
                // the JSON file is printed correctly
                print("Validation Successful with response JSON \(JSON)")
                // this variable is seen as nil outside this function (even in return)
                guard let itemsData = response.data else {
                    print("Request failed while parsing response")
                    return
                }
                do {
                    let decoder = JSONDecoder()
                    let item = try decoder.decode(ResponseModel.self, from: itemsData)
                    DispatchQueue.main.async {
                        completion(item)
                    }
                } catch {
                    print("Request failed while decoding response")
                    return
                }
                //completion(.success(JSON))
            case .failure(let error):
                print("Request failed with error \(error)")
                return//completion(.failure(error))
            }
        }
    }
}
