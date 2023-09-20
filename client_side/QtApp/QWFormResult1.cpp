#include "QWFormResult1.h"
#include "ui_QWFormResult.h"

QWFormResult::QWFormResult(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::QWFormResult)
{
    ui->setupUi(this);
}

QWFormResult::~QWFormResult()
{
    delete ui;
}
