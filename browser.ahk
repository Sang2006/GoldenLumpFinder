#NoEnv
SendMode Input
SetWorkingDir %A_ScriptDir%

; Set a variable to track whether the loop should continue or stop
global ContinueLoop := True

; Set up the hotkey to start the script when Ctrl+Shift+X is pressed
^+x::
    SetTimer, LoopClicks, 100
    return

; Set up the hotkey to stop the script when Ctrl+Shift+Y is pressed
^+y::
    SetTimer, LoopClicks, Off
    global ContinueLoop := False
    return

LoopClicks:
    Loop {
        ; Exit the loop if ContinueLoop is set to False
        if (!ContinueLoop) {
            break
        }

        ; Click Lump (Replace with your screen cords)
        Click, 602, 214

        ; Click Options (Replace with your screen cords)
        Click, 620, 120

        ; Click Export (Replace with your screen cords)
        Click, 701, 463

        ; Reload the current webpage by sending the F5 key
        Send {F5}

        ; Wait for the page to finish loading before continuing
        Sleep, 2500
    }
    return
