#ifndef QWFORMSETWEIGHT1_H
#define QWFORMSETWEIGHT1_H

#include <QWidget>

namespace Ui {
class QWFormSetWeight;
}

class QWFormSetWeight : public QWidget
{
    Q_OBJECT

public:
    explicit QWFormSetWeight(QWidget *parent = nullptr);
    ~QWFormSetWeight();

private:
    Ui::QWFormSetWeight *ui;
};

#endif // QWFORMSETWEIGHT1_H
