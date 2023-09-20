#ifndef QWFORMIMPORT_H
#define QWFORMIMPORT_H

#include <QMainWindow>

namespace Ui {
class QWFormImport;
}

class QWFormImport : public QMainWindow
{
    Q_OBJECT

public:
    explicit QWFormImport(QWidget *parent = nullptr);
    ~QWFormImport();

private:
    Ui::QWFormImport *ui;
};

#endif // QWFORMIMPORT_H
