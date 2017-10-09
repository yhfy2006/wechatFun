//
//  ViewController.swift
//  wechatFuniOS
//
//  Created by He, Changchen on 10/6/17.
//  Copyright © 2017 He, Changchen. All rights reserved.
//

import UIKit
import Alamofire
import AlamofireImage

class ViewController: UIViewController {
    
    @IBOutlet weak var botIdText: UILabel!
    @IBOutlet weak var startButton: UIButton!
    @IBOutlet weak var qrCodeImg : UIImageView!
    
    var botid:String?
    

    override func viewDidLoad() {
        super.viewDidLoad()
        
        // Do any additional setup after loading the view, typically from a nib.
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }

    @IBAction func start(_ sender: UIButton) {
        Alamofire.request("http://127.0.0.1:5000/newbot").responseString { (response) in
            let botId = response.result.value
            if let botId = botId{
                self.botIdText.text = botId
                self.botid = botId
                UserDefaults.standard.set(botId, forKey: "botid")
                
                Timer.scheduledTimer(withTimeInterval: 3, repeats: true, block: { (timerh) in
                    self.fetchImage(timer: timerh)
                })
            
            }
        }
        
    }
    
    func fetchImage(timer: Timer!){
        if let botid = self.botid{
            let requestUrl = "http://127.0.0.1:5000/qr/" + botid
            Alamofire.request(requestUrl).responseImage { response in
                guard let image = response.result.value else {
                    // Handle error
                    return
                }
                // Do stuff with your image
                self.qrCodeImg.image = image;
                timer.invalidate()
                
                Timer.scheduledTimer(withTimeInterval: 3, repeats: true, block: { (timerh) in
                    self.fetchBotStatus(timer: timerh)
                })
            }
        }
    }
    
    func fetchBotStatus(timer:Timer){
        let requestUrl = "http://127.0.0.1:5000/loginstatus/" + self.botid!
        Alamofire.request(requestUrl).responseString { response in
            if let botId = response.result.value{
                if botId == "2"
                {
                    timer.invalidate()
                    self.loginSuccess()
                }
            }
            return
        }
    }
    
    func loginSuccess() {
        performSegue(withIdentifier: "loginSuccess", sender: self)
    }
    
    
}

