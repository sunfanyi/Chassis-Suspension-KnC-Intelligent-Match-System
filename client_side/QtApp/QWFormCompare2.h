#ifndef QWFORMCOMPARE2_H
#define QWFORMCOMPARE2_H

#include <QWidget>

namespace Ui {
class QWFormCompare2;
}

class QWFormCompare2 : public QWidget
{
    Q_OBJECT

public:
    explicit QWFormCompare2(QWidget *parent = nullptr);
    ~QWFormCompare2();

private:
    Ui::QWFormCompare2 *ui;
};

#endif // QWFORMCOMPARE2_H
