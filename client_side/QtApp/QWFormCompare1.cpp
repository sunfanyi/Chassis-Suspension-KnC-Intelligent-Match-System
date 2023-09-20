#include "QWFormCompare1.h"
#include "ui_QWFormCompare.h"

QWFormCompare::QWFormCompare(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::QWFormCompare)
{
    ui->setupUi(this);
}

QWFormCompare::~QWFormCompare()
{
    delete ui;
}
