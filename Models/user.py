class User:

    def __init__(self,id,uuid, fname, lname, tdoc, doc, dbirth):
        self.US_ID          =   id
        self.US_UUID        =   uuid
        self.US_FIRST_NAME  =   fname
        self.US_LAST_NAME   =   lname
        self.US_TYPE_DOC    =   tdoc
        self.US_DOCUMENT    =   doc
        self.US_DATE_BIRTH  =   dbirth

    # convierte objeto en diccionario 
    def to_dic(self):
        return {
            "id"    : self.US_ID             ,    
            "uuid"  : self.US_UUID           ,   
            "fname" : self.US_FIRST_NAME     ,
            "lname" : self.US_LAST_NAME      , 
            "tdoc"  : self.US_TYPE_DOC       ,
            "doc"   : self.US_DOCUMENT       ,
            "dbirth": self.US_DATE_BIRTH 
        }