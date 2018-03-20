Header header

# dState of the gascontroller
float64 GasPid_dState

# iState of the gascontroller
float64 GasPid_iState

# timestamp of the previous update of the gascontroller [s]
float64 GasPid_tPrevious

# timestamp of the most recent update of the gascontroller [s]
float64 GasPid_tCurrent

# pTerm of the gascontroller
float64 GasPid_pTerm

# iTerm of the gascontroller
float64 GasPid_iTerm

# dTerm of the gascontroller
float64 GasPid_dTerm

# The result of the gascontroller 
float64 GasPid_result

# The reference value of the gascontroller [m/s]
float64 GasPid_referenceValue

# The current (measured) value of the controlled variable of the gascontroller [m/s]
float64 GasPid_currentValue


# dState of the brakecontroller
float64 BrakePid_dState

# iState of the brakecontroller
float64 BrakePid_iState

# timestamp of the previous update of the brakecontroller [s]
float64 BrakePid_tPrevious

# timestamp of the most recent update of the brakecontroller [s]
float64 BrakePid_tCurrent

# pTerm of the brakecontroller
float64 BrakePid_pTerm

# iTerm of the brakecontroller
float64 BrakePid_iTerm

# dTerm of the brakecontroller
float64 BrakePid_dTerm

# The result of the brakecontroller 
float64 BrakePid_result

# The reference value of the brakecontroller [m/s]
float64 BrakePid_referenceValue

# The current (measured) value of the controlled variable of the brakecontroller [m/s]
float64 BrakePid_currentValue


# The feedforward offset of the steering adaptation of the gascontroller
float64 GasAdaptation_ffSteering

# The currently activated controller: true=gasCtrl; false=brakeController
bool activeController

# The final result of the gascontroller
int32 finalGas

# The final result of the brakecontroller
int32 finalBrake

