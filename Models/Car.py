class Car: 

    def __init__(self, CAR_ID , CAR_UUID , CAR_BRAND,CAR_COLOR ,CAR_PRICE,CAR_LIC_PLATE, CAR_US_ID ):
        self.CAR_ID         =   CAR_ID
        self.CAR_UUID       =   CAR_UUID        
        self.CAR_BRAND      =   CAR_BRAND
        self.CAR_COLOR      =   CAR_COLOR
        self.CAR_PRICE      =   CAR_PRICE
        self.CAR_LIC_PLATE  =   CAR_LIC_PLATE
        self.CAR_US_ID      =   CAR_US_ID

    def to_dic(self):
        return {
            "id"        : self.CAR_ID          ,
            "uuid"      : self.CAR_UUID        ,
            "brand"     : self.CAR_BRAND       ,
            "color"     : self.CAR_COLOR       ,
            "price"     : self.CAR_PRICE       ,
            "lic_plate" : self.CAR_LIC_PLATE   ,
            "us_id"     : self.CAR_US_ID
        }
        