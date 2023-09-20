QT       += core gui

greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

CONFIG += c++11

# You can make your code fail to compile if it uses deprecated APIs.
# In order to do so, uncomment the following line.
#DEFINES += QT_DISABLE_DEPRECATED_BEFORE=0x060000    # disables all the APIs deprecated before Qt 6.0.0

SOURCES += \
    QWFormCompare1.cpp \
    QWFormCompare2.cpp \
    QWFormImport.cpp \
    QWFormResult1.cpp \
    QWFormResult2.cpp \
    QWFormSetTarget.cpp \
    QWFormSetWeight1.cpp \
    QWFormSetWeight2.cpp \
    QWFormWelcome.cpp \
    main.cpp \
    MainWindow.cpp \
    temp_qss_SetTarget.cpp

HEADERS += \
    MainWindow.h \
    QWFormCompare1.h \
    QWFormCompare2.h \
    QWFormImport.h \
    QWFormResult1.h \
    QWFormResult2.h \
    QWFormSetTarget.h \
    QWFormSetWeight1.h \
    QWFormSetWeight2.h \
    QWFormWelcome.h \
    temp_qss_SetTarget.h

FORMS += \
    MainWindow.ui \
    QWFormCompare1.ui \
    QWFormCompare2.ui \
    QWFormImport.ui \
    QWFormResult1.ui \
    QWFormResult2.ui \
    QWFormSetTarget.ui \
    QWFormSetWeight1.ui \
    QWFormSetWeight2.ui \
    QWFormWelcome.ui \
    temp_qss_SetTarget.ui

# Default rules for deployment.
qnx: target.path = /tmp/$${TARGET}/bin
else: unix:!android: target.path = /opt/$${TARGET}/bin
!isEmpty(target.path): INSTALLS += target

RESOURCES += \
    res.qrc
