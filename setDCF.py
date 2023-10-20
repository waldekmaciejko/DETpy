def setDCF (Cmiss, Cfa, Ptrue):
    """
    set Decision Cost Function parameters
    """
    
    DCF_parameters = [Cmiss, Cfa, Ptrue, 1-Ptrue]
    
    return DCF_parameters