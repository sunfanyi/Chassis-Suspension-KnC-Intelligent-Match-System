#include "QWFormResult2.h"
#include "ui_QWFormResult2.h"

QWFormResult2::QWFormResult2(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::QWFormResult2)
{
    ui->setupUi(this);
}

QWFormResult2::~QWFormResult2()
{
    delete ui;
}
