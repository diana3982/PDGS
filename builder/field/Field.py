class Field(object):

    def init(self, name=None, abbrev=None, description=None, mask=None, size=None, data_type=None, base=None, val_constraint=None, required=False, next=None):
        self.name = name
        self.abbrev = abbrev
        self.description
        self.mask = mask
        self.size = size
        self.data_type = data_type
        self.base = base
        self.val_constraint = val_constraint
        self.required = required
        self.next = next

    def addNode(self, nodeToAdd):
        self.next = nodeToAdd

    def getFieldName(self):
        return self.name

    def getAbbreviation(self):
        return self.abbrev

    def getDescription(self):
        return self.description

    def getMask(self):
        if (self.mask == None):
            return "Not Applicable"
        return self.mask

    def getSize(self):
        return self.size

    def getDataType(self):
        return self.data_type

    def getBase(self):
        if(self.base == None):
            return "Not Applicable"
        return self.base

    def getValueConstraint(self):
        if(self.val_constraint == None):
            return "Not Applicable"
        return self.val_constraint

    def ifRequired(self):
        if(self.ifRequired == None):
            return "Not Applicable"
        return self.ifRequired
