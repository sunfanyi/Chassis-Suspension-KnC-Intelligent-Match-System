#ifndef QWFORMRESULT2_H
#define QWFORMRESULT2_H

#include <QWidget>

namespace Ui {
class QWFormResult2;
}

class QWFormResult2 : public QWidget
{
    Q_OBJECT

public:
    explicit QWFormResult2(QWidget *parent = nullptr);
    ~QWFormResult2();

private:
    Ui::QWFormResult2 *ui;
};

#endif // QWFORMRESULT2_H
