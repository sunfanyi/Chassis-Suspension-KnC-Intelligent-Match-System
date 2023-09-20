#include "QWFormCompare2.h"
#include "ui_QWFormCompare2.h"

QWFormCompare2::QWFormCompare2(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::QWFormCompare2)
{
    ui->setupUi(this);
}

QWFormCompare2::~QWFormCompare2()
{
    delete ui;
}
