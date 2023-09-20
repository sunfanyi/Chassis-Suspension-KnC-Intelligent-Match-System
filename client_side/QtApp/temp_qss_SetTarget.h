#ifndef TEMP_QSS_SETTARGET_H
#define TEMP_QSS_SETTARGET_H

#include <QWidget>

namespace Ui {
class temp_qss_SetTarget;
}

class temp_qss_SetTarget : public QWidget
{
    Q_OBJECT

public:
    explicit temp_qss_SetTarget(QWidget *parent = nullptr);
    ~temp_qss_SetTarget();

private:
    Ui::temp_qss_SetTarget *ui;
};

#endif // TEMP_QSS_SETTARGET_H
