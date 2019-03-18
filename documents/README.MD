Front End:

Back END:
    EndPoints:
        Token/
            http://127.0.0.1:8000/Token/
            Params: 
            Type:
                POST
            Payload:
                {
                    "username": "",
                    "password": ""
                }
            Returns:
                {
                    "token": "8f3ee07191763b5a4c50b2e985e85d0b2bfa144a"
                }

        Address/
            http://100.1.253.16:8000/Address/
            Params: access_token
            Type:
                GET|POST
            Payload:
                {
                    "customerID": "",
                    "address1": "",
                    "address2": "",
                    "town": "",
                    "county": "",
                    "postcode": "",
                    "phoneNumber": "",
                    "email": "",
                    "country": "",
                    "city": ""
                }
            Returns:
            [
                {
                    "customerID": 8978864,
                    "address1": "Sutton House",
                    "address2": "Berry Hill Road",
                    "town": "Staffordshire",
                    "county": "Staffordshire",
                    "postcode": "ST4 2NL",
                    "phoneNumber": "01782 838822",
                    "email": "rkw@rkwltd.com",
                    "country": "UK",
                    "city": "Stoke"
                }
            ]

        Manufacturer/
            http://100.1.253.16:8000/Manufacturer/
            Params: access_token
            Type:
                GET
            Returns:
                [
                    {
                        "manufacturerCode": "MORPHY"
                    }
                ]

        Productlist/
            http://100.1.253.16:8000/Productlist/
            Params: access_token|manufacturerCode|itemno|LTPrice|GTPrice
            Type:
                GET
            Returns:
                [
                    {
                        "id": 99906,
                        "itemno": "HBHD01",
                        "description": "Hand Blender Holder Accessory",
                        "price": "14.48"
                    }
                ]

        ProductDetailed/
            http://100.1.253.16:8000/ProductDetailed/
            Params: access_token|itemno
            Type:
                GET
            Returns:
                [
                    {
                        "id": 104649,
                        "itemno": "T14001",
                        "description": "Halogen Low Fat Air Fryer",
                        "description2": "Black",
                        "price": "29.95",
                        "colour": "BLACK",
                        "manufacturerCode": "TOWER",
                        "Product_Category": "EOL",
                        "RRP": "99.99",
                        "SSP": "44.99",
                        "FreeStock": 100,
                        "ItemSpec1": "1300W of power uses less energy and cooks 3 times faster",
                        "ItemSpec2": "12 litre bowl with 5L extender ring great for families",
                        "ItemSpec3": "Triple cooking power of halogen / convection and infrared",
                        "ItemSpec4": "Removable glass bowl for easy cleaning and observation",
                        "ItemSpec5": "Cooks food from frozen no thawing time needed",
                        "ItemSpec6": "Halogen heating element heats directly",
                        "ItemSpec7": "Added browning roasting and flavour enhancement",
                        "ItemSpec8": "Convection circulates the air for even heat distribution",
                        "ItemSpec9": "Includes recipe book",
                        "ItemSpec10": "",
                        "TI": 3,
                        "HI": 5,
                        "Item_Height": "32.40",
                        "Item_Length": "32.40",
                        "Item_Width": "39.50",
                        "ProductPaging_Height": "23.10",
                        "ProductPaging_Length": "36.40",
                        "ProductPaging_Width": "36.40",
                        "CartonHeight": "24.60",
                        "CartonLength": "38.20",
                        "CartonWidth": "73.50",
                        "palletQty": 30,
                        "cartonQty": 2,
                        "restockDate": "2019-03-15",
                        "IPGID": -1
                    }
                ]