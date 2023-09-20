#ifndef QWFORMRESULT1_H
#define QWFORMRESULT1_H

#include <QWidget>

namespace Ui {
class QWFormResult;
}

class QWFormResult : public QWidget
{
    Q_OBJECT

public:
    explicit QWFormResult(QWidget *parent = nullptr);
    ~QWFormResult();

private:
    Ui::QWFormResult *ui;
};

#endif // QWFORMRESULT1_H
