#include "QWFormWelcome.h"
#include "ui_QWFormWelcome.h"

QWFormWelcome::QWFormWelcome(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::QWFormWelcome)
{
    ui->setupUi(this);
}

QWFormWelcome::~QWFormWelcome()
{
    delete ui;
}
