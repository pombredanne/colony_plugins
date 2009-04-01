##################################################
# StockQuote_services_types.py
# generated by ZSI.generate.wsdl2python
##################################################


import ZSI
import ZSI.TCcompound
from ZSI.schema import LocalElementDeclaration, ElementDeclaration, TypeDefinition, GTD, GED

##############################
# targetNamespace
# http://www.webserviceX.NET/
##############################

class ns0:
    targetNamespace = "http://www.webserviceX.NET/"

    class GetQuote_Dec(ZSI.TCcompound.ComplexType, ElementDeclaration):
        literal = "GetQuote"
        schema = "http://www.webserviceX.NET/"
        def __init__(self, **kw):
            ns = ns0.GetQuote_Dec.schema
            TClist = [ZSI.TC.String(pname=(ns,"symbol"), aname="_symbol", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded"))]
            kw["pname"] = ("http://www.webserviceX.NET/","GetQuote")
            kw["aname"] = "_GetQuote"
            self.attribute_typecode_dict = {}
            ZSI.TCcompound.ComplexType.__init__(self,None,TClist,inorder=0,**kw)
            class Holder:
                typecode = self
                def __init__(self):
                    # pyclass
                    self._symbol = None
                    return
            Holder.__name__ = "GetQuote_Holder"
            self.pyclass = Holder

    class GetQuoteResponse_Dec(ZSI.TCcompound.ComplexType, ElementDeclaration):
        literal = "GetQuoteResponse"
        schema = "http://www.webserviceX.NET/"
        def __init__(self, **kw):
            ns = ns0.GetQuoteResponse_Dec.schema
            TClist = [ZSI.TC.String(pname=(ns,"GetQuoteResult"), aname="_GetQuoteResult", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded"))]
            kw["pname"] = ("http://www.webserviceX.NET/","GetQuoteResponse")
            kw["aname"] = "_GetQuoteResponse"
            self.attribute_typecode_dict = {}
            ZSI.TCcompound.ComplexType.__init__(self,None,TClist,inorder=0,**kw)
            class Holder:
                typecode = self
                def __init__(self):
                    # pyclass
                    self._GetQuoteResult = None
                    return
            Holder.__name__ = "GetQuoteResponse_Holder"
            self.pyclass = Holder

    class string_Dec(ZSI.TC.String, ElementDeclaration):
        literal = "string"
        schema = "http://www.webserviceX.NET/"
        def __init__(self, **kw):
            kw["pname"] = ("http://www.webserviceX.NET/","string")
            kw["aname"] = "_string"
            class IHolder(str): typecode=self
            kw["pyclass"] = IHolder
            IHolder.__name__ = "_string_immutable_holder"
            ZSI.TC.String.__init__(self, **kw)

# end class ns0 (tns: http://www.webserviceX.NET/)
