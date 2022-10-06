MIN_ANGLE        =           0
MAX_ANGLE        =           180

LF_KNEE_PIN      =           10
LF_SHOULDER_PIN  =           9
LF_HIP_PIN       =           8
LB_KNEE_PIN      =           2
LB_SHOULDER_PIN  =           1
LB_HIP_PIN       =           0
RF_KNEE_PIN      =           14
RF_SHOULDER_PIN  =           13
RF_HIP_PIN       =           12
RB_KNEE_PIN      =           6
RB_SHOULDER_PIN  =           5
RB_HIP_PIN       =           4

'''
RF_KNEE_INIT     =           70
RF_SHOULDER_INIT =           80
RF_HIP_INIT      =           60
RB_KNEE_INIT     =           75 
RB_SHOULDER_INIT =           60 
RB_HIP_INIT      =           85 
LF_KNEE_INIT     =           90 
LF_SHOULDER_INIT =           100 
LF_HIP_INIT      =           65 
LB_KNEE_INIT     =           94 
LB_SHOULDER_INIT =           65 
LB_HIP_INIT      =           55 
'''
RF_KNEE_INIT     =           90
RF_SHOULDER_INIT =           90
RF_HIP_INIT      =           90
RB_KNEE_INIT     =           90 
RB_SHOULDER_INIT =           90
RB_HIP_INIT      =           90 
LF_KNEE_INIT     =           90 
LF_SHOULDER_INIT =           90 
LF_HIP_INIT      =           90
LB_KNEE_INIT     =           90 
LB_SHOULDER_INIT =           90
LB_HIP_INIT      =           90 
RF_LEG_PIN           =   [RF_KNEE_PIN, RF_SHOULDER_PIN, RF_HIP_PIN]
RB_LEG_PIN           =   [RB_KNEE_PIN, RB_SHOULDER_PIN, RB_HIP_PIN]
LF_LEG_PIN           =   [LF_KNEE_PIN, LF_SHOULDER_PIN, LF_HIP_PIN]
LB_LEG_PIN           =   [LB_KNEE_PIN, LB_SHOULDER_PIN, LB_HIP_PIN]

RF_LEG_INIT      =   [RF_KNEE_INIT, RF_SHOULDER_INIT, RF_HIP_INIT]
RB_LEG_INIT      =   [RB_KNEE_INIT, RB_SHOULDER_INIT, RB_HIP_INIT]
LF_LEG_INIT      =   [LF_KNEE_INIT, LF_SHOULDER_INIT, LF_HIP_INIT]
LB_LEG_INIT      =   [LB_KNEE_INIT, LB_SHOULDER_INIT, LB_HIP_INIT]

RF_LEG_FWD = [RF_KNEE_INIT + 15, RF_SHOULDER_INIT - 20, RF_HIP_INIT]
RB_LEG_FWD = [RB_KNEE_INIT + 15, RB_SHOULDER_INIT - 20, RB_HIP_INIT]
LF_LEG_FWD = [LF_KNEE_INIT - 15, LF_SHOULDER_INIT + 20, LF_HIP_INIT]
LB_LEG_FWD = [LB_KNEE_INIT - 15, LB_SHOULDER_INIT + 20, LB_HIP_INIT]
