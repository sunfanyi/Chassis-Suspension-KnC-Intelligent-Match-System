echo off

rem Copy the .ui file under QtApp and translate
call copy   .\QtApp\MainWIndow.ui     MainWindow.ui
call pyuic5     -o ui_MainWindow.py     MainWindow.ui

call copy   .\QtApp\QWFormWelcome.ui     QWFormWelcome.ui
call pyuic5     -o ui_QWFormWelcome.py     QWFormWelcome.ui

call copy   .\QtApp\QWFormImport.ui     QWFormImport.ui
call pyuic5     -o ui_QWFormImport.py     QWFormImport.ui

call copy   .\QtApp\QWFormSetTarget.ui     QWFormSetTarget.ui
call pyuic5     -o ui_QWFormSetTarget.py     QWFormSetTarget.ui

call copy   .\QtApp\QWFormSetWeight1.ui     QWFormSetWeight1.ui
call pyuic5     -o ui_QWFormSetWeight1.py     QWFormSetWeight1.ui

call copy   .\QtApp\QWFormSetWeight2.ui     QWFormSetWeight2.ui
call pyuic5     -o ui_QWFormSetWeight2.py     QWFormSetWeight2.ui

call copy   .\QtApp\QWFormCompare1.ui     QWFormCompare1.ui
call pyuic5     -o ui_QWFormCompare1.py     QWFormCompare1.ui

call copy   .\QtApp\QWFormCompare2.ui     QWFormCompare2.ui
call pyuic5     -o ui_QWFormCompare2.py     QWFormCompare2.ui

call copy   .\QtApp\QWFormResult1.ui     QWFormResult1.ui
call pyuic5     -o ui_QWFormResult1.py     QWFormResult1.ui

call copy   .\QtApp\QWFormResult2.ui     QWFormResult2.ui
call pyuic5     -o ui_QWFormResult2.py     QWFormResult2.ui


rem Copy resources file
call pyrcc5     .\QtApp\res.qrc  -o  res_rc.py
