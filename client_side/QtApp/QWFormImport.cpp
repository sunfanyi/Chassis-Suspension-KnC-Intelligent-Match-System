#include "QWFormImport.h"
#include "ui_QWFormImport.h"

QWFormImport::QWFormImport(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::QWFormImport)
{
    ui->setupUi(this);
}

QWFormImport::~QWFormImport()
{
    delete ui;
}
