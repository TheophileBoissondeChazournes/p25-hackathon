#include <iostream>

struct Matrix {
    int rows;
    int cols;
    double* data;

    Matrix(int r, int c) : rows(r), cols(c) {
        data = new double[rows * cols];
    }

    Matrix(const Matrix& other) : rows(other.rows), cols(other.cols) {
        data = new double[rows * cols];
        for(int i=0; i<rows*cols; i++) data[i] = other.data[i];
    }

    ~Matrix() {
        delete[] data;
    }

    void set_value(int r, int c, double val) {
        data[r * cols + c] = val;
    }

    double get_value(int r, int c) const {
        return data[r * cols + c];
    }

    Matrix somme(const Matrix& other) {
        Matrix res(rows, cols);
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                res.set_value(i, j, get_value(i, j) + other.get_value(i, j));
            }
        }
        return res;
    }

    Matrix multiplicationScalaire(double s) {
        Matrix res(rows, cols);
        for (int i = 0; i < rows * cols; i++) {
             res.data[i] = data[i] * s;
        }
        return res;
    }

    Matrix produitMatriciel(const Matrix& other) {
        Matrix resultat(rows, other.cols);
        for(int x=0; x < resultat.rows * resultat.cols; x++) resultat.data[x] = 0; 

        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < other.cols; j++) {
                for (int k = 0; k < cols; k++) {
                    double val = resultat.get_value(i, j) + (get_value(i, k) * other.get_value(k, j));
                    resultat.set_value(i, j, val);
                }
            }
        }
        return resultat;
    }

    void print() {
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                std::cout << get_value(i, j) << " ";
            }
            std::cout << std::endl;
        }
        std::cout << std::endl;
    }
};

int main() {

    Matrix A(2, 2);
    A.set_value(0, 0, 1.0); A.set_value(0, 1, 2.0);
    A.set_value(1, 0, 3.0); A.set_value(1, 1, 4.0);


    Matrix B(2, 2);
    B.set_value(0, 0, 2.0); B.set_value(0, 1, 0.0);
    B.set_value(1, 0, 1.0); B.set_value(1, 1, 2.0);

    std::cout << "Somme A + B :" << std::endl;
    Matrix C = A.somme(B);
    C.print();

    std::cout << "Produit A * B :" << std::endl;
    Matrix D = A.produitMatriciel(B);
    D.print();

    std::cout <<"Produit de A par 3 :"<< std::endl;
    Matrix E=A.multiplicationScalaire(3);
    A.print(); 

    return 0;
}