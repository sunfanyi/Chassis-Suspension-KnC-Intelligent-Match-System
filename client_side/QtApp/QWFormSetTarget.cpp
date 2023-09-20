#include "QWFormSetTarget.h"
#include "ui_QWFormSetTarget.h"

QWFormSetTarget::QWFormSetTarget(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::QWFormSetTarget)
{
    ui->setupUi(this);
}

QWFormSetTarget::~QWFormSetTarget()
{
    delete ui;
}
