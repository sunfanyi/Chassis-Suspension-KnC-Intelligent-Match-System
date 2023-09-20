#include "QWFormSetWeight1.h"
#include "ui_QWFormSetWeight.h"

QWFormSetWeight::QWFormSetWeight(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::QWFormSetWeight)
{
    ui->setupUi(this);
}

QWFormSetWeight::~QWFormSetWeight()
{
    delete ui;
}
