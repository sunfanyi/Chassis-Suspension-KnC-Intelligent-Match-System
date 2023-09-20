#ifndef QWFORMWELCOME_H
#define QWFORMWELCOME_H

#include <QWidget>

namespace Ui {
class QWFormWelcome;
}

class QWFormWelcome : public QWidget
{
    Q_OBJECT

public:
    explicit QWFormWelcome(QWidget *parent = nullptr);
    ~QWFormWelcome();

private:
    Ui::QWFormWelcome *ui;
};

#endif // QWFORMWELCOME_H
