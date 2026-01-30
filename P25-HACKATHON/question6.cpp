#include <iostream>
#include <vector>

struct Triplet {
    int r;
    int c;
    double v;
};

class SparseMatrix {
private: 
    int rows;
    int cols;
    std::vector<Triplet> elements;

public:
    SparseMatrix(int r, int c) : rows(r), cols(c) {}

    void set_value(int r, int c, double value){
        for(auto it = elements.begin(); it != elements.end(); ++it){
            if(it->r == r && it->c == c){
                if(value == 0){
                    elements.erase(it);
                } else {
                    it->v = value;
            }
                return;
        }
    }

        if(value!=0){
            elements.push_back({r,c,value});
        }

    }

    double get_value(int r, int c) const{
        for(auto it = elements.begin(); it != elements.end(); ++it){
            if((it->r == r) && (it->c == c)){
                return it->v;
            }
        }
        return 0;
    }

    SparseMatrix somme(const SparseMatrix& other) {
        SparseMatrix res(rows, cols);
        for(auto& el : elements){
            res.set_value(el.r, el.c, el.v);
        }
        for(auto& el : other.elements){
            res.set_value(el.r, el.c, res.get_value(el.r, el.c) + el.v);
        }
        return res;
    }

    SparseMatrix MultiplicationScalaire(const double scalaire){
        SparseMatrix res(rows, cols);
        for (auto& el : elements){
            res.set_value(el.r, el.c, scalaire * el.v);
        }
        return res;
    }

    SparseMatrix ProduitMatriciel(const SparseMatrix& other){
        SparseMatrix res(rows, other.cols);
        for(auto& el1 : elements){
            for(auto& el2 : other.elements){
                if(el1.c == el2.r){
                    double val = res.get_value(el1.r, el2.c) + (el1.v * el2.v);
                    res.set_value(el1.r, el2.c, val);
                }
            }
        }
        return res;
    }

    void debugPrint() {
        std::cout << "Matrice " << rows << "x" << cols << std::endl;
        std::cout << "Elements stockés (Non-Zéro) : " << elements.size() << std::endl;
        for (const auto& el : elements) {
            std::cout << "  -> Case (" << el.r << "," << el.c << ") = " << el.v << std::endl;
        }
    }

    void print() {
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                std::cout << get_value(i, j) << " ";
            }
            std::cout << std::endl;
        }
    }
};

    int main() {

    SparseMatrix A(2, 2);
    A.set_value(0, 0, 1.0); A.set_value(0, 1, 2.0);
    A.set_value(1, 0, 3.0); A.set_value(1, 1, 4.0);


    SparseMatrix B(2, 2);
    B.set_value(0, 0, 2.0); B.set_value(0, 1, 0.0); 
    B.set_value(1, 0, 1.0); B.set_value(1, 1, 2.0);

    std::cout << "--- Matrice A ---" << std::endl;
    A.print();

    std::cout << "--- Matrice B ---" << std::endl;
    B.print();

    std::cout << "Somme A + B :" << std::endl;
    SparseMatrix C = A.somme(B);
    C.print();

    std::cout << "Produit A * B :" << std::endl;
    SparseMatrix D = A.ProduitMatriciel(B);
    D.print();

    std::cout <<"Produit de A par 3 :"<< std::endl;
    SparseMatrix E = A.MultiplicationScalaire(3.0);
    E.print(); 

    return 0;
}
