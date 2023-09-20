#include "temp_qss_SetTarget.h"
#include "ui_temp_qss_SetTarget.h"

temp_qss_SetTarget::temp_qss_SetTarget(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::temp_qss_SetTarget)
{
    ui->setupUi(this);
}

temp_qss_SetTarget::~temp_qss_SetTarget()
{
    delete ui;
}
