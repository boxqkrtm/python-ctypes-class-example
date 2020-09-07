#-*- coding: utf-8 -*-

import ctypes
 
class CHello(object):
 
    def __init__( self ):
        self.lib = ctypes.cdll.LoadLibrary('python integration example')
        self.lib.CHello_new.argtypes = []
        self.lib.CHello_new.restype = ctypes.c_void_p
        self.obj = self.lib.CHello_new()
 
    def printOut( self ):
        self.lib.CHello_print.argtypes = [ctypes.c_void_p]
        self.lib.CHello_print.restype = ctypes.c_void_p
        self.lib.CHello_print( self.obj )
 
    def push_back( self , s ):
        self.lib.CHello_push_back.argtypes = [ctypes.c_void_p, ctypes.c_wchar_p]
        self.lib.CHello_push_back.restype = ctypes.c_void_p
        self.lib.CHello_push_back( self.obj, s )

    def print( self, s ):
        self.lib.print.argtypes = [ctypes.c_wchar_p]
        self.lib.print.restype = ctypes.c_wchar_p
        val = self.lib.print(s)
        print("return", val)

    def testArr( self ):
        self.lib.intarraytest.argtypes = []
        self.lib.intarraytest.restype = ctypes.POINTER(ctypes.c_int32)
        vals = self.lib.intarraytest()
        valList = [vals[i] for i in range(3)]
        return valList

 
if __name__ == '__main__':
 
    f = CHello()
    f.print('hello world')
    f.push_back("-------------------------------------")
    f.push_back("  hello world ")
    f.push_back("-------------------------------------")
    f.printOut()
    print(f.testArr())