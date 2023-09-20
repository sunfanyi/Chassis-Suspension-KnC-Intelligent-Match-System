#ifndef QWFORMSETTARGET_H
#define QWFORMSETTARGET_H

#include <QWidget>

namespace Ui {
class QWFormSetTarget;
}

class QWFormSetTarget : public QWidget
{
    Q_OBJECT

public:
    explicit QWFormSetTarget(QWidget *parent = nullptr);
    ~QWFormSetTarget();

private:
    Ui::QWFormSetTarget *ui;
};

#endif // QWFORMSETTARGET_H
