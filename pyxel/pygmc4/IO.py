class IO :

    # References
    parent = None
    
    # ------------------------------------------------------------
    #   I/O Resources                                             
    # ------------------------------------------------------------

    # LED 
    LED      = [0,0,0,0,0,0,0]
    LED_7Seg = [0,0,0,0,0,0,0,0]

    # +-0-+ 
    # 5   1
    # +-6-+
    # 4   2
    # +-3-+ 8
    LED_Fig = [ [ 1,1,1,1,1,0,0,0 ], # 0
                [ 0,1,1,0,0,0,0,0 ], # 1
                [ 1,1,0,1,1,0,1,0 ], # 2
                [ 1,1,1,1,0,1,0,0 ], # 3
                [ 0,1,1,0,0,1,1,0 ], # 4
                [ 1,0,1,1,0,1,1,0 ], # 5
                [ 1,0,1,1,0,1,1,0 ], # 6
                [ 1,1,1,0,0,0,0,0 ], # 7
                [ 1,1,1,1,1,1,1,0 ], # 8
                [ 1,1,1,1,0,1,1,0 ], # 9
                [ 1,1,1,0,1,1,1,0 ], # A
                [ 0,0,1,1,1,1,1,0 ], # B
                [ 0,0,0,1,1,0,1,0 ], # C
                [ 0,1,1,1,1,0,1,0 ], # D
                [ 1,0,0,1,1,1,1,0 ], # E
                [ 1,0,0,0,1,1,1,0 ] ] # F
                
    # ------------------------------------------------------------
    #   I/O Emulation
    # ------------------------------------------------------------

    # I/O Initialize
    def IO_Init( self, p ) :
        self.parent = p


        return 0

    # I/O Finalialize
    def IO_Fin( self ) :

        return 0

# End of IO.py
        
    