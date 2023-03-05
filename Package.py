class Package:

    def __init__(self, Package_ID, Delivery_address, Delivery_city, Delivery_zip, Deliver_State, Delivery_deadline, Package_weight, Delivery_status):
        self.Package_ID = Package_ID
        self.Delivery_address = Delivery_address
        self.Delivery_city = Delivery_city
        self.Delivery_zip = Delivery_zip
        self.Delivery_State = Deliver_State
        self.Delivery_deadline = Delivery_deadline
        self.Package_weight = Package_weight
        self.Delivery_status = Delivery_status


        def __str__(self):
            return " %s, %s, %s, %s, %s, %s, %s, %s" % (self.Package_ID, self.Delivery_Address, self.Delivery_city, self.Delivery_zip, self.Delivery_State, self.Delivery_deadline, self.Package_weight, self.Delivery_status)

