#ifndef QWFORMSETWEIGHT2_H
#define QWFORMSETWEIGHT2_H

#include <QWidget>

namespace Ui {
class QWFormSetWeight2;
}

class QWFormSetWeight2 : public QWidget
{
    Q_OBJECT

public:
    explicit QWFormSetWeight2(QWidget *parent = nullptr);
    ~QWFormSetWeight2();

private:
    Ui::QWFormSetWeight2 *ui;
};

#endif // QWFORMSETWEIGHT2_H
