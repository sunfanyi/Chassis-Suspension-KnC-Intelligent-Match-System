#include "QWFormSetWeight2.h"
#include "ui_QWFormSetWeight2.h"

QWFormSetWeight2::QWFormSetWeight2(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::QWFormSetWeight2)
{
    ui->setupUi(this);
}

QWFormSetWeight2::~QWFormSetWeight2()
{
    delete ui;
}
