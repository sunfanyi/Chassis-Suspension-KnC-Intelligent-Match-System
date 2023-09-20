#ifndef QWFORMCOMPARE1_H
#define QWFORMCOMPARE1_H

#include <QWidget>

namespace Ui {
class QWFormCompare;
}

class QWFormCompare : public QWidget
{
    Q_OBJECT

public:
    explicit QWFormCompare(QWidget *parent = nullptr);
    ~QWFormCompare();

private:
    Ui::QWFormCompare *ui;
};

#endif // QWFORMCOMPARE1_H
