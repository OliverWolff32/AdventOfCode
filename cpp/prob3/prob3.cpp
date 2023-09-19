#include <iostream>
#include <fstream>
using namespace std;

int main() {
    string line;
    ifstream myfile ("prob3.txt");
    int sum = 0;
    while(getline(myfile, line)) {
        string h1 = line.substr(0, line.size()/2);
        string h2 = line.substr(line.size()/2);
        for(char c : h1) {
            for(char c2 : h2) {
                if (c == c2) {
                    cout << c;
                    cout << c2;
                    if(islower(c)) {
                        sum += c - 96;
                        goto end;
                    } else {
                        sum += c - 38;
                        goto end;
                    }
                }
            }
        }
        end:;
    }
    cout << sum;
    return 0;
}
